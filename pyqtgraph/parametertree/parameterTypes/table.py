from ...Qt import QtWidgets
from ...widgets.TypedTableWidget import TypedTableWidget, interpretRows, normalizeColumns
from ..Parameter import Parameter
from .basetypes import WidgetParameterItem


class TableParameterItem(WidgetParameterItem):
    """ParameterItem displaying a :class:`TypedTableWidget` below the parameter name, with
    buttons for adding and removing rows."""

    # most rows to show before the table scrolls
    maxVisibleRows = 10

    def __init__(self, param, depth):
        super().__init__(param, depth)
        self.table.sigValueChanged.connect(self._updateTableHeight)
        self._updateTableHeight()

    def makeWidget(self):
        self.asSubItem = True
        self.hideWidget = False
        self.table = TypedTableWidget(self.param.opts['columns'])

        self.addBtn = QtWidgets.QPushButton('Add row')
        self.addBtn.clicked.connect(self.table.addRow)
        self.removeBtn = QtWidgets.QPushButton('Remove row')
        self.removeBtn.clicked.connect(self.table.removeSelectedRows)
        btnLayout = QtWidgets.QHBoxLayout()
        btnLayout.setContentsMargins(0, 0, 0, 0)
        btnLayout.addWidget(self.addBtn)
        btnLayout.addWidget(self.removeBtn)
        btnLayout.addStretch()

        w = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(w)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        layout.addWidget(self.table)
        layout.addLayout(btnLayout)
        w.sigChanged = self.table.sigValueChanged
        w.value = self.table.value
        w.setValue = self.table.setValue
        w.setReadOnly = self.setReadOnly
        return w

    def setReadOnly(self, readOnly):
        self.table.setReadOnly(readOnly)
        self.addBtn.setVisible(not readOnly)
        self.removeBtn.setVisible(not readOnly)

    def _updateTableHeight(self):
        table = self.table
        rows = min(max(table.rowCount(), 1), self.maxVisibleRows)
        height = (table.horizontalHeader().height() + rows * table.verticalHeader().defaultSectionSize()
                  + 2 * table.frameWidth())
        table.setFixedHeight(height)
        self.subItem.setSizeHint(0, self.widget.sizeHint())

    def updateEditorVisible(self, sel=None):
        super().updateEditorVisible(sel)
        # don't leave an empty row where the table would be
        self.subItem.setHidden(self.valueIsNone())

    def updateDisplayLabel(self, value=None):
        if value is None and not self.valueIsNone():
            n = self.table.rowCount()
            value = f"{n} row{'' if n == 1 else 's'}"
        super().updateDisplayLabel(value)

    def optsChanged(self, param, opts):
        super().optsChanged(param, opts)
        if 'columns' in opts:
            self.table.setColumns(opts['columns'])
            if self.param.hasValue() and self.param.value() is not None:
                self.table.setValue(self.param.value())


class TableParameter(Parameter):
    """Parameter whose value is a list of rows, each a tuple with one value per column.

    The ``columns`` option is required; it is a list of column definitions as described in
    :class:`~pyqtgraph.widgets.TypedTableWidget.TypedTableWidget`. Values are checked and
    converted to the column types when set.
    """
    itemClass = TableParameterItem

    def _interpretValue(self, v):
        return interpretRows(normalizeColumns(self.opts['columns']), v)
