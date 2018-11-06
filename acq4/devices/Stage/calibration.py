from __future__ import print_function
import numpy as np
import scipy.stats, scipy.optimize
import acq4.pyqtgraph as pg
from acq4.Manager import getManager
from acq4.util import Qt
from acq4.util.target import Target


class CalibrationWindow(Qt.QWidget):
    def __init__(self, device):
        self.dev = device
        self._cammod = None
        self._camdev = None

        Qt.QWidget.__init__(self)
        self.resize(600, 300)
        self.setWindowTitle("Calibration: %s" % device.name())

        self.layout = Qt.QGridLayout()
        self.setLayout(self.layout)

        # tree columns:
        #   stage x, y, z   global x, y, z   error
        self.pointTree = Qt.QTreeWidget()
        self.pointTree.setHeaderLabels(['stage pos', 'parent pos', 'error'])
        self.pointTree.setColumnCount(3)
        self.layout.addWidget(self.pointTree, 0, 0)
        self.pointTree.setColumnWidth(0, 200)
        self.pointTree.setColumnWidth(1, 200)

        self.btnPanel = Qt.QWidget()
        self.btnPanelLayout = Qt.QHBoxLayout()
        self.btnPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.btnPanel.setLayout(self.btnPanelLayout)
        self.layout.addWidget(self.btnPanel, 1, 0)

        self.addPointBtn = Qt.QPushButton("add point")
        self.addPointBtn.setCheckable(True)
        self.btnPanelLayout.addWidget(self.addPointBtn)

        self.removePointBtn = Qt.QPushButton("remove point")
        self.btnPanelLayout.addWidget(self.removePointBtn)
        
        self.saveBtn = Qt.QPushButton("save calibration")
        self.btnPanelLayout.addWidget(self.saveBtn)

        self.addPointBtn.toggled.connect(self.addPointToggled)
        self.removePointBtn.clicked.connect(self.removePointClicked)
        self.saveBtn.clicked.connect(self.saveClicked)

        # more controls:
        #    Show calibration points (in camera module)
        #    Force orthogonal axes: xy, xz, yz

        self.loadCalibrationFromDevice()

        cam = self.getCameraDevice()
        cam.sigGlobalTransformChanged.connect(self.cameraTransformChanged)

    def addPointToggled(self):
        cammod = self.getCameraModule()
        if self.addPointBtn.isChecked():
            cammod.window().getView().scene().sigMouseClicked.connect(self.cameraModuleClicked)
            self.addPointBtn.setText("click new point..")
        else:
            pg.disconnect(cammod.window().getView().scene().sigMouseClicked, self.cameraModuleClicked)
            self.addPointBtn.setText("add point")

    def cameraModuleClicked(self, ev):
        if ev.button() != Qt.Qt.LeftButton:
            return

        camera = self.getCameraDevice()
        cameraPos = camera.mapToGlobal([0, 0, 0])

        globalPos = self._cammod.window().getView().mapSceneToView(ev.scenePos())
        globalPos = [globalPos.x(), globalPos.y(), cameraPos[2]]
        parentDev = self.dev.parentDevice()
        if parentDev is None:
            parentPos = globalPos
        else:
            parentPos = parentDev.mapFromGlobal(globalPos)

        stagePos = self.dev.getPosition()

        self.calibration['points'].append((stagePos, parentPos))
        item = self._addCalibrationPoint(stagePos, parentPos)

        target = Target()
        self._cammod.window().addItem(target)
        target.setPos(pg.Point(globalPos[:2]))
        target.setDepth(globalPos[2])
        target.setFocusDepth(globalPos[2])
        item.target = target

        # self.calibration.append({'global': pos, 'stage': self.dev.}

        self.addPointBtn.setChecked(False)
        self.recalculate()

    def cameraTransformChanged(self):
        cam = self.getCameraDevice()
        fdepth = cam.mapToGlobal([0, 0, 0])[2]

        items = [self.pointTree.topLevelItem(i) for i in range(self.pointTree.topLevelItemCount())]
        for item in items:
            if item.target is None:
                continue
            item.target.setFocusDepth(fdepth)

    def removePointClicked(self):
        sel = self.pointTree.selectedItems()[0]
        index = self.pointTree.indexOfTopLevelItem(sel)
        self.pointTree.takeTopLevelItem(index)
        if sel.target is not None:
            sel.target.scene().removeItem(sel.target)
        items = [self.pointTree.topLevelItem(i) for i in range(self.pointTree.topLevelItemCount())]
        self.calibration['points'] = [(item.stagePos, item.parentPos) for item in items]
        self.recalculate()

    def saveClicked(self):
        self.saveCalibrationToDevice()

    def loadCalibrationFromDevice(self):
        self.calibration = self.dev.readConfigFile('calibration')
        self.calibration.setdefault('points', [])
        for stagePos, parentPos in self.calibration['points']:
            self._addCalibrationPoint(stagePos, parentPos)
        self.recalculate()

    def saveCalibrationToDevice(self):
        self.dev.writeConfigFile(self.calibration, 'calibration')
        m = np.zeros((4, 4))
        m[:, :3] = self.transform
        m[3, 3] = 1
        tr = pg.Transform3D(m.T)
        self.dev._axisTransform = tr
        self.dev._inverseAxisTransform = None
        self.dev._updateTransform()

    def _addCalibrationPoint(self, stagePos, parentPos):
        item = Qt.QTreeWidgetItem(["%0.3g, %0.3g, %0.3g" % tuple(stagePos), "%0.3g, %0.3g, %0.3g" % tuple(parentPos), ""])
        self.pointTree.addTopLevelItem(item)
        item.stagePos = stagePos
        item.parentPos = parentPos
        item.target = None
        return item

    def recalculate(self):
        # identity affine transform matrix
        m = np.zeros((4, 3))
        m[:3] = np.eye(3)

        npts = len(self.calibration['points'])
        a = np.empty((npts, 4))
        a[:, 3] = 1  # needed for translation in affine mapping
        b = np.empty((npts, 3))
        for i, pt in enumerate(self.calibration['points']):
            a[i, :3] = pt[0]
            b[i] = pt[1]

        def mapError(x, a, b):
            # transform a through matrix x
            mappedPos = np.dot(a, x.reshape(4, 3))

            # measure distance from each mapped point to the desired point in b
            return np.linalg.norm(mappedPos - b, axis=1)

        def errFn(x, a, b):
            # reduce all distance errors to a scalar
            return np.linalg.norm(mapError(x, a, b))

        # find affine matrix that minimizes error
        self.result = scipy.optimize.minimize(errFn, m, (a, b))
        self.transform = self.result.x.reshape(4, 3)
        error = mapError(self.transform, a, b)

        for i in range(npts):
            item = self.pointTree.topLevelItem(i)
            item.setText(2, "%0.3g" % error[i])

    def getCameraModule(self):
        if self._cammod is None:
            manager = getManager()
            mods = manager.listInterfaces('cameraModule')
            if len(mods) == 0:
                raise Exception("Calibration requires an open camera module")
            self._cammod = manager.getModule(mods[0])
        return self._cammod

    def getCameraDevice(self):
        if self._camdev is None:
            manager = getManager()
            camName = self.dev.config.get('calibrationImagingDevice', None)
            if camName is None:
                raise Exception("Calibration requires 'calibrationImagingDevice' key in stage configuration.")
            self._camdev = manager.getDevice(camName)
        return self._camdev



class StageCalibration(object):
    # Old code, never used.. maybe just dump it!
    def __init__(self, stage):
        self.stage = stage
        self.framedelay = None

    def calibrate(self, camera):
        import imreg_dft  # FFT image registration by Chris Gohlke; available via pip
        n = 300
        dx = 10e-6

        self.move = None
        self.camera = camera
        self.offsets = np.empty((n, 2))
        self.frames = []
        self.index = 0
        # current stage position
        pos = self.stage.getPosition()

        # where to move on each update
        self.positions = np.zeros((n, 2))
        self.positions[:,0] = pos[0] + np.arange(n) * dx
        self.positions[:,1] = pos[1]

        camera.sigNewFrame.connect(self.newFrame)

    def newFrame(self, frame):
        try:
            if self.move is not None and not self.move.isDone():
                # stage is still moving; discard frame
                return

            if self.framedelay is None:
                # stage has stopped; discard 2 more frames to be sure
                # we get the right image.
                self.framedelay = pg.ptime.time() + 1./frame.info()['fps']
            elif self.framedelay < frame.info()['time']:
                # now we are ready to keep this frame.
                self.framedelay = None
                self.processFrame(frame)
        except Exception:
            pg.disconnect(self.camera.sigNewFrame, self.newFrame)
            raise

    def processFrame(self, frame):
        self.frames.append(frame)
        index = self.index

        # update index for next iteration
        self.index += 1

        # decide whether to move the stage
        finished = self.index >= self.positions.shape[0]
        if not finished:
            self.move = self.stage.moveTo(self.positions[self.index], 'slow')

        # calculate offset (while stage moves no next location)
        if index == 0:
            offset = (0, 0)
        else:
            compareIndex = max(0, index-10)
            offset, _ = imreg_dft.translation(frame.getImage(), self.frames[compareIndex].getImage())
            px = self.camera.getPixelSize()
            offset = self.offsets[compareIndex] + offset.astype(float) * [px.x(), px.y()]
        self.offsets[index] = offset

        # finish up if there are no more positions
        if finished:
            pg.disconnect(self.camera.sigNewFrame, self.newFrame)
            self.analyze()

    def analyze(self):
        # frames = []
        # for frame in self.frames:
        #     frames.append(frame.getImage()[np.newaxis, ...])
        # self.frameArray = np.concatenate(frames, axis=0)
        # self.imageView = pg.image(self.frameArray)

        # linear regression to determine scale between stage steps and camera microns
        x = ((self.positions - self.positions[0])**2).sum(axis=1)**0.5
        y = (self.offsets**2).sum(axis=1)**0.5
        slope, yint, r, p, stdev = scipy.stats.linregress(x, y)

        # subtract linear approximation to get residual error
        y1 = x * slope + yint
        self.xvals = x
        self.error = y - y1
        self.errorPlot = pg.plot(x, self.error, title='X axis error (slope = %0.2f um/step)' % (slope*1e6), labels={'left': ('Error', 'm'), 'bottom': ('position', 'steps')})

        # fit residual to combination of sine waves
        def fn(p, x):
            return (p[2] * np.sin((x + p[0]) * 1 * p[1]) + 
                    p[3] * np.sin((x + p[0]) * 2 * p[1]) + 
                    p[4] * np.sin((x + p[0]) * 3 * p[1]) + 
                    p[5] * np.sin((x + p[0]) * 4 * p[1]))

        def erf(p, x, y):
            return fn(p, x) - y

        f0 = 6 * np.pi / x.max()  # guess there are 3 cycles in the data
        amp = self.error.max()
        self.fit = scipy.optimize.leastsq(erf, [0, f0, amp, amp, amp, amp], (x, self.error))[0]
        self.errorPlot.plot(x, fn(self.fit, x), pen='g')

    def closeEvent(self, ev):
        for t in self.targets:
            t.scene().removeItem(t)
