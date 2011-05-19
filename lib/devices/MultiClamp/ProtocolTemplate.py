# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/devices/MultiClamp/ProtocolTemplate.ui'
#
# Created: Wed May 18 20:44:14 2011
#      by: PyQt4 UI code generator 4.8.3
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
        Form.resize(302, 110)
        Form.setAutoFillBackground(True)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.splitter_2 = QtGui.QSplitter(Form)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame_2 = QtGui.QFrame(self.layoutWidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.icModeRadio = QtGui.QRadioButton(self.frame_2)
        self.icModeRadio.setObjectName(_fromUtf8("icModeRadio"))
        self.horizontalLayout_2.addWidget(self.icModeRadio)
        self.i0ModeRadio = QtGui.QRadioButton(self.frame_2)
        self.i0ModeRadio.setChecked(True)
        self.i0ModeRadio.setObjectName(_fromUtf8("i0ModeRadio"))
        self.horizontalLayout_2.addWidget(self.i0ModeRadio)
        self.vcModeRadio = QtGui.QRadioButton(self.frame_2)
        self.vcModeRadio.setObjectName(_fromUtf8("vcModeRadio"))
        self.horizontalLayout_2.addWidget(self.vcModeRadio)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.holdingCheck = QtGui.QCheckBox(self.frame_2)
        self.holdingCheck.setObjectName(_fromUtf8("holdingCheck"))
        self.horizontalLayout_6.addWidget(self.holdingCheck)
        self.holdingSpin = QtGui.QDoubleSpinBox(self.frame_2)
        self.holdingSpin.setEnabled(False)
        self.holdingSpin.setMinimum(-1000000.0)
        self.holdingSpin.setMaximum(1000000.0)
        self.holdingSpin.setObjectName(_fromUtf8("holdingSpin"))
        self.horizontalLayout_6.addWidget(self.holdingSpin)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.primarySignalCheck = QtGui.QCheckBox(self.layoutWidget)
        self.primarySignalCheck.setObjectName(_fromUtf8("primarySignalCheck"))
        self.gridLayout.addWidget(self.primarySignalCheck, 0, 0, 1, 1)
        self.secondarySignalCheck = QtGui.QCheckBox(self.layoutWidget)
        self.secondarySignalCheck.setObjectName(_fromUtf8("secondarySignalCheck"))
        self.gridLayout.addWidget(self.secondarySignalCheck, 1, 0, 1, 1)
        self.primarySignalCombo = QtGui.QComboBox(self.layoutWidget)
        self.primarySignalCombo.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.primarySignalCombo.sizePolicy().hasHeightForWidth())
        self.primarySignalCombo.setSizePolicy(sizePolicy)
        self.primarySignalCombo.setMinimumSize(QtCore.QSize(40, 0))
        self.primarySignalCombo.setObjectName(_fromUtf8("primarySignalCombo"))
        self.primarySignalCombo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.primarySignalCombo, 0, 1, 1, 1)
        self.secondarySignalCombo = QtGui.QComboBox(self.layoutWidget)
        self.secondarySignalCombo.setEnabled(False)
        self.secondarySignalCombo.setMinimumSize(QtCore.QSize(40, 0))
        self.secondarySignalCombo.setObjectName(_fromUtf8("secondarySignalCombo"))
        self.secondarySignalCombo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.secondarySignalCombo, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 2, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.secondaryGainCheck = QtGui.QCheckBox(self.layoutWidget)
        self.secondaryGainCheck.setObjectName(_fromUtf8("secondaryGainCheck"))
        self.horizontalLayout_7.addWidget(self.secondaryGainCheck)
        self.secondaryGainSpin = QtGui.QSpinBox(self.layoutWidget)
        self.secondaryGainSpin.setEnabled(False)
        self.secondaryGainSpin.setMaximum(100000)
        self.secondaryGainSpin.setObjectName(_fromUtf8("secondaryGainSpin"))
        self.horizontalLayout_7.addWidget(self.secondaryGainSpin)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.primaryGainCheck = QtGui.QCheckBox(self.layoutWidget)
        self.primaryGainCheck.setObjectName(_fromUtf8("primaryGainCheck"))
        self.horizontalLayout_5.addWidget(self.primaryGainCheck)
        self.primaryGainSpin = QtGui.QSpinBox(self.layoutWidget)
        self.primaryGainSpin.setEnabled(False)
        self.primaryGainSpin.setMaximum(100000)
        self.primaryGainSpin.setObjectName(_fromUtf8("primaryGainSpin"))
        self.horizontalLayout_5.addWidget(self.primaryGainSpin)
        self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.frame = QtGui.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.waveGeneratorLabel = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waveGeneratorLabel.sizePolicy().hasHeightForWidth())
        self.waveGeneratorLabel.setSizePolicy(sizePolicy)
        self.waveGeneratorLabel.setObjectName(_fromUtf8("waveGeneratorLabel"))
        self.verticalLayout.addWidget(self.waveGeneratorLabel)
        self.waveGeneratorWidget = StimGenerator(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.waveGeneratorWidget.sizePolicy().hasHeightForWidth())
        self.waveGeneratorWidget.setSizePolicy(sizePolicy)
        self.waveGeneratorWidget.setObjectName(_fromUtf8("waveGeneratorWidget"))
        self.verticalLayout.addWidget(self.waveGeneratorWidget)
        self.verticalLayout_2.addWidget(self.frame)
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.topPlotWidget = PlotWidget(self.splitter)
        self.topPlotWidget.setObjectName(_fromUtf8("topPlotWidget"))
        self.bottomPlotWidget = PlotWidget(self.splitter)
        self.bottomPlotWidget.setObjectName(_fromUtf8("bottomPlotWidget"))
        self.verticalLayout_3.addWidget(self.splitter_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.icModeRadio.setText(QtGui.QApplication.translate("Form", "IC", None, QtGui.QApplication.UnicodeUTF8))
        self.i0ModeRadio.setText(QtGui.QApplication.translate("Form", "I=0", None, QtGui.QApplication.UnicodeUTF8))
        self.vcModeRadio.setText(QtGui.QApplication.translate("Form", "VC", None, QtGui.QApplication.UnicodeUTF8))
        self.holdingCheck.setText(QtGui.QApplication.translate("Form", "Holding (pA)", None, QtGui.QApplication.UnicodeUTF8))
        self.primarySignalCheck.setText(QtGui.QApplication.translate("Form", "Primary:", None, QtGui.QApplication.UnicodeUTF8))
        self.secondarySignalCheck.setText(QtGui.QApplication.translate("Form", "Secondary:", None, QtGui.QApplication.UnicodeUTF8))
        self.primarySignalCombo.setItemText(0, QtGui.QApplication.translate("Form", "MembranePotential", None, QtGui.QApplication.UnicodeUTF8))
        self.secondarySignalCombo.setItemText(0, QtGui.QApplication.translate("Form", "MembraneCurrent", None, QtGui.QApplication.UnicodeUTF8))
        self.secondaryGainCheck.setText(QtGui.QApplication.translate("Form", "Set Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.primaryGainCheck.setText(QtGui.QApplication.translate("Form", "Set Gain", None, QtGui.QApplication.UnicodeUTF8))
        self.waveGeneratorLabel.setText(QtGui.QApplication.translate("Form", "Function (values in pA)", None, QtGui.QApplication.UnicodeUTF8))

from generator.StimGenerator import StimGenerator
from pyqtgraph.PlotWidget import PlotWidget
