# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/modules/Camera/CameraTemplate.ui'
#
# Created: Wed May 18 20:44:21 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(799, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.graphicsWidget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsWidget.sizePolicy().hasHeightForWidth())
        self.graphicsWidget.setSizePolicy(sizePolicy)
        self.graphicsWidget.setObjectName(_fromUtf8("graphicsWidget"))
        self.horizontalLayout_3.addWidget(self.graphicsWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy)
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.DockWidgetVerticalTitleBar)
        self.dockWidget.setObjectName(_fromUtf8("dockWidget"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.vboxlayout.setSpacing(2)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.btnAcquire = QtGui.QPushButton(self.dockWidgetContents)
        self.btnAcquire.setCheckable(True)
        self.btnAcquire.setObjectName(_fromUtf8("btnAcquire"))
        self.hboxlayout.addWidget(self.btnAcquire)
        self.btnRecord = QtGui.QPushButton(self.dockWidgetContents)
        self.btnRecord.setEnabled(True)
        self.btnRecord.setCheckable(True)
        self.btnRecord.setFlat(False)
        self.btnRecord.setObjectName(_fromUtf8("btnRecord"))
        self.hboxlayout.addWidget(self.btnRecord)
        self.btnSnap = QtGui.QToolButton(self.dockWidgetContents)
        self.btnSnap.setEnabled(True)
        self.btnSnap.setObjectName(_fromUtf8("btnSnap"))
        self.hboxlayout.addWidget(self.btnSnap)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.hboxlayout1.addWidget(self.label_2)
        self.binningCombo = QtGui.QComboBox(self.dockWidgetContents)
        self.binningCombo.setObjectName(_fromUtf8("binningCombo"))
        self.hboxlayout1.addWidget(self.binningCombo)
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.hboxlayout1.addWidget(self.label_3)
        self.spinExposure = SpinBox(self.dockWidgetContents)
        self.spinExposure.setMinimumSize(QtCore.QSize(80, 0))
        self.spinExposure.setObjectName(_fromUtf8("spinExposure"))
        self.hboxlayout1.addWidget(self.spinExposure)
        self.btnFullFrame = QtGui.QPushButton(self.dockWidgetContents)
        self.btnFullFrame.setObjectName(_fromUtf8("btnFullFrame"))
        self.hboxlayout1.addWidget(self.btnFullFrame)
        self.scaleToImageBtn = QtGui.QPushButton(self.dockWidgetContents)
        self.scaleToImageBtn.setObjectName(_fromUtf8("scaleToImageBtn"))
        self.hboxlayout1.addWidget(self.scaleToImageBtn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_2.setSizePolicy(sizePolicy)
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.vboxlayout1.setSpacing(0)
        self.vboxlayout1.setMargin(0)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName(_fromUtf8("hboxlayout2"))
        self.histogram = GraphicsView(self.dockWidgetContents_2)
        self.histogram.setFrameShape(QtGui.QFrame.NoFrame)
        self.histogram.setObjectName(_fromUtf8("histogram"))
        self.hboxlayout2.addWidget(self.histogram)
        self.gradientWidget = GradientWidget(self.dockWidgetContents_2)
        self.gradientWidget.setMinimumSize(QtCore.QSize(20, 0))
        self.gradientWidget.setObjectName(_fromUtf8("gradientWidget"))
        self.hboxlayout2.addWidget(self.gradientWidget)
        self.vboxlayout1.addLayout(self.hboxlayout2)
        self.btnAutoGain = QtGui.QPushButton(self.dockWidgetContents_2)
        self.btnAutoGain.setCheckable(True)
        self.btnAutoGain.setChecked(False)
        self.btnAutoGain.setObjectName(_fromUtf8("btnAutoGain"))
        self.vboxlayout1.addWidget(self.btnAutoGain)
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setHorizontalSpacing(6)
        self.gridlayout.setVerticalSpacing(0)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label_6 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridlayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.spinAutoGainSpeed = QtGui.QDoubleSpinBox(self.dockWidgetContents_2)
        self.spinAutoGainSpeed.setProperty(_fromUtf8("value"), 2.0)
        self.spinAutoGainSpeed.setObjectName(_fromUtf8("spinAutoGainSpeed"))
        self.gridlayout.addWidget(self.spinAutoGainSpeed, 0, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridlayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.spinAutoGainCenterWeight = QtGui.QDoubleSpinBox(self.dockWidgetContents_2)
        self.spinAutoGainCenterWeight.setMaximum(1.0)
        self.spinAutoGainCenterWeight.setSingleStep(0.1)
        self.spinAutoGainCenterWeight.setObjectName(_fromUtf8("spinAutoGainCenterWeight"))
        self.gridlayout.addWidget(self.spinAutoGainCenterWeight, 1, 1, 1, 1)
        self.vboxlayout1.addLayout(self.gridlayout)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_2)
        self.dockWidget_4 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_4.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable|QtGui.QDockWidget.DockWidgetVerticalTitleBar)
        self.dockWidget_4.setObjectName(_fromUtf8("dockWidget_4"))
        self.dockWidgetContents_4 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_4.setSizePolicy(sizePolicy)
        self.dockWidgetContents_4.setObjectName(_fromUtf8("dockWidgetContents_4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkEnableROIs = QtGui.QCheckBox(self.dockWidgetContents_4)
        self.checkEnableROIs.setObjectName(_fromUtf8("checkEnableROIs"))
        self.gridLayout.addWidget(self.checkEnableROIs, 0, 0, 1, 2)
        self.label_7 = QtGui.QLabel(self.dockWidgetContents_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.spinROITime = QtGui.QDoubleSpinBox(self.dockWidgetContents_4)
        self.spinROITime.setSingleStep(0.1)
        self.spinROITime.setProperty(_fromUtf8("value"), 5.0)
        self.spinROITime.setObjectName(_fromUtf8("spinROITime"))
        self.gridLayout.addWidget(self.spinROITime, 4, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(88, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 5, 0, 1, 2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.btnClearROIs = QtGui.QToolButton(self.dockWidgetContents_4)
        self.btnClearROIs.setObjectName(_fromUtf8("btnClearROIs"))
        self.gridLayout.addWidget(self.btnClearROIs, 2, 1, 1, 1)
        self.btnAddROI = QtGui.QToolButton(self.dockWidgetContents_4)
        self.btnAddROI.setObjectName(_fromUtf8("btnAddROI"))
        self.gridLayout.addWidget(self.btnAddROI, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.plotWidget = PlotWidget(self.dockWidgetContents_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setObjectName(_fromUtf8("plotWidget"))
        self.horizontalLayout.addWidget(self.plotWidget)
        self.dockWidget_4.setWidget(self.dockWidgetContents_4)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_4)
        self.dockWidget_5 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_5.setFloating(False)
        self.dockWidget_5.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockWidget_5.setObjectName(_fromUtf8("dockWidget_5"))
        self.dockWidgetContents_5 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_5.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_5.setSizePolicy(sizePolicy)
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.dockWidgetContents_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.addFrameBtn = QtGui.QToolButton(self.dockWidgetContents_5)
        self.addFrameBtn.setObjectName(_fromUtf8("addFrameBtn"))
        self.horizontalLayout_2.addWidget(self.addFrameBtn)
        self.clearFramesBtn = QtGui.QToolButton(self.dockWidgetContents_5)
        self.clearFramesBtn.setObjectName(_fromUtf8("clearFramesBtn"))
        self.horizontalLayout_2.addWidget(self.clearFramesBtn)
        self.dockWidget_5.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_5)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setFloating(False)
        self.dockWidget_3.setObjectName(_fromUtf8("dockWidget_3"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_3.setSizePolicy(sizePolicy)
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.dockWidgetContents_3)
        self.vboxlayout2.setSpacing(2)
        self.vboxlayout2.setMargin(0)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.btnDivideBackground = QtGui.QToolButton(self.dockWidgetContents_3)
        self.btnDivideBackground.setCheckable(True)
        self.btnDivideBackground.setObjectName(_fromUtf8("btnDivideBackground"))
        self.vboxlayout2.addWidget(self.btnDivideBackground)
        self.btnLockBackground = QtGui.QToolButton(self.dockWidgetContents_3)
        self.btnLockBackground.setCheckable(True)
        self.btnLockBackground.setObjectName(_fromUtf8("btnLockBackground"))
        self.vboxlayout2.addWidget(self.btnLockBackground)
        self.frame_2 = QtGui.QFrame(self.dockWidgetContents_3)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.hboxlayout3 = QtGui.QHBoxLayout(self.frame_2)
        self.hboxlayout3.setSpacing(0)
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setObjectName(_fromUtf8("hboxlayout3"))
        self.label_4 = QtGui.QLabel(self.frame_2)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.hboxlayout3.addWidget(self.label_4)
        self.spinFilterTime = QtGui.QDoubleSpinBox(self.frame_2)
        self.spinFilterTime.setSingleStep(1.0)
        self.spinFilterTime.setProperty(_fromUtf8("value"), 5.0)
        self.spinFilterTime.setObjectName(_fromUtf8("spinFilterTime"))
        self.hboxlayout3.addWidget(self.spinFilterTime)
        self.vboxlayout2.addWidget(self.frame_2)
        self.frame_3 = QtGui.QFrame(self.dockWidgetContents_3)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.hboxlayout4 = QtGui.QHBoxLayout(self.frame_3)
        self.hboxlayout4.setSpacing(2)
        self.hboxlayout4.setMargin(0)
        self.hboxlayout4.setObjectName(_fromUtf8("hboxlayout4"))
        self.label_5 = QtGui.QLabel(self.frame_3)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.hboxlayout4.addWidget(self.label_5)
        self.spinFlattenSize = QtGui.QDoubleSpinBox(self.frame_3)
        self.spinFlattenSize.setProperty(_fromUtf8("value"), 0.0)
        self.spinFlattenSize.setObjectName(_fromUtf8("spinFlattenSize"))
        self.hboxlayout4.addWidget(self.spinFlattenSize)
        self.vboxlayout2.addWidget(self.frame_3)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem3)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAcquire.setToolTip(QtGui.QApplication.translate("MainWindow", "Start/stop camera acquisition.\n"
"In general, this can just stay on always.", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAcquire.setText(QtGui.QApplication.translate("MainWindow", "Acquire", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRecord.setToolTip(QtGui.QApplication.translate("MainWindow", "Start/stop recording frames as they are acquired. \n"
"Frames are written to the current storage directory set in \n"
"the data manager window.", None, QtGui.QApplication.UnicodeUTF8))
        self.btnRecord.setText(QtGui.QApplication.translate("MainWindow", "Record", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSnap.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Save a single frame to disk.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\">Frames are written to the current storage directory set in </p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\">the data manager window.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSnap.setText(QtGui.QApplication.translate("MainWindow", "Snap", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Binning", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.spinExposure.setToolTip(QtGui.QApplication.translate("MainWindow", "Sets the exposure time for each frame.", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFullFrame.setToolTip(QtGui.QApplication.translate("MainWindow", "Set the region of interest to the maximum possible area.", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFullFrame.setText(QtGui.QApplication.translate("MainWindow", "Full Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleToImageBtn.setToolTip(QtGui.QApplication.translate("MainWindow", "Scales the view such that camera pixels match screen pixels exactly. This can increase the rate frames are displayed (does not affect the acquisition rate, though).", None, QtGui.QApplication.UnicodeUTF8))
        self.scaleToImageBtn.setText(QtGui.QApplication.translate("MainWindow", "Scale 1:1", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_2.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Display Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAutoGain.setToolTip(QtGui.QApplication.translate("MainWindow", "Determines the behavior of the white/black level sliders.\n"
"When enabled, the sliders maximum and minimum values are set\n"
"to the maximum and minimum intensity values in the image.\n"
"When disabled, the minimum is 0 and the maximum is the largest \n"
"possible intensity given the bit depth of the camera.", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAutoGain.setText(QtGui.QApplication.translate("MainWindow", "Auto Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Slow", None, QtGui.QApplication.UnicodeUTF8))
        self.spinAutoGainSpeed.setToolTip(QtGui.QApplication.translate("MainWindow", "Smooths out the auto gain control, prevents very\n"
"brief flashes from affecting the gain. Larger values\n"
"indicate more smoothing.\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Center Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.spinAutoGainCenterWeight.setToolTip(QtGui.QApplication.translate("MainWindow", "Weights the auto gain measurement to the center 1/3 of\n"
"the frame when set to 1.0. A value of 0.0 meters from \n"
"the entire frame.", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_4.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Plots", None, QtGui.QApplication.UnicodeUTF8))
        self.checkEnableROIs.setText(QtGui.QApplication.translate("MainWindow", "Enable ROIs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Time:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnClearROIs.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAddROI.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_5.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Persistent Frames", None, QtGui.QApplication.UnicodeUTF8))
        self.addFrameBtn.setText(QtGui.QApplication.translate("MainWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.clearFramesBtn.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidget_3.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Background Subtraction", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDivideBackground.setToolTip(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enable/disable background division. Accumulates a running</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">average of several previous frames and divides this from the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">current visible frame. Does <span style=\" font-style:italic;\">not</span> affect images written to disk.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDivideBackground.setText(QtGui.QApplication.translate("MainWindow", "Divide Background", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLockBackground.setToolTip(QtGui.QApplication.translate("MainWindow", "Locks the background frame so that it no longer integrates new frames into itself.", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLockBackground.setText(QtGui.QApplication.translate("MainWindow", "Lock Background", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Time const.", None, QtGui.QApplication.UnicodeUTF8))
        self.spinFilterTime.setToolTip(QtGui.QApplication.translate("MainWindow", "Sets the approximate number of frames to be averaged for\n"
"background division.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Blur Bg.", None, QtGui.QApplication.UnicodeUTF8))
        self.spinFlattenSize.setToolTip(QtGui.QApplication.translate("MainWindow", "Blurs the background frame before dividing it from the current frame.", None, QtGui.QApplication.UnicodeUTF8))

from SpinBox import SpinBox
from pyqtgraph.GradientWidget import GradientWidget
from pyqtgraph.GraphicsView import GraphicsView
from pyqtgraph.PlotWidget import PlotWidget
