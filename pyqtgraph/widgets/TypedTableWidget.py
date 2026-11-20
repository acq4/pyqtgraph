from contextlib import contextmanager

from .. import functions as fn
from ..Qt import QtCore, QtWidgets
from .SpinBox import SpinBox

__all__ = ['TypedTableWidget']

# item data role holding each cell's typed value (DisplayRole holds the formatted text)
VALUE_ROLE = QtCore.Qt.ItemDataRole.UserRole

# column options that are passed through to the SpinBox editor of numeric columns
_SPINBOX_OPTS = ('suffix', 'siPrefix', 'step', 'dec', 'minStep', 'decimals', 'finite')

def _toInt(v):
    i = int(v)
    if i != v:
        raise ValueError(f"{v!r} is not an integer")
    return i


# converters applied to the values in each column
_COLUMN_TYPES = {'float': float, 'int': _toInt, 'str': str}


def normalizeColumns(columns):
    """Return a copy of *columns* (see :class:`TypedTableWidget`) with defaults filled in."""
    columns = [dict(col) for col in columns]
    for col in columns:
        col.setdefault('title', col['name'])
        col.setdefault('type', 'float')
        if col['type'] not in _COLUMN_TYPES:
            raise ValueError(f"Unsupported column type {col['type']!r} for column {col['name']!r}")
        col.setdefault('default', '' if col['type'] == 'str' else 0)
    return columns


def interpretRows(columns, rows):
    """Return *rows* converted to a list of tuples of values typed according to *columns*
    (as returned by normalizeColumns).

    Raises ValueError if a row does not have exactly one value per column, or TypeError /
    ValueError if a value cannot be converted to its column's type.
    """
    out = []
    for row in rows:
        row = tuple(row)
        if len(row) != len(columns):
            raise ValueError(f"Table row {row!r} must have {len(columns)} values")
        out.append(tuple(_COLUMN_TYPES[col['type']](v) for col, v in zip(columns, row)))
    return out


class TypedTableWidget(QtWidgets.QTableWidget):
    """Editable table whose columns each hold values of a declared type.

    The value of the table is a list of rows, each row a tuple with one item per column.
    Edits are made with a type-appropriate editor (a :class:`SpinBox` for numeric columns),
    so every cell always holds a valid value of its column's type.

    *columns* is a list of dicts, one per column, with keys:

    ==========  ============================================================================
    name        Column name (required)
    title       Header text (default: name)
    type        'float', 'int' or 'str' (default: 'float')
    default     Value used to fill this column when a row is added to an empty table
                (default: 0 for numeric columns, '' for str)
    limits      (min, max) bounds for numeric columns
    suffix,     Passed to the :class:`SpinBox` editor of numeric columns; *suffix* and
    siPrefix,   *siPrefix* also determine how values are displayed.
    step, ...
    ==========  ============================================================================
    """

    sigValueChanged = QtCore.Signal(object)  # self

    def __init__(self, columns=(), parent=None):
        super().__init__(parent)
        self.columns = []
        self._updating = False
        self.setItemDelegate(_TypedItemDelegate(self))
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.verticalHeader().setDefaultSectionSize(self.fontMetrics().height() + 6)
        self.itemChanged.connect(self._itemChanged)
        self.setColumns(columns)

    def setColumns(self, columns):
        """Set the column definitions (see class docstring). Existing rows are cleared."""
        self.columns = normalizeColumns(columns)
        self.setRowCount(0)
        self.setColumnCount(len(self.columns))
        self.setHorizontalHeaderLabels([col['title'] for col in self.columns])
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

    def value(self):
        """Return the table contents as a list of row tuples."""
        return [
            tuple(self.item(r, c).data(VALUE_ROLE) for c in range(self.columnCount()))
            for r in range(self.rowCount())
        ]

    def setValue(self, rows):
        """Replace the table contents with *rows*, a sequence of row sequences."""
        rows = interpretRows(self.columns, rows)
        with self._blockItemChanged():
            self.setRowCount(0)
            for row in rows:
                self._appendRow(row)
        self.sigValueChanged.emit(self)

    def addRow(self):
        """Append a row, copying the last row or using column defaults if the table is empty."""
        values = self.value()
        row = values[-1] if values else tuple(col['default'] for col in self.columns)
        with self._blockItemChanged():
            self._appendRow(row)
        self.sigValueChanged.emit(self)

    def removeSelectedRows(self):
        """Remove the selected rows, or the last row if none is selected."""
        rows = sorted({idx.row() for idx in self.selectedIndexes()}, reverse=True)
        if not rows:
            rows = [self.rowCount() - 1]
        with self._blockItemChanged():
            for r in rows:
                if r >= 0:
                    self.removeRow(r)
        self.sigValueChanged.emit(self)

    def setReadOnly(self, readOnly):
        triggers = QtWidgets.QAbstractItemView.EditTrigger
        self.setEditTriggers(triggers.NoEditTriggers if readOnly else (
            triggers.DoubleClicked | triggers.EditKeyPressed | triggers.AnyKeyPressed))

    def displayText(self, column, value):
        """Return the text used to display *value* in *column*."""
        col = self.columns[column]
        if col['type'] == 'str':
            return value
        suffix = col.get('suffix', '')
        if col.get('siPrefix', False):
            return fn.siFormat(value, suffix=suffix)
        return f"{value:g} {suffix}".rstrip()

    def _appendRow(self, row):
        r = self.rowCount()
        self.insertRow(r)
        for c, v in enumerate(row):
            item = QtWidgets.QTableWidgetItem()
            item.setData(VALUE_ROLE, v)
            item.setText(self.displayText(c, v))
            self.setItem(r, c, item)

    def _itemChanged(self, item):
        if self._updating:
            return
        # the delegate sets VALUE_ROLE; refresh the display text to match
        with self._blockItemChanged():
            item.setText(self.displayText(item.column(), item.data(VALUE_ROLE)))
        self.sigValueChanged.emit(self)

    @contextmanager
    def _blockItemChanged(self):
        self._updating = True
        try:
            yield
        finally:
            self._updating = False


class _TypedItemDelegate(QtWidgets.QStyledItemDelegate):
    """Edits numeric cells with a SpinBox configured from the column definition."""

    def createEditor(self, parent, option, index):
        col = self.parent().columns[index.column()]
        if col['type'] == 'str':
            return QtWidgets.QLineEdit(parent)
        opts = {k: col[k] for k in _SPINBOX_OPTS if k in col}
        if 'limits' in col:
            opts['bounds'] = col['limits']
        editor = SpinBox(parent, int=col['type'] == 'int', compactHeight=False, **opts)
        return editor

    def setEditorData(self, editor, index):
        value = index.data(VALUE_ROLE)
        if isinstance(editor, SpinBox):
            editor.setValue(value)
            editor.selectNumber()
        else:
            editor.setText(value)

    def setModelData(self, editor, model, index):
        if isinstance(editor, SpinBox):
            editor.editingFinishedEvent()  # apply any text typed but not yet interpreted
            value = editor.value()
        else:
            value = editor.text()
        model.setData(index, value, VALUE_ROLE)
