# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './acq4/modules/Camera/CameraTemplate.ui'
#
# Created: Mon Dec 23 22:46:59 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1051, 877)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.graphicsView = GraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.horizontalLayout_3.addWidget(self.graphicsView)
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
        self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btnAcquire = QtGui.QPushButton(self.dockWidgetContents)
        self.btnAcquire.setCheckable(True)
        self.btnAcquire.setObjectName(_fromUtf8("btnAcquire"))
        self.horizontalLayout_5.addWidget(self.btnAcquire)
        self.btnSnap = FeedbackButton(self.dockWidgetContents)
        self.btnSnap.setObjectName(_fromUtf8("btnSnap"))
        self.horizontalLayout_5.addWidget(self.btnSnap)
        self.btnRecord = QtGui.QPushButton(self.dockWidgetContents)
        self.btnRecord.setEnabled(True)
        self.btnRecord.setCheckable(True)
        self.btnRecord.setFlat(False)
        self.btnRecord.setObjectName(_fromUtf8("btnRecord"))
        self.horizontalLayout_5.addWidget(self.btnRecord)
        self.recordXframesCheck = QtGui.QCheckBox(self.dockWidgetContents)
        self.recordXframesCheck.setObjectName(_fromUtf8("recordXframesCheck"))
        self.horizontalLayout_5.addWidget(self.recordXframesCheck)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.recordXframesSpin = QtGui.QSpinBox(self.dockWidgetContents)
        self.recordXframesSpin.setEnabled(True)
        self.recordXframesSpin.setMinimum(1)
        self.recordXframesSpin.setMaximum(1000000)
        self.recordXframesSpin.setProperty("value", 100)
        self.recordXframesSpin.setObjectName(_fromUtf8("recordXframesSpin"))
        self.horizontalLayout_4.addWidget(self.recordXframesSpin)
        self.framesLabel = QtGui.QLabel(self.dockWidgetContents)
        self.framesLabel.setEnabled(True)
        self.framesLabel.setObjectName(_fromUtf8("framesLabel"))
        self.horizontalLayout_4.addWidget(self.framesLabel)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.hboxlayout.addWidget(self.label_2)
        self.binningCombo = QtGui.QComboBox(self.dockWidgetContents)
        self.binningCombo.setObjectName(_fromUtf8("binningCombo"))
        self.hboxlayout.addWidget(self.binningCombo)
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.hboxlayout.addWidget(self.label_3)
        self.spinExposure = SpinBox(self.dockWidgetContents)
        self.spinExposure.setMinimumSize(QtCore.QSize(80, 0))
        self.spinExposure.setObjectName(_fromUtf8("spinExposure"))
        self.hboxlayout.addWidget(self.spinExposure)
        self.btnFullFrame = QtGui.QPushButton(self.dockWidgetContents)
        self.btnFullFrame.setObjectName(_fromUtf8("btnFullFrame"))
        self.hboxlayout.addWidget(self.btnFullFrame)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.hboxlayout, 1, 0, 1, 1)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_2.setSizePolicy(sizePolicy)
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.vboxlayout = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.vboxlayout.setSpacing(0)
        self.vboxlayout.setMargin(0)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.histogram = HistogramLUTWidget(self.dockWidgetContents_2)
        self.histogram.setObjectName(_fromUtf8("histogram"))
        self.hboxlayout1.addWidget(self.histogram)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.btnAutoGain = QtGui.QPushButton(self.dockWidgetContents_2)
        self.btnAutoGain.setCheckable(True)
        self.btnAutoGain.setChecked(False)
        self.btnAutoGain.setObjectName(_fromUtf8("btnAutoGain"))
        self.vboxlayout.addWidget(self.btnAutoGain)
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setHorizontalSpacing(6)
        self.gridlayout.setVerticalSpacing(0)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label_6 = QtGui.QLabel(self.dockWidgetContents_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridlayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.spinAutoGainSpeed = QtGui.QDoubleSpinBox(self.dockWidgetContents_2)
        self.spinAutoGainSpeed.setProperty("value", 2.0)
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
        self.vboxlayout.addLayout(self.gridlayout)
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
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.spinROITime = QtGui.QDoubleSpinBox(self.dockWidgetContents_4)
        self.spinROITime.setSingleStep(0.1)
        self.spinROITime.setProperty("value", 5.0)
        self.spinROITime.setObjectName(_fromUtf8("spinROITime"))
        self.gridLayout.addWidget(self.spinROITime, 5, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(88, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 2)
        self.btnAddROI = QtGui.QPushButton(self.dockWidgetContents_4)
        self.btnAddROI.setObjectName(_fromUtf8("btnAddROI"))
        self.gridLayout.addWidget(self.btnAddROI, 1, 0, 1, 1)
        self.btnClearROIs = QtGui.QPushButton(self.dockWidgetContents_4)
        self.btnClearROIs.setObjectName(_fromUtf8("btnClearROIs"))
        self.gridLayout.addWidget(self.btnClearROIs, 1, 1, 1, 1)
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
        self.dockWidget_5.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
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
        self.addFrameBtn = FeedbackButton(self.dockWidgetContents_5)
        self.addFrameBtn.setObjectName(_fromUtf8("addFrameBtn"))
        self.horizontalLayout_2.addWidget(self.addFrameBtn)
        self.clearFramesBtn = QtGui.QPushButton(self.dockWidgetContents_5)
        self.clearFramesBtn.setObjectName(_fromUtf8("clearFramesBtn"))
        self.horizontalLayout_2.addWidget(self.clearFramesBtn)
        self.dockWidget_5.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_5)
        self.dockWidget_3 = QtGui.QDockWidget(MainWindow)
        self.dockWidget_3.setFloating(False)
        self.dockWidget_3.setFeatures(QtGui.QDockWidget.DockWidgetFloatable|QtGui.QDockWidget.DockWidgetMovable)
        self.dockWidget_3.setObjectName(_fromUtf8("dockWidget_3"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_3.setSizePolicy(sizePolicy)
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_4 = QtGui.QLabel(self.dockWidgetContents_3)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 6, 1, 1, 1)
        self.contAvgBgCheck = QtGui.QCheckBox(self.dockWidgetContents_3)
        self.contAvgBgCheck.setObjectName(_fromUtf8("contAvgBgCheck"))
        self.gridLayout_3.addWidget(self.contAvgBgCheck, 2, 0, 1, 4)
        self.bgTimeSpin = QtGui.QDoubleSpinBox(self.dockWidgetContents_3)
        self.bgTimeSpin.setDecimals(1)
        self.bgTimeSpin.setSingleStep(1.0)
        self.bgTimeSpin.setProperty("value", 3.0)
        self.bgTimeSpin.setObjectName(_fromUtf8("bgTimeSpin"))
        self.gridLayout_3.addWidget(self.bgTimeSpin, 1, 2, 1, 2)
        self.collectBgBtn = QtGui.QPushButton(self.dockWidgetContents_3)
        self.collectBgBtn.setCheckable(True)
        self.collectBgBtn.setObjectName(_fromUtf8("collectBgBtn"))
        self.gridLayout_3.addWidget(self.collectBgBtn, 0, 0, 1, 4)
        self.divideBgBtn = QtGui.QPushButton(self.dockWidgetContents_3)
        self.divideBgBtn.setCheckable(True)
        self.divideBgBtn.setAutoExclusive(False)
        self.divideBgBtn.setObjectName(_fromUtf8("divideBgBtn"))
        self.gridLayout_3.addWidget(self.divideBgBtn, 5, 0, 1, 4)
        self.label_5 = QtGui.QLabel(self.dockWidgetContents_3)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 3, 0, 1, 1)
        self.bgBlurSpin = QtGui.QDoubleSpinBox(self.dockWidgetContents_3)
        self.bgBlurSpin.setProperty("value", 0.0)
        self.bgBlurSpin.setObjectName(_fromUtf8("bgBlurSpin"))
        self.gridLayout_3.addWidget(self.bgBlurSpin, 3, 2, 1, 2)
        self.subtractBgBtn = QtGui.QPushButton(self.dockWidgetContents_3)
        self.subtractBgBtn.setCheckable(True)
        self.subtractBgBtn.setAutoExclusive(False)
        self.subtractBgBtn.setObjectName(_fromUtf8("subtractBgBtn"))
        self.gridLayout_3.addWidget(self.subtractBgBtn, 4, 0, 1, 4)
        self.dockWidget_3.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_3)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Camera", None))
        self.dockWidget.setWindowTitle(_translate("MainWindow", "Camera", None))
        self.btnAcquire.setToolTip(_translate("MainWindow", "Start/stop camera acquisition.\n"
"In general, this can just stay on always.", None))
        self.btnAcquire.setText(_translate("MainWindow", "Acquire", None))
        self.btnSnap.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Record a single frame. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Image is written to the current storage directory set in </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">the data manager window.</span></p></body></html>", None))
        self.btnSnap.setText(_translate("MainWindow", "Snap", None))
        self.btnRecord.setToolTip(_translate("MainWindow", "Start/stop recording frames as they are acquired. \n"
"Frames are written to the current storage directory set in \n"
"the data manager window.", None))
        self.btnRecord.setText(_translate("MainWindow", "Record", None))
        self.recordXframesCheck.setText(_translate("MainWindow", "Stop recording after", None))
        self.framesLabel.setText(_translate("MainWindow", "frames.", None))
        self.label_2.setText(_translate("MainWindow", "Binning", None))
        self.label_3.setText(_translate("MainWindow", "Exposure", None))
        self.spinExposure.setToolTip(_translate("MainWindow", "Sets the exposure time for each frame.", None))
        self.btnFullFrame.setToolTip(_translate("MainWindow", "Set the region of interest to the maximum possible area.", None))
        self.btnFullFrame.setText(_translate("MainWindow", "Full Frame", None))
        self.dockWidget_2.setWindowTitle(_translate("MainWindow", "Display Gain", None))
        self.btnAutoGain.setToolTip(_translate("MainWindow", "Determines the behavior of the white/black level sliders.\n"
"When enabled, the sliders maximum and minimum values are set\n"
"to the maximum and minimum intensity values in the image.\n"
"When disabled, the minimum is 0 and the maximum is the largest \n"
"possible intensity given the bit depth of the camera.", None))
        self.btnAutoGain.setText(_translate("MainWindow", "Auto Gain", None))
        self.label_6.setText(_translate("MainWindow", "Slow", None))
        self.spinAutoGainSpeed.setToolTip(_translate("MainWindow", "Smooths out the auto gain control, prevents very\n"
"brief flashes from affecting the gain. Larger values\n"
"indicate more smoothing.\n"
"", None))
        self.label_8.setText(_translate("MainWindow", "Center Weight", None))
        self.spinAutoGainCenterWeight.setToolTip(_translate("MainWindow", "Weights the auto gain measurement to the center 1/3 of\n"
"the frame when set to 1.0. A value of 0.0 meters from \n"
"the entire frame.", None))
        self.dockWidget_4.setWindowTitle(_translate("MainWindow", "Plots", None))
        self.checkEnableROIs.setToolTip(_translate("MainWindow", "Enables online calculation/plotting for ROIs.\n"
"ROIs can be still be used as position markers \n"
"if this box is unchecked.", None))
        self.checkEnableROIs.setText(_translate("MainWindow", "Enable ROIs", None))
        self.label_7.setText(_translate("MainWindow", "Time:", None))
        self.spinROITime.setToolTip(_translate("MainWindow", "Sets the amount of time that ROI data is displayed in the plot.", None))
        self.btnAddROI.setToolTip(_translate("MainWindow", "Adds an ROI to the canvas.", None))
        self.btnAddROI.setText(_translate("MainWindow", "Add", None))
        self.btnClearROIs.setToolTip(_translate("MainWindow", "Clears all ROIs from the canvas.", None))
        self.btnClearROIs.setText(_translate("MainWindow", "Clear", None))
        self.dockWidget_5.setWindowTitle(_translate("MainWindow", "Persistent Frames", None))
        self.addFrameBtn.setToolTip(_translate("MainWindow", "Adds the current camera image to the canvas.\n"
"", None))
        self.addFrameBtn.setText(_translate("MainWindow", "Add", None))
        self.clearFramesBtn.setToolTip(_translate("MainWindow", "Clears all images from the canvas.", None))
        self.clearFramesBtn.setText(_translate("MainWindow", "Clear", None))
        self.dockWidget_3.setWindowTitle(_translate("MainWindow", "Background Subtraction", None))
        self.label_4.setText(_translate("MainWindow", "Average", None))
        self.contAvgBgCheck.setText(_translate("MainWindow", "Continuous Average", None))
        self.bgTimeSpin.setToolTip(_translate("MainWindow", "Sets the approximate number of frames to be averaged for\n"
"background division.", None))
        self.bgTimeSpin.setSuffix(_translate("MainWindow", " s", None))
        self.collectBgBtn.setText(_translate("MainWindow", "Collect Background", None))
        self.divideBgBtn.setToolTip(_translate("MainWindow", "Enables background division. \n"
"Either a set of static background frames need to have already by collected\n"
"(by pressing \'Static\' above) or \'Continuous\' needs to be pressed.", None))
        self.divideBgBtn.setText(_translate("MainWindow", "Divide Background", None))
        self.label_5.setText(_translate("MainWindow", "Blur Background.", None))
        self.bgBlurSpin.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Blurs the background frame before dividing it from the current frame.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Large blur values may cause performance to degrade.</span></p></body></html>", None))
        self.subtractBgBtn.setText(_translate("MainWindow", "Subtract Background", None))

from acq4.pyqtgraph.widgets.PlotWidget import PlotWidget
from acq4.pyqtgraph import HistogramLUTWidget, SpinBox, FeedbackButton
from acq4.pyqtgraph.widgets.GraphicsView import GraphicsView
