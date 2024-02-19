from PyQt5 import QtWidgets #Import necessary libraries
#from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QPushButton, QLabel, QFileDialog, QLineEdit, QFontDialog
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

#Function to create a label with the given data - Labels created with this function must be static
def constrLabel(window, Xcoord, Ycoord, width, height, font, size, text):
    labelOne = QtWidgets.QLabel(window) #Specify which window the label is in
    labelOne.setGeometry(Xcoord, Ycoord, width, height) #Set the size and placement of the label window
    labelOne.setFont(QFont(font, size)) #Set the font and size of the label
    labelOne.setText(text) #Set the specified text applied to the label

#Function to browse files, select a file, and add file path to lineUpload
def browseFiles(lineUpload, window, labelOrig):
    isCorrect = False #Variable to hold condition - Determines if PLC file is valid
    fileGet = QFileDialog.getOpenFileName(window, "Select PLC File", "C:\\") #Select the file and assign it to a variable
    fileName = fileGet[0] #Get just the file name from the returned argument

    if(PLCvalid(fileName) == True): #If the file is valid:
        labelConfirm = "PLC File Successfully Uploaded" #Confirm that the label is valid
        isCorrect = True #Condition is true since file is valid
        lineUpload.setText(fileName) #Set verification label text
    else:
        lineUpload.setText("") #If the file is not valid, re-set the file path in the line edit
        labelConfirm = "Invalid PLC File Selected" #Set verification label text
    
    labelOrig.setText(labelConfirm) #Set verification label text
    
def PLCvalid(fileName):
    fileOpen = open(fileName, 'r') #Open the file to read the first line - Detect if the PLC file is valid
    headLine = fileOpen.readline() #Read the first line and assign it to a variable
    if(headLine != "PLC File"): #If the header is not as expected, return "False"
        return False
    return True #Otherwise, return "True"

def mainWindow():
    appOne = QApplication(sys.argv) #Initialize application
    winMain = QMainWindow() #Define a main window to be shown
    winMain.setFixedSize(1200, 900) #Set the fixed size of a window/widget
    winMain.setWindowTitle("Track Controller (HW)") #Change the title of the window displayed

    winMain.setStyleSheet("background-color: #d7e3f0")

    labelTitle = constrLabel(winMain, 20, 5, 500, 50, "Segoe UI", 14, "Welcome, PLC Programmer!") #Create a title label using the constrLabel function
    labelUpload = constrLabel(winMain, 20, 70, 300, 50, "Segoe UI", 12, "Upload PLC File:") #Create a label to upload the PLC file using the constrLabel function

    lineUpload = QLineEdit(winMain)
    lineUpload.setGeometry(260, 75, 360, 45) #Implement a line edit for the user to enter the path of the object
    lineUpload.setStyleSheet("background-color: white")
    lineUpload.setReadOnly(True)

    browseButton = QPushButton("Browse", winMain) #Create a push button to browse files
    browseButton.setGeometry(635, 75, 160, 45) #Set the size and orientation of the button to browse files
    browseButton.setFont(QFont("Segoe UI", 8)) #Set the font of the browse button text
    browseButton.setStyleSheet("background-color: white")

    #Create a label to display whether or not the PLC file has been successfully uploaded
    labelConfirm = QtWidgets.QLabel(winMain)
    labelConfirm.setGeometry(810, 70, 500, 50)
    labelConfirm.setFont(QFont("Segoe UI", 10))
    labelConfirm.setText("")

    browseButton.clicked.connect(lambda: browseFiles(lineUpload, winMain, labelConfirm)) #When the button is clicked, a file dialog box is shown to select the PLC file

    winMain.show()
    sys.exit(appOne.exec_())

mainWindow()
