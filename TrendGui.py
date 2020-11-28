from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QTableWidget, QWidget
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QPushButton
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

        self.createButtonWidget()
        self.createTableWidget()

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
