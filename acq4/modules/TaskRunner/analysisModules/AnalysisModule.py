# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from acq4.pyqtgraph.WidgetGroup import WidgetGroup

class AnalysisModule(QtGui.QWidget):
    def __init__(self, taskRunner):
        QtGui.QWidget.__init__(self)
        self.pr = taskRunner
        self.pr.sigNewFrame.connect(self.newFrame)
        self.pr.sigTaskSequenceStarted.connect(self.taskSequenceStarted)
        self.pr.sigTaskStarted.connect(self.taskStarted)
        self.pr.sigTaskFinished.connect(self.taskFinished)

    def postGuiInit(self):
        self.stateGroup = WidgetGroup(self)

    def newFrame(self, *args):
        pass
        #print "NEW FRAME!"
        #print args

    def taskStarted(self, *args):
        pass
        #print "taskStarted!"
        
    def taskFinished(self):
        pass
    
    def taskSequenceStarted(self, *args):
        pass
        #print "taskStarted!"
    
    def saveState(self):
        return self.stateGroup.state()
        
    def restoreState(self, state):
        self.stateGroup.setState(state)
        
    def quit(self):
        try:
            self.pr.sigNewFrame.disconnect(self.newFrame)
        except TypeError:
            pass
        try:
            self.pr.sigTaskSequenceStarted.disconnect(self.taskSequenceStarted)
        except TypeError:
            pass
        try:
            self.pr.sigTaskStarted.disconnect(self.taskStarted)
        except TypeError:
            pass
        try:
            self.pr.sigTaskFinished.disconnect(self.taskFinished)
        except TypeError:
            pass
        
