from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QTableWidget, QWidget
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton, QComboBox
import sys
import TrendScrape
from TrendController import TrendCtrl

class TrendGui(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setWindowTitle('TrendGui')
        self.setFixedSize(510, 440)

        # gui has one main widget with a QGridLayout()
        self.generalLayout = QVBoxLayout()
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.generalLayout)

        self.createTargetList()
        self.createButtonWidget()
        self.createTableWidget()

    def createTargetList(self):
        self.targetWidget = QWidget()
        self.targetLayout = QHBoxLayout()
        self.targetWidget.setLayout(self.targetLayout)

        self.targetBox = QComboBox()

        targetList = ['San francisco-Oakland-San Jose',
                      'New York NY',
                      'Dallas-FT. Worth TX',
                      'Chicago IL']
        self.targetBox.addItems(targetList)

        self.targetLayout.addWidget(self.targetBox)
        self.generalLayout.addWidget(self.targetWidget)

    """ Creates a table using QLabels"""    
    def createTableWidget(self):
        self.tableWidget = QWidget()
        self.tableWidget.setFixedSize(492, 343)
        self.tableLayout = QVBoxLayout()
        self.tableWidget.setLayout(self.tableLayout)        

        # create table
        self.trendTable = QTableWidget(10, 3)
        self.trendTable.setColumnWidth(0, 300)
        self.trendTable.setColumnWidth(1, 75)
        self.trendTable.setColumnWidth(2, 75)

        # create header for the table

        self.trendTable.setHorizontalHeaderLabels("Topic;Increase;Dominance".split(";"))
        
        self.tableLayout.addWidget(self.trendTable)
        self.generalLayout.addWidget(self.tableWidget)

    """ Contains the start and stop buttons for the scanner """
    def createButtonWidget(self):
        self.buttonWidget = QWidget()
        self.buttonLayout = QHBoxLayout()
        self.buttonWidget.setLayout(self.buttonLayout)

        self.startButton = QPushButton("Start")
        self.stopButton = QPushButton("Stop")
        self.quitButton = QPushButton("Quit")

        self.buttonLayout.addWidget(self.startButton)
        self.buttonLayout.addWidget(self.stopButton)

        self.generalLayout.addWidget(self.buttonWidget)
        


def main():
    """Main function"""
    trendProgram = QApplication([])
    trendGui = TrendGui()
    trendCtrl = TrendCtrl(trendGui)
    trendCtrl.display()

    #executre Trend Program Application
    sys.exit(trendProgram.exec())
    
if __name__ == '__main__':

    main()
