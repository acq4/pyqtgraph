# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'devTemplate.ui'
#
# Created: Thu Oct 20 13:03:02 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(579, 388)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.powerGroup = QtGui.QGroupBox(Form)
        self.powerGroup.setTitle(_fromUtf8(""))
        self.powerGroup.setObjectName(_fromUtf8("powerGroup"))
        self.gridLayout_4 = QtGui.QGridLayout(self.powerGroup)
        self.gridLayout_4.setMargin(6)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_5 = QtGui.QLabel(self.powerGroup)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_4.addWidget(self.label_5, 0, 2, 1, 1)
        self.expectedPowerSpin = SpinBox(self.powerGroup)
        self.expectedPowerSpin.setMinimumSize(QtCore.QSize(75, 0))
        self.expectedPowerSpin.setObjectName(_fromUtf8("expectedPowerSpin"))
        self.gridLayout_4.addWidget(self.expectedPowerSpin, 0, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.powerGroup)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 1, 2, 1, 1)
        self.toleranceSpin = SpinBox(self.powerGroup)
        self.toleranceSpin.setMinimumSize(QtCore.QSize(75, 0))
        self.toleranceSpin.setObjectName(_fromUtf8("toleranceSpin"))
        self.gridLayout_4.addWidget(self.toleranceSpin, 1, 3, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.powerGroup)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.currentPowerRadio = QtGui.QRadioButton(self.groupBox_3)
        self.currentPowerRadio.setObjectName(_fromUtf8("currentPowerRadio"))
        self.verticalLayout.addWidget(self.currentPowerRadio)
        self.expectedPowerRadio = QtGui.QRadioButton(self.groupBox_3)
        self.expectedPowerRadio.setChecked(True)
        self.expectedPowerRadio.setObjectName(_fromUtf8("expectedPowerRadio"))
        self.verticalLayout.addWidget(self.expectedPowerRadio)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 4, 2, 1)
        self.label_4 = QtGui.QLabel(self.powerGroup)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.outputPowerLabel = QtGui.QLabel(self.powerGroup)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.outputPowerLabel.setFont(font)
        self.outputPowerLabel.setText(_fromUtf8(""))
        self.outputPowerLabel.setObjectName(_fromUtf8("outputPowerLabel"))
        self.gridLayout_4.addWidget(self.outputPowerLabel, 0, 1, 1, 1)
        self.samplePowerLabel = QtGui.QLabel(self.powerGroup)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(50)
        font.setBold(False)
        self.samplePowerLabel.setFont(font)
        self.samplePowerLabel.setText(_fromUtf8(""))
        self.samplePowerLabel.setObjectName(_fromUtf8("samplePowerLabel"))
        self.gridLayout_4.addWidget(self.samplePowerLabel, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.powerGroup)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.powerGroup, 0, 0, 1, 1)
        self.wavelengthGroup = QtGui.QGroupBox(Form)
        self.wavelengthGroup.setTitle(_fromUtf8(""))
        self.wavelengthGroup.setObjectName(_fromUtf8("wavelengthGroup"))
        self.gridLayout_5 = QtGui.QGridLayout(self.wavelengthGroup)
        self.gridLayout_5.setMargin(6)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_7 = QtGui.QLabel(self.wavelengthGroup)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.wavelengthSpin = SpinBox(self.wavelengthGroup)
        self.wavelengthSpin.setSuffix(_fromUtf8(""))
        self.wavelengthSpin.setObjectName(_fromUtf8("wavelengthSpin"))
        self.gridLayout_5.addWidget(self.wavelengthSpin, 0, 1, 1, 1)
        self.wavelengthCombo = QtGui.QComboBox(self.wavelengthGroup)
        self.wavelengthCombo.setObjectName(_fromUtf8("wavelengthCombo"))
        self.wavelengthCombo.addItem(_fromUtf8(""))
        self.gridLayout_5.addWidget(self.wavelengthCombo, 0, 2, 1, 1)
        self.gridLayout.addWidget(self.wavelengthGroup, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setMargin(6)
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setVerticalSpacing(4)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.calibrationList = QtGui.QTreeWidget(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setWeight(50)
        font.setBold(False)
        self.calibrationList.setFont(font)
        self.calibrationList.setRootIsDecorated(False)
        self.calibrationList.setItemsExpandable(False)
        self.calibrationList.setObjectName(_fromUtf8("calibrationList"))
        self.calibrationList.header().setStretchLastSection(True)
        self.gridLayout_6.addWidget(self.calibrationList, 0, 0, 1, 4)
        self.calibrateBtn = QtGui.QPushButton(self.groupBox_2)
        self.calibrateBtn.setObjectName(_fromUtf8("calibrateBtn"))
        self.gridLayout_6.addWidget(self.calibrateBtn, 1, 0, 1, 1)
        self.deleteBtn = QtGui.QPushButton(self.groupBox_2)
        self.deleteBtn.setObjectName(_fromUtf8("deleteBtn"))
        self.gridLayout_6.addWidget(self.deleteBtn, 1, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setMargin(6)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.microscopeCombo = QtGui.QComboBox(self.groupBox)
        self.microscopeCombo.setObjectName(_fromUtf8("microscopeCombo"))
        self.gridLayout_2.addWidget(self.microscopeCombo, 1, 1, 1, 1)
        self.scanLabel = QtGui.QLabel(self.groupBox)
        self.scanLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.scanLabel.setObjectName(_fromUtf8("scanLabel"))
        self.gridLayout_2.addWidget(self.scanLabel, 1, 3, 1, 1)
        self.measurementSpin = SpinBox(self.groupBox)
        self.measurementSpin.setMinimum(0.0)
        self.measurementSpin.setMaximum(100.0)
        self.measurementSpin.setProperty(_fromUtf8("value"), 1.0)
        self.measurementSpin.setObjectName(_fromUtf8("measurementSpin"))
        self.gridLayout_2.addWidget(self.measurementSpin, 1, 4, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.meterCombo = QtGui.QComboBox(self.groupBox)
        self.meterCombo.setObjectName(_fromUtf8("meterCombo"))
        self.gridLayout_2.addWidget(self.meterCombo, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 3, 1, 1)
        self.settlingSpin = SpinBox(self.groupBox)
        self.settlingSpin.setObjectName(_fromUtf8("settlingSpin"))
        self.gridLayout_2.addWidget(self.settlingSpin, 2, 4, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.pCellGroup = QtGui.QGroupBox(self.groupBox)
        self.pCellGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.pCellGroup.setObjectName(_fromUtf8("pCellGroup"))
        self.gridLayout_8 = QtGui.QGridLayout(self.pCellGroup)
        self.gridLayout_8.setMargin(6)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.gridLayout_7 = QtGui.QGridLayout()
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_9 = QtGui.QLabel(self.pCellGroup)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        self.minVSpin = SpinBox(self.pCellGroup)
        self.minVSpin.setMinimum(-99.0)
        self.minVSpin.setSingleStep(0.01)
        self.minVSpin.setProperty(_fromUtf8("value"), -0.2)
        self.minVSpin.setObjectName(_fromUtf8("minVSpin"))
        self.gridLayout_7.addWidget(self.minVSpin, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.pCellGroup)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_7.addWidget(self.label_11, 0, 2, 1, 1)
        self.stepsSpin = SpinBox(self.pCellGroup)
        self.stepsSpin.setDecimals(0)
        self.stepsSpin.setMinimum(10.0)
        self.stepsSpin.setMaximum(1000.0)
        self.stepsSpin.setProperty(_fromUtf8("value"), 20.0)
        self.stepsSpin.setObjectName(_fromUtf8("stepsSpin"))
        self.gridLayout_7.addWidget(self.stepsSpin, 0, 3, 1, 1)
        self.label_10 = QtGui.QLabel(self.pCellGroup)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_7.addWidget(self.label_10, 2, 0, 1, 1)
        self.maxVSpin = SpinBox(self.pCellGroup)
        self.maxVSpin.setSingleStep(0.01)
        self.maxVSpin.setProperty(_fromUtf8("value"), 1.2)
        self.maxVSpin.setObjectName(_fromUtf8("maxVSpin"))
        self.gridLayout_7.addWidget(self.maxVSpin, 2, 1, 1, 1)
        self.recalibratePCellCheck = QtGui.QCheckBox(self.pCellGroup)
        self.recalibratePCellCheck.setObjectName(_fromUtf8("recalibratePCellCheck"))
        self.gridLayout_7.addWidget(self.recalibratePCellCheck, 2, 3, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.pCellGroup, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 2, 0, 1, 4)
        self.qSwitchBtn = QtGui.QPushButton(self.groupBox_2)
        self.qSwitchBtn.setCheckable(True)
        self.qSwitchBtn.setObjectName(_fromUtf8("qSwitchBtn"))
        self.gridLayout_6.addWidget(self.qSwitchBtn, 1, 3, 1, 1)
        self.shutterBtn = QtGui.QPushButton(self.groupBox_2)
        self.shutterBtn.setCheckable(True)
        self.shutterBtn.setObjectName(_fromUtf8("shutterBtn"))
        self.gridLayout_6.addWidget(self.shutterBtn, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Expected Output Power:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Tolerance:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "For energy calculations use:", None, QtGui.QApplication.UnicodeUTF8))
        self.currentPowerRadio.setText(QtGui.QApplication.translate("Form", "Current Power", None, QtGui.QApplication.UnicodeUTF8))
        self.expectedPowerRadio.setText(QtGui.QApplication.translate("Form", "Expected Power", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Current Output Power:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Power at sample (calc.):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Current Wavelength: ", None, QtGui.QApplication.UnicodeUTF8))
        self.wavelengthCombo.setItemText(0, QtGui.QApplication.translate("Form", "Set wavelength for:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Power Calibration", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrationList.headerItem().setText(0, QtGui.QApplication.translate("Form", "Microscope", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrationList.headerItem().setText(1, QtGui.QApplication.translate("Form", "Objective", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrationList.headerItem().setText(2, QtGui.QApplication.translate("Form", "Wavelength", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrationList.headerItem().setText(3, QtGui.QApplication.translate("Form", "Transmission", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrationList.headerItem().setText(4, QtGui.QApplication.translate("Form", "Power at Sample", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrationList.headerItem().setText(5, QtGui.QApplication.translate("Form", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrateBtn.setText(QtGui.QApplication.translate("Form", "Calibrate", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBtn.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Calibration Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Microscope:", None, QtGui.QApplication.UnicodeUTF8))
        self.scanLabel.setText(QtGui.QApplication.translate("Form", "Measurement Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.measurementSpin.setSuffix(QtGui.QApplication.translate("Form", " s", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Power Meter:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Settling Duration:", None, QtGui.QApplication.UnicodeUTF8))
        self.settlingSpin.setToolTip(QtGui.QApplication.translate("Form", "Specify the time it takes for the selected power meter to settle on a value.", None, QtGui.QApplication.UnicodeUTF8))
        self.pCellGroup.setTitle(QtGui.QApplication.translate("Form", "Pockel Cell Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Minimum Voltage:", None, QtGui.QApplication.UnicodeUTF8))
        self.minVSpin.setSuffix(QtGui.QApplication.translate("Form", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("Form", "Number of Steps: ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Form", "Maximum Voltage:", None, QtGui.QApplication.UnicodeUTF8))
        self.maxVSpin.setSuffix(QtGui.QApplication.translate("Form", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.recalibratePCellCheck.setText(QtGui.QApplication.translate("Form", "Re-Calibrate Pockel Cell", None, QtGui.QApplication.UnicodeUTF8))
        self.qSwitchBtn.setText(QtGui.QApplication.translate("Form", "Turn On QSwitch", None, QtGui.QApplication.UnicodeUTF8))
        self.shutterBtn.setText(QtGui.QApplication.translate("Form", "Open Shutter", None, QtGui.QApplication.UnicodeUTF8))

from SpinBox import SpinBox
