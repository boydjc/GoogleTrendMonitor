from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QTableWidgetItem
from TrendScrape import TrendScraper
import time

class TrendCtrl():

    def __init__(self, gui):
        # give the class an insatance of the gui so that it can
        # do things with it
        self.gui = gui

        self.connectButtonSignals()

        # create a dictionary for storing the results
        # the purpose of this dictionary is to track how many times the
        # result has been in the #1 spot
        self.domDict = {}

        

    def display(self):
        self.gui.show()

    def connectButtonSignals(self):
        self.gui.startButton.clicked.connect(self.startTrendThread)
        self.gui.stopButton.clicked.connect(self.stopTrendThread)

    def connectThreadSignals(self):
        self.trendThread.updateTableSig.connect(self.processThreadData)

    def checkInDict(self, item):

        if item in self.domDict:
            return True
        else:
            return False

    def processThreadData(self, data):

        # if the topic is not in the dictionary then add it
        entryCount = 0
        for entry in data:
            if not(self.checkInDict(entry[0])):
                self.domDict.update({entry[0]:[entry[1], 0]})
            else:
                self.domDict.update({entry[0]:[entry[1], self.domDict[entry[0]][1]]})
                # don't let the dominance count exceed 100
                if(entryCount == 0 and self.domDict[entry[0]][1] <= 100):
                    # incrememnt the dominance of the first entry since it will be in the highest spot
                    self.domDict[entry[0]][1] += 1
                else:
                    if(self.domDict[entry[0]][1] > 0):
                        # subtract from the entrys dominance if it loses the top spot
                        self.domDict[entry[0]][1] -= 1

            entryCount += 1
        
        
        # first row
        if not(data[0][0] == ""):
            self.gui.trendTable.setItem(0, 0, QTableWidgetItem(data[0][0]))
            self.gui.trendTable.setItem(0, 1, QTableWidgetItem(self.domDict[data[0][0]][0]))
            self.gui.trendTable.setItem(0, 2, QTableWidgetItem(str(self.domDict[data[0][0]][1])))
            
        # second row
        if not(data[1][0] == ""):
            self.gui.trendTable.setItem(1, 0, QTableWidgetItem(data[1][0]))
            self.gui.trendTable.setItem(1, 1, QTableWidgetItem(self.domDict[data[1][0]][0]))
            self.gui.trendTable.setItem(1, 2, QTableWidgetItem(str(self.domDict[data[1][0]][1])))
        # third row
        if not(data[2][0] == ""):
            self.gui.trendTable.setItem(2, 0, QTableWidgetItem(data[2][0]))
            self.gui.trendTable.setItem(2, 1, QTableWidgetItem(self.domDict[data[2][0]][0]))
            self.gui.trendTable.setItem(2, 2, QTableWidgetItem(str(self.domDict[data[2][0]][1])))
            
        # fourth row
        if not(data[3][0] == ""):
            self.gui.trendTable.setItem(3, 0, QTableWidgetItem(data[3][0]))
            self.gui.trendTable.setItem(3, 1, QTableWidgetItem(self.domDict[data[3][0]][0]))
            self.gui.trendTable.setItem(3, 2, QTableWidgetItem(str(self.domDict[data[3][0]][1])))
            
        # fifth row
        if not(data[4][0] == ""):
            self.gui.trendTable.setItem(4, 0, QTableWidgetItem(data[4][0]))
            self.gui.trendTable.setItem(4, 1, QTableWidgetItem(self.domDict[data[4][0]][0]))
            self.gui.trendTable.setItem(4, 2, QTableWidgetItem(str(self.domDict[data[4][0]][1])))
            
        # sixth row
        if not(data[5][0] == ""):
            self.gui.trendTable.setItem(5, 0, QTableWidgetItem(data[5][0]))
            self.gui.trendTable.setItem(5, 1, QTableWidgetItem(self.domDict[data[5][0]][0]))
            self.gui.trendTable.setItem(5, 2, QTableWidgetItem(str(self.domDict[data[5][0]][1])))
            
        # Seventh row
        if not(data[6][0] == ""):
            self.gui.trendTable.setItem(6, 0, QTableWidgetItem(data[6][0]))
            self.gui.trendTable.setItem(6, 1, QTableWidgetItem(self.domDict[data[6][0]][0]))
            self.gui.trendTable.setItem(6, 2, QTableWidgetItem(str(self.domDict[data[6][0]][1])))
            
        # Eighth row
        if not(data[7][0] == ""):
            self.gui.trendTable.setItem(7, 0, QTableWidgetItem(data[7][0]))
            self.gui.trendTable.setItem(7, 1, QTableWidgetItem(self.domDict[data[7][0]][0]))
            self.gui.trendTable.setItem(7, 2, QTableWidgetItem(str(self.domDict[data[7][0]][1])))
            
        # Nineth row
        if not(data[8][0] == ""):
            self.gui.trendTable.setItem(8, 0, QTableWidgetItem(data[8][0]))
            self.gui.trendTable.setItem(8, 1, QTableWidgetItem(self.domDict[data[8][0]][0]))
            self.gui.trendTable.setItem(8, 2, QTableWidgetItem(str(self.domDict[data[8][0]][1])))
            
        # Tenth row
        if not(data[9][0] == ""):
            self.gui.trendTable.setItem(9, 0, QTableWidgetItem(data[9][0]))
            self.gui.trendTable.setItem(9, 1, QTableWidgetItem(self.domDict[data[9][0]][0]))
            self.gui.trendTable.setItem(9, 2, QTableWidgetItem(str(self.domDict[data[9][0]][1])))
    
    def startTrendThread(self):
        print("Starting thread")

        # get the currently selected target
        selectedTarget = self.gui.targetBox.currentText()
        self.trendThread = TrendThread(selectedTarget)
        self.connectThreadSignals()
        self.trendThread.threadRunning = True
        self.trendThread.start()

    def stopTrendThread(self):
        print("Stopping thread")
        self.trendThread.threadRunning = False
        self.trendThread.quit()

""" Thread that handles getting all of the trend data"""
class TrendThread(QThread):

    updateTableSig = pyqtSignal(list)
    
    
    def __init__(self, target):
        QThread.__init__(self)

        print("Starting Web Driver")
        self.trender = TrendScraper(target)

        self.threadRunning = False
        
    def run(self):
        while(self.threadRunning):
            self.updateTableSig.emit(self.trender.getRelatedData())
            self.trender.refreshPage()
            time.sleep(5)
