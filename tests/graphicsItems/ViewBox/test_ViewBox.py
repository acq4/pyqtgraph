#import PySide
import pytest

import pyqtgraph as pg

app = pg.mkQApp()
qtest = pg.Qt.QtTest.QTest
QRectF = pg.QtCore.QRectF

def assertMapping(vb, r1, r2):
    assert vb.mapFromView(r1.topLeft()) == r2.topLeft()
    assert vb.mapFromView(r1.bottomLeft()) == r2.bottomLeft()
    assert vb.mapFromView(r1.topRight()) == r2.topRight()
    assert vb.mapFromView(r1.bottomRight()) == r2.bottomRight()

def init_viewbox():
    """Helper function to init the ViewBox
    """
    global win, vb
    
    win = pg.GraphicsLayoutWidget()
    win.ci.layout.setContentsMargins(0,0,0,0)
    win.resize(200, 200)
    win.show()
    vb = win.addViewBox()
    
    # set range before viewbox is shown
    vb.setRange(xRange=[0, 10], yRange=[0, 10], padding=0)
    
    # required to make mapFromView work properly.
    qtest.qWaitForWindowExposed(win)
    
    g = pg.GridItem()
    vb.addItem(g)
    app.processEvents()
    
def test_ViewBox():
    init_viewbox()
    
    w = vb.geometry().width()
    h = vb.geometry().height()
    view1 = QRectF(0, 0, 10, 10)
    size1 = QRectF(0, h, w, -h)
    assertMapping(vb, view1, size1)
    
    # test resize
    win.resize(400, 400)
    app.processEvents()
    w = vb.geometry().width()
    h = vb.geometry().height()
    size1 = QRectF(0, h, w, -h)
    assertMapping(vb, view1, size1)
    
    # now lock aspect
    vb.setAspectLocked()
    
    # test wide resize
    win.resize(800, 400)
    app.processEvents()
    w = vb.geometry().width()
    h = vb.geometry().height()
    view1 = QRectF(-5, 0, 20, 10)
    size1 = QRectF(0, h, w, -h)
    assertMapping(vb, view1, size1)
    
    # test tall resize
    win.resize(200, 400)
    app.processEvents()
    w = vb.geometry().width()
    h = vb.geometry().height()
    view1 = QRectF(0, -5, 10, 20)
    size1 = QRectF(0, h, w, -h)
    assertMapping(vb, view1, size1)

    win.close()


def test_ViewBox_setMenuEnabled():
    init_viewbox()
    vb.setMenuEnabled(True)
    assert vb.menu is not None
    vb.setMenuEnabled(False)
    assert vb.menu is None



def test_register_stores_destroyed_slot():
    """register() with a name stores a slot on the instance for later disconnection."""
    vb = pg.ViewBox(name="test_register_slot")
    try:
        assert vb._destroyedForgetSlot is not None
        assert callable(vb._destroyedForgetSlot)
        assert "test_register_slot" in pg.ViewBox.NamedViews
    finally:
        vb.close()


def test_unregister_clears_destroyed_slot():
    """unregister() disconnects and clears the destroyed slot to prevent double-removal."""
    vb = pg.ViewBox(name="test_unregister_slot")
    assert vb._destroyedForgetSlot is not None

    vb.unregister()

    assert vb._destroyedForgetSlot is None
    assert "test_unregister_slot" not in pg.ViewBox.NamedViews
    assert vb not in pg.ViewBox.AllViews


def test_no_crash_if_slot_called_after_unregister():
    """Calling forgetView after unregister (as destroyed signal would) must not crash.

    This is the core regression: the destroyed signal previously could fire
    after close() already cleaned up the view, causing a double-removal.
    """
    vb = pg.ViewBox(name="test_slot_after_close")
    vid = id(vb)
    name = "test_slot_after_close"

    vb.close()

    # Simulates what the destroyed signal slot would have done had it not been disconnected.
    # forgetView must handle a view that's already been removed without crashing.
    pg.ViewBox.forgetView(vid, name)


def test_unnamed_viewbox_has_no_destroyed_slot():
    """An unnamed ViewBox does not register a destroyed slot (nothing to forget)."""
    vb = pg.ViewBox()
    assert not hasattr(vb, '_destroyedForgetSlot') or vb._destroyedForgetSlot is None
    vb.close()


def test_close_removes_from_all_views():
    """close() fully unregisters the ViewBox from both AllViews and NamedViews."""
    vb = pg.ViewBox(name="test_close_cleanup")
    assert vb in pg.ViewBox.AllViews
    assert "test_close_cleanup" in pg.ViewBox.NamedViews

    vb.close()

    assert vb not in pg.ViewBox.AllViews
    assert "test_close_cleanup" not in pg.ViewBox.NamedViews


skipreason = "Skipping this test until someone has time to fix it."
@pytest.mark.skipif(True, reason=skipreason)
def test_limits_and_resize():
    init_viewbox()

    # now lock aspect
    vb.setAspectLocked()
    # test limits + resize  (aspect ratio constraint has priority over limits
    win.resize(400, 400)
    app.processEvents()
    vb.setLimits(xMin=0, xMax=10, yMin=0, yMax=10)
    win.resize(800, 400)
    app.processEvents()
    w = vb.geometry().width()
    h = vb.geometry().height()
    view1 = QRectF(-5, 0, 20, 10)
    size1 = QRectF(0, h, w, -h)
    assertMapping(vb, view1, size1)
