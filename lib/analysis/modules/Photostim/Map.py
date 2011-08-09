# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from advancedTypes import OrderedDict
import pyqtgraph as pg
import numpy as np
import ProgressDialog

class Map:
    ### A map is a group of (possibly overlapping) scans and associated meta-data. 
    ### Maps will automatically merge overlapping spots and join non-overlapping scans to create a single scan
    mapFields = OrderedDict([
        ('cell', 'int'),
        ('scans', 'blob'),
        #('date', 'int'),
        #('name', 'text'),
        ('description', 'text'),
        ('cellType', 'text'),
        ('mode', 'text'),
        ('holding', 'real'),
        ('internal', 'text'),
        ('acsf', 'text'),
        ('drug', 'text'),
        ('temp', 'real'),
    ])
        
    def __init__(self, host, rec=None):
        self.host = host     ## host is the parent Photostim object
        self.stubs = []      ## list of ScanStub objects for scans in the map that have not been loaded yet
        self.scans = []      ## list of loaded Scan objects
        self.scanItems = {}  ## maps {scan: tree item}
        self.points = []         ## Holds all data: [ (position, [(scan, dh), ...], spotData), ... ]
        self.pointsByFile = {}   ## just a lookup dictionary
        self.spots = []          ## used to construct scatterplotitem
        self.sPlotItem = pg.ScatterPlotItem(pxMode=False)
        
        self.header = self.mapFields.keys()[2:]
        
        self.item = QtGui.QTreeWidgetItem([""] * len(self.header))
        self.item.setFlags(QtCore.Qt.ItemIsSelectable| QtCore.Qt.ItemIsEditable| QtCore.Qt.ItemIsEnabled)
        self.item.map = self
        self.item.setExpanded(True)
        self.rowID = None
        
        ## If a DB record was supplied, that means this map already exists in the DB so
        ## we can reload the list of scans already included in the map
        if rec is not None:
            self.rowID = rec['rowid']
            scans = rec['scans']
            #del rec['scans']
            #del rec['cell']
            for i in range(len(self.header)):
                self.item.setText(i, str(rec[self.header[i]]))
            for fh,rowid in scans:
                item = QtGui.QTreeWidgetItem([fh.shortName()])
                #print "Create scan stub:", fh
                self.stubs.append(ScanStub(fh, item, rowid))  ## rowid can be either a (table, rowid) pair or an integer implying ('ProtocolSequence', rowid)
                item.handle = fh
                self.item.addChild(item)

    def name(self, cell=None):
        rec = self.getRecord()
        if cell is None:
            cell = rec['cell']
        if cell is None:
            return ""
        name = cell.shortName()
        if rec['holding'] < -.04:
            name = name + "_excitatory"
        elif rec['holding'] >= -.01:
            name = name + "_inhibitory"
        return name

    def rebuildPlot(self):
        ## decide on point locations, build scatterplot
        self.points = []         ## Holds all data: [ (position, [(scan, dh), ...], spotData), ... ]
        self.pointsByFile = {}   ## just a lookup dictionary
        self.spots = []               ## used to construct scatterplotitem
        for scan in self.scans:  ## iterate over all points in all scans
            #if isinstance(scan, tuple):
                #continue    ## need to load before building
            self.addScanSpots(scan)
        self.sPlotItem.setPoints(self.spots)

    def addScanSpots(self, scan):
        for pt in scan.spots():
            pos = pt.scenePos()
            size = pt.size  #sceneBoundingRect().width()
            added = False
            fh = self.host.dataModel.getClampFile(pt.data)
            for pt2 in self.points:     ## check all previously added points for position match
                pos2 = pt2[0]
                dp = pos2-pos
                dist = (dp.x()**2 + dp.y()**2)**0.5
                if dist < size/3.:      ## if position matches, add scan/spot data into existing site
                    pt2[1].append((scan, pt.data))
                    pt2[2]['data'].append((scan, fh))
                    added = True
                    self.pointsByFile[pt.data] = pt2
                    break
            if not added:               ## ..otherwise, add a new site
                self.spots.append({'pos': pos, 'size': size, 'data': [(scan, fh)]})
                self.points.append((pos, [(scan, fh)], self.spots[-1]))
                self.pointsByFile[pt.data] = self.points[-1]

    def addScans(self, scanList):
        #print "Map.addScans:", scanList
        for scan in scanList:
            if scan in self.scans:
                continue
                #raise Exception("Scan already present in this map.")
            
            if len(self.scans) == 0:
                ## auto-populate fields
                rec = self.generateDefaults(scan)
                for i in range(2, len(self.mapFields)):
                    ind = i-2
                    key = self.mapFields.keys()[i]
                    if key in rec and str(self.item.text(ind)) == '':
                        self.item.setText(ind, str(rec[key]))

            if scan is None:
                raise Exception("Tried to add None as scan")
            self.scans.append(scan)
            item = QtGui.QTreeWidgetItem([scan.name()])
            item.scan = scan
            self.item.addChild(item)
            self.item.setExpanded(True)
            
            self.scanItems[scan] = item

    def generateDefaults(self, scan):
        rec = {}
        source = scan.source()
        sinfo = source.info()
        if 'sequenceParams' in sinfo:
            next = source[source.ls()[0]]
        else:
            next = source
        
        if next.exists('Clamp1.ma'):
            cname = 'Clamp1'
            file = next['Clamp1.ma']
        elif next.exists('Clamp2.ma'):
            cname = 'Clamp2'
            file = next['Clamp2.ma']
            
        data = file.read()
        info = data._info[-1]
        if 'ClampState' in info:
            rec['mode'] = info['ClampState']['mode']
            rec['holding'] = info['ClampState']['holding']
        else:  ## older meta-info format for MultiClamp
            rec['mode'] = info['mode']
            try:
                rec['holding'] = float(sinfo['devices'][cname]['holdingSpin'])*1000.
            except:
                pass
        
        cell = source.parent()
        day = cell.parent().parent()
        dinfo = day.info()
        rec['acsf'] = dinfo.get('solution', '')
        rec['internal'] = dinfo.get('internal', '')
        rec['temp'] = dinfo.get('temperature', '')
        
        rec['cellType'] = cell.info().get('type', '')
        
        ninfo = next.info()
        if 'Temperature.BathTemp' in ninfo:
            rec['temp'] = ninfo['Temperature.BathTemp']
        rec['description'] = self.name(source.parent())
        return rec


    def removeScan(self, scan):
        self.scans.remove(scan)
        item = self.scanItems[scan]
        self.item.removeChild(item)
        
    def getRecord(self):
        ### Create a dictionary with all the record data for this map. 
        rec = {}
        i = 0
        for k in self.mapFields:
            if k == 'scans':  ## list of row IDs of the scans included in this map
                rowids = []
                for s in self.stubs:
                    rowids.append(s.rowId)
                for s in self.scans:
                    rowids.append(s.rowId())
                rec['scans'] = rowids
            elif k == 'cell':   ## decide which cell this map belongs to. 
                if len(self.scans) == 0 and len(self.stubs) == 0:
                    rec['cell'] = None
                else:
                    if len(self.scans) > 0:
                        rec['cell'] = self.scans[0].source().parent()
                    else:
                        rec['cell'] = self.stubs[0].dirHandle.parent()
                        
                    #if isinstance(s, tuple):
                        #rec[k] = s[0].parent()
                    #else:
                        #rec[k] = self.scans[0].source.parent()
            else:
                rec[k] = str(self.item.text(i))
                if self.mapFields[k] == 'real':
                    try:
                        num = rec[k].replace('C', '')  ## convert to numerical value (by stripping units)
                        rec[k] = float(num)
                    except:
                        pass
                i += 1
        return rec
        
    def isVisible(self):
        return self.sPlotItem.isVisible()
            
    def recolor(self, n, nMax):
        if not self.sPlotItem.isVisible():
            return
        spots = self.sPlotItem.points()
        colors = []
        with ProgressDialog.ProgressDialog("Computing map %s (%d/%d)" % (self.name(), n, nMax), 0, len(spots)) as dlg:
            for i in xrange(len(spots)):
                s = spots[i]
                data = []
                sources = s.data
                for scan, dh in sources:
                    data.append(scan.getStats(dh))
                
                if len(data) == 0:
                    continue
                if len(data) == 1:
                    mergeData = data[0]
                else:
                    mergeData = {}
                    for k in data[0]:
                        vals = [d[k] for d in data if k in d]
                        try:
                            if len(data) == 2:
                                mergeData[k] = np.mean(vals)
                            elif len(data) > 2:
                                mergeData[k] = np.median(vals)
                            elif len(data) == 1:
                                mergeData[k] = vals[0]
                            else:
                                mergeData[k] = 0
                        except:
                            mergeData[k] = vals[0]
                #print mergeData
                color = self.host.getColor(mergeData)
                #s.setBrush(color)  ## wait until after to set the colors
                colors.append((s, color))
                dlg.setValue(i)
                if dlg.wasCanceled():
                    raise Exception("Process canceled by user.")
                
        for s, c in colors:
            s.setBrush(c)


    def loadStubs(self):
        ### Turn all stubs into fully-loaded scans.
        with ProgressDialog.ProgressDialog("Loading scans...", 0, len(self.stubs)) as dlg:
            for stub in self.stubs:
                QtGui.QApplication.processEvents()
                ### can we load a partial map if one scan fails? (should we?)
                newScans = self.host.loadScan(stub.dirHandle)
                if len(newScans) > 1:
                    ## For sequence scans, we somehow need to decide how to reload the exact set of spots that were chosen for this scan before..
                    raise Exception("Haven't implemented reloading sequence scans yet")
                elif len(newScans) == 1:
                    newScan = newScans[0]
                else:
                    raise Exception("Photostim.loadScan returned empty list for file '%s'" % str(stub.dirHandle))
                    
                stub.treeItem.scan = newScan
                self.scans.append(newScan)
                self.scanItems[newScan] = stub.treeItem
                dlg += 1
                if dlg.wasCanceled():
                    raise Exception("Map load canceled by user.")
        self.stubs = []
            
        ## decide on point set, generate scatter plot 
        self.rebuildPlot()


class ScanStub:
    def __init__(self, dirHandle, treeItem, rowId):
        self.dirHandle = dirHandle ## ProtocolSequence directory handle for this scan (or group of scans?)
        self.treeItem = treeItem   ## treeItem for this scan in the map tree
        self.rowId = rowId         ## DB row ID for this scan (in which table?)
        
        