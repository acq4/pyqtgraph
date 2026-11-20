import pytest

import pyqtgraph as pg
import pyqtgraph.parametertree as pt
from pyqtgraph.Qt import QtCore
from pyqtgraph.widgets.TypedTableWidget import VALUE_ROLE

app = pg.mkQApp()

COLUMNS = [
    dict(name='n', type='int', default=1),
    dict(name='duration', suffix='s', siPrefix=True, default=0.2),
    dict(name='pressure', suffix='Pa', siPrefix=True, limits=(-100e3, 0)),
]


def makeTree(**opts):
    param = pt.Parameter.create(name='pulses', type='table', columns=COLUMNS, **opts)
    tree = pt.ParameterTree()
    tree.setParameters(param, showTop=True)
    param._testTree = tree  # keep the tree alive
    return param, next(iter(param.items))


def test_table_value_conversion():
    param = pt.Parameter.create(name='pulses', type='table', columns=COLUMNS, value=[[1, 0.2, -30e3]])
    assert param.value() == [(1, 0.2, -30e3)]
    assert isinstance(param.value()[0][1], float)

    with pytest.raises(ValueError):
        param.setValue([(1, 0.2)])  # wrong row length
    with pytest.raises(ValueError):
        param.setValue([(1.5, 0.2, -30e3)])  # non-integer in int column
    with pytest.raises(ValueError):
        pg.TypedTableWidget([dict(name='x', type='complex')])


def test_table_item():
    rows = [(1, 0.2, -30e3), (2, 0.5, -60e3)]
    param, item = makeTree(value=rows)
    table = item.table
    assert table.rowCount() == 2
    assert table.item(1, 1).text() == '500 ms'
    assert table.item(1, 2).text() == '-60 kPa'
    assert item.displayLabel.text() == '2 rows'

    # parameter -> table
    param.setValue([(3, 1.0, -10e3)])
    assert table.value() == [(3, 1.0, -10e3)]
    assert item.displayLabel.text() == '1 row'

    # add row copies the last row; remove row drops the selection (or the last row)
    item.addBtn.click()
    assert param.value() == [(3, 1.0, -10e3), (3, 1.0, -10e3)]
    table.selectRow(0)
    item.removeBtn.click()
    assert param.value() == [(3, 1.0, -10e3)]
    table.clearSelection()
    item.removeBtn.click()
    assert param.value() == []
    item.addBtn.click()
    assert param.value() == [(1, 0.2, 0.0)]  # column defaults


def test_table_cell_edit():
    param, item = makeTree(value=[(1, 0.2, -30e3)])
    table = item.table
    # editing a cell the way the delegate does updates the parameter and the display text
    table.model().setData(table.model().index(0, 1), 0.75, VALUE_ROLE)
    assert param.value() == [(1, 0.75, -30e3)]
    assert table.item(0, 1).text() == '750 ms'


def test_table_delegate_editor():
    param, item = makeTree(value=[(1, 0.2, -30e3)])
    table = item.table
    delegate = table.itemDelegate()
    index = table.model().index(0, 2)
    editor = delegate.createEditor(table.viewport(), None, index)
    assert isinstance(editor, pg.SpinBox)
    assert editor.opts['suffix'] == 'Pa'
    assert editor.opts['bounds'] == [-100e3, 0]
    delegate.setEditorData(editor, index)
    assert editor.value() == -30e3
    editor.lineEdit().setText('-45 kPa')
    delegate.setModelData(editor, table.model(), index)
    assert param.value() == [(1, 0.2, -45e3)]

    intEditor = delegate.createEditor(table.viewport(), None, table.model().index(0, 0))
    assert intEditor.opts['int']


def test_table_readonly():
    param, item = makeTree(value=[(1, 0.2, -30e3)], readonly=True)
    assert item.table.editTriggers() == item.table.EditTrigger.NoEditTriggers
    assert item.addBtn.isHidden()
    param.setReadonly(False)
    assert not item.addBtn.isHidden()


def test_optional_table():
    param, item = makeTree(value=None, optional=True)
    assert param.value() is None
    assert item.subItem.isHidden()
    assert item.displayLabel.text() == 'None'
    item.noneBtn.click()
    assert param.value() == []
    assert not item.subItem.isHidden()
    param.setValue([(1, 0.2, -30e3)])
    item.noneBtn.click()
    assert param.value() is None
    item.noneBtn.click()
    assert param.value() == [(1, 0.2, -30e3)]


def test_table_columns_change():
    param, item = makeTree(value=[(1, 0.2, -30e3)])
    param.setOpts(columns=COLUMNS + [dict(name='label', type='str')])
    # existing value no longer fits the columns
    assert item.table.columnCount() == 4
    param.setValue([(1, 0.2, -30e3, 'a')])
    assert item.table.value() == [(1, 0.2, -30e3, 'a')]
