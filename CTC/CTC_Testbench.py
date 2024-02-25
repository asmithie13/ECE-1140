#File that holds the data to run the CTC UI
#Abby Magistro

#pyqt imports
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

class CTC_Testbench(QtWidgets.QMainWindow):
    def __init__(self):
        super(CTC_Testbench, self).__init__()
        #Loading base UI layout from .ui file
        uic.loadUi("CTC/CTC_Testbench.ui", self)

        #Connect Buttons to signals defining behavior
        self.UpdateOccupiedBlocksButton.clicked.connect(self.updateBlocks_button)
        self.UpdateTicketSalesButton.clicked.connect(self.updateTicketSales_button)

        #Changing Button Colors
        self.UpdateOccupiedBlocksButton.setStyleSheet("background-color : rgb(38, 207, 4)") #Green
        self.UpdateTicketSalesButton.setStyleSheet("background-color : rgb(38, 207, 4)")    #Green

        #Setting Combo box values
        lines = ['green', 'red']
        self.LineSelect.addItems(lines)


    #Defines functionality of the update occupied blocks button on the Testbench
    def updateBlocks_button(self):
        BlockText = self.OccupiedBlocksField.text()
        UpdatedBlocks = list(map(str.strip, BlockText.split(',')))

        UpdatedBlocksWithTrain = []
        for i in UpdatedBlocks:
            UpdatedBlocksWithTrain.append(['X', i])

        self.occupiedBlocks.BlockData = UpdatedBlocksWithTrain
        self.OccupiedBlockTable.setModel(BlocksTableModel(self.occupiedBlocks.BlockData))

    #Defines funtionality of the update ticket sales button on the testbench
    def updateTicketSales_button(self):
        SalesText = self.TicketSalesField.text()
        Sales = list(map(str.strip, SalesText.split(',')))
        line = self.LineSelect.currentText()

        
        self.ThroughputGraph.heights = Sales
        

        self.ThroughputGraph.updateThroughputGraph()
        pixmap = QPixmap('CTC/ThroughputGraph.jpeg')
        self.ThroughputGraphLabel.setPixmap(pixmap)



UI_Window = QtWidgets.QApplication(sys.argv)
CTC_tb_widow = CTC_Testbench()
CTC_tb_widow.show()
UI_Window.exec_()