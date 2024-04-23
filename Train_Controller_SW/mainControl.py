# -*- coding: utf-8 -*-
from math import ceil

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1146, 857)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("alternate-background-color: rgb(255, 143, 148);")
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.BrkAcelBox = QtWidgets.QGroupBox(self.centralwidget)
        self.BrkAcelBox.setMinimumSize(QtCore.QSize(525, 0))
        self.BrkAcelBox.setStyleSheet("background-color: rgb(233, 247, 255);")
        self.BrkAcelBox.setTitle("")
        self.BrkAcelBox.setObjectName("BrkAcelBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.BrkAcelBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.BrkAcelBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)


        ### BRAKE OUTPUT
        self.lcdBrk = QtWidgets.QLCDNumber(self.BrkAcelBox)
        self.lcdBrk.setDigitCount(3)
        self.lcdBrk.setObjectName("lcdBrk")
        self.verticalLayout_2.addWidget(self.lcdBrk)
        ### BRAKE INPUT
        self.vertSliderBrk = QtWidgets.QSlider(self.BrkAcelBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.vertSliderBrk.sizePolicy().hasHeightForWidth())
        self.vertSliderBrk.setSizePolicy(sizePolicy)
        self.vertSliderBrk.setMaximumSize(QtCore.QSize(16777215, 200))
        self.vertSliderBrk.setOrientation(QtCore.Qt.Vertical)
        self.vertSliderBrk.setObjectName("vertSliderBrk")
        self.vertSliderBrk.setMaximum(1)
        self.verticalLayout_2.addWidget(self.vertSliderBrk)

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.BrkAcelBox)
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("selection-color: rgb(255, 14, 30);")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")

        #### ACCELERATION PERCENT OUT
        self.lcdAcel = QtWidgets.QLCDNumber(self.groupBox_2)
        self.lcdAcel.setObjectName("lcdAcel")
        self.verticalLayout.addWidget(self.lcdAcel)
        self.lcdAcel.setDigitCount(12)
        self.label_20 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)

        ## POWER FAILURE INDICATOR
        self.PwrFail = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.PwrFail.setFont(font)
        self.PwrFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.PwrFail.setAlignment(QtCore.Qt.AlignCenter)
        self.PwrFail.setObjectName("PwrFail")
        self.verticalLayout.addWidget(self.PwrFail)

        ####BRAKE FAILURE INDICATION
        self.BrkFail = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.BrkFail.setFont(font)
        self.BrkFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.BrkFail.setAlignment(QtCore.Qt.AlignCenter)
        self.BrkFail.setObjectName("BrkFail")
        self.verticalLayout.addWidget(self.BrkFail)

        ###SIGNAL FAILURE INDICATOR
        self.SigFail = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.SigFail.setFont(font)
        self.SigFail.setStyleSheet("color: rgb(225, 225, 225);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.SigFail.setAlignment(QtCore.Qt.AlignCenter)
        self.SigFail.setObjectName("SigFail")
        self.verticalLayout.addWidget(self.SigFail)

        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.BrkAcelBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)

        ### POWER OUTPUT DISPLAY
        self.lcdPowOut = QtWidgets.QLCDNumber(self.BrkAcelBox)
        self.lcdPowOut.setMaximumSize(QtCore.QSize(16777215, 400))
        self.lcdPowOut.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdPowOut.setSmallDecimalPoint(False)
        self.lcdPowOut.setDigitCount(3)
        self.lcdPowOut.setObjectName("lcdPowOut")
        self.verticalLayout_3.addWidget(self.lcdPowOut)

        ### ACELLERATE INPUT
        self.vertSliderPow = QtWidgets.QSlider(self.BrkAcelBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.vertSliderPow.sizePolicy().hasHeightForWidth())
        self.vertSliderPow.setSizePolicy(sizePolicy)
        self.vertSliderPow.setMaximumSize(QtCore.QSize(16777215, 200))
        self.vertSliderPow.setOrientation(QtCore.Qt.Vertical)
        self.vertSliderPow.setObjectName("vertSliderPow")
        self.vertSliderPow.setMaximum(100)
        self.verticalLayout_3.addWidget(self.vertSliderPow)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.horizontalLayout_8.addLayout(self.horizontalLayout)
        self.gridLayout_2.addWidget(self.BrkAcelBox, 1, 1, 2, 2)

        ### TRAIN SELECTION

        self.Train_Select_Box = QtWidgets.QGroupBox(self.centralwidget)
        self.Train_Select_Box.setMaximumSize(QtCore.QSize(400, 16777215))
        self.Train_Select_Box.setStyleSheet("background-color: rgb(233, 247, 255);")
        self.Train_Select_Box.setTitle("")
        self.Train_Select_Box.setObjectName("Train_Select_Box")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.Train_Select_Box)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.undergrnd_ind = QtWidgets.QLabel(self.Train_Select_Box)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.undergrnd_ind.setFont(font)
        self.undergrnd_ind.setAlignment(QtCore.Qt.AlignCenter)
        self.undergrnd_ind.setObjectName("undergrnd_ind")
        self.verticalLayout_6.addWidget(self.undergrnd_ind)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem)
        self.undergrnd_ind.setStyleSheet("color: rgb(225, 225, 225);\n"
                                      "background-color: rgb(255, 255, 255);")
    

        #self.trainSel = QtWidgets.QComboBox(self.Train_Select_Box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        #sizePolicy.setHeightForWidth(self.trainSel.sizePolicy().hasHeightForWidth())
        #self.trainSel.setSizePolicy(sizePolicy)
        #self.trainSel.setMaximumSize(QtCore.QSize(500, 45))
        #self.trainSel.setStyleSheet("background-color: rgb(255, 255, 255);")
        #self.trainSel.setIconSize(QtCore.QSize(4, 4))
        #self.trainSel.setObjectName("trainSel")
        #self.trainSel.addItem("")
        #self.trainSel.addItem("")
        #self.trainSel.addItem("")
        
        #self.verticalLayout_6.addWidget(self.trainSel)
        self.gridLayout_2.addWidget(self.Train_Select_Box, 1, 0, 1, 1)


        ####EBRAKE
        self.Ebrake = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.Ebrake.setFont(font)
        self.Ebrake.setAutoFillBackground(False)
        self.Ebrake.setStyleSheet("background-color: rgb(255, 55, 62);\n"
                                  "selection-background-color: rgb(255, 52, 53);\n"
                                  "selection-color: rgb(255, 159, 154);")
        self.Ebrake.setCheckable(True)
        self.Ebrake.setChecked(False)
        self.Ebrake.setDefault(False)
        self.Ebrake.setFlat(False)
        self.Ebrake.setObjectName("Ebrake")
        self.gridLayout_2.addWidget(self.Ebrake, 6, 0, 1, 4)

        self.CabinConditionsBox = QtWidgets.QGroupBox(self.centralwidget)
        self.CabinConditionsBox.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.CabinConditionsBox.setFont(font)
        self.CabinConditionsBox.setStyleSheet("background-color: rgb(233, 247, 255);")
        self.CabinConditionsBox.setAlignment(QtCore.Qt.AlignCenter)
        self.CabinConditionsBox.setObjectName("CabinConditionsBox")
        self.gridLayout = QtWidgets.QGridLayout(self.CabinConditionsBox)
        self.gridLayout.setObjectName("gridLayout")

        ## RIGHT DOOR TRIGGER
        self.buttonDoorR = QtWidgets.QPushButton(self.CabinConditionsBox)
        self.buttonDoorR.setCheckable(True)
        self.buttonDoorR.setObjectName("buttonDoorR")
        self.gridLayout.addWidget(self.buttonDoorR, 2, 3, 1, 2)
        self.label_13 = QtWidgets.QLabel(self.CabinConditionsBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)


        self.IntLights = QtWidgets.QLabel(self.CabinConditionsBox)
        self.IntLights.setObjectName("IntLights")
        self.gridLayout.addWidget(self.IntLights, 1, 0, 1, 1)

        ### TEMEPERATURE INPUT

        self.temp = QtWidgets.QSpinBox(self.CabinConditionsBox)
        self.temp.setProperty("minimum", 60)
        self.temp.setProperty("maximum", 90)
        self.temp.setObjectName("temp")
        self.gridLayout.addWidget(self.temp, 3, 1, 1, 1)

        ### TEMPERATURE OUTPUT
        self.lcdCurTemp = QtWidgets.QLCDNumber(self.CabinConditionsBox)
        self.lcdCurTemp.setObjectName("lcdCurTemp")
        self.lcdCurTemp.display(self.temp.value())
        self.lcdCurTemp.setDigitCount(2)
        self.lcdCurTemp.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdCurTemp.setSmallDecimalPoint(False)
        self.lcdCurTemp.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.gridLayout.addWidget(self.lcdCurTemp, 3, 2, 1, 3)

        ### HEADLIGHT CONTROLL
        self.buttonHDon = QtWidgets.QPushButton(self.CabinConditionsBox)
        self.buttonHDon.setCheckable(True)
        self.buttonHDon.setChecked(False)
        self.buttonHDon.setAutoDefault(False)
        self.buttonHDon.setObjectName("buttonHDon")
        self.gridLayout.addWidget(self.buttonHDon, 0, 1, 1, 2)

        ### LEFT DOORS CONTROLL
        self.buttonDoorL = QtWidgets.QPushButton(self.CabinConditionsBox)
        self.buttonDoorL.setCheckable(True)
        self.buttonDoorL.setObjectName("buttonDoorL")
        self.gridLayout.addWidget(self.buttonDoorL, 2, 1, 1, 2)
        self.buttonHDoff = QtWidgets.QPushButton(self.CabinConditionsBox)
        self.buttonHDoff.setCheckable(True)
        self.buttonHDoff.setChecked(True)
        self.buttonHDoff.setObjectName("buttonHDoff")
        self.gridLayout.addWidget(self.buttonHDoff, 0, 3, 1, 2)
        self.label = QtWidgets.QLabel(self.CabinConditionsBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.CabinConditionsBox)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 0, 1, 1)

        ### INTERIOR LIGHTS INPUT
        self.IntLightSld = QtWidgets.QSlider(self.CabinConditionsBox)
        self.IntLightSld.setMaximum(2)
        self.IntLightSld.setSingleStep(1)
        self.IntLightSld.setPageStep(2)
        self.IntLightSld.setSliderPosition(0)
        self.IntLightSld.setTracking(False)
        self.IntLightSld.setOrientation(QtCore.Qt.Horizontal)
        self.IntLightSld.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.IntLightSld.setTickInterval(1)
        self.IntLightSld.setObjectName("IntLightSld")
        self.gridLayout.addWidget(self.IntLightSld, 1, 1, 1, 4)
        self.gridLayout_2.addWidget(self.CabinConditionsBox, 0, 3, 1, 1)

        ##########SPEAKER SECTION~##################
        self.SpeakerOutputBox = QtWidgets.QGroupBox(self.centralwidget)
        self.SpeakerOutputBox.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SpeakerOutputBox.setFont(font)
        self.SpeakerOutputBox.setStyleSheet("background-color: rgb(233, 247, 255);")
        self.SpeakerOutputBox.setTitle("")
        self.SpeakerOutputBox.setAlignment(QtCore.Qt.AlignCenter)
        self.SpeakerOutputBox.setObjectName("SpeakerOutputBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.SpeakerOutputBox)
        self.gridLayout_4.setObjectName("gridLayout_4")

        ### ANNOUNCEMENT INPUT
        self.Announcement = QtWidgets.QLabel(self.SpeakerOutputBox)
        self.Announcement.setObjectName("Announcement")
        self.gridLayout_4.addWidget(self.Announcement, 2, 0, 1, 1)
        self.lineEditAnn = QtWidgets.QLineEdit(self.SpeakerOutputBox)
        self.lineEditAnn.setText("")
        self.lineEditAnn.setObjectName("lineEditAnn")
        self.gridLayout_4.addWidget(self.lineEditAnn, 2, 1, 1, 1)


        self.CurrentOutput = QtWidgets.QLabel(self.SpeakerOutputBox)
        self.CurrentOutput.setObjectName("CurrentOutput")
        self.gridLayout_4.addWidget(self.CurrentOutput, 3, 0, 1, 1)

        ### CURRENT STATION OUTPUT
        self.CurrentStation = QtWidgets.QLabel(self.SpeakerOutputBox)
        self.CurrentStation.setObjectName("CurrentStation")
        self.gridLayout_4.addWidget(self.CurrentStation, 1, 0, 1, 1)

        ###CURRENT SPEAKER OUTPUT
        self.SpeakerOuputs = QtWidgets.QLabel(self.SpeakerOutputBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.SpeakerOuputs.setFont(font)
        self.SpeakerOuputs.setAlignment(QtCore.Qt.AlignCenter)
        self.SpeakerOuputs.setObjectName("SpeakerOuputs")
        self.gridLayout_4.addWidget(self.SpeakerOuputs, 0, 0, 1, 2)
        self.CurStatOut = QtWidgets.QLabel(self.SpeakerOutputBox)
        self.CurStatOut.setAlignment(QtCore.Qt.AlignCenter)
        self.CurStatOut.setObjectName("CurStatOut")
        self.gridLayout_4.addWidget(self.CurStatOut, 1, 1, 1, 1)
        self.SpkrOut = QtWidgets.QLabel(self.SpeakerOutputBox)
        self.SpkrOut.setText("")
        self.SpkrOut.setObjectName("SpkrOut")
        self.gridLayout_4.addWidget(self.SpkrOut, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.SpeakerOutputBox, 1, 3, 1, 1)
        self.groupBox_9 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_9.setStyleSheet("background-color: rgb(233, 247, 255);")
        self.groupBox_9.setTitle("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.DistanceTillStop = QtWidgets.QLabel(self.groupBox_9)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.DistanceTillStop.setFont(font)
        self.DistanceTillStop.setAlignment(QtCore.Qt.AlignCenter)
        self.DistanceTillStop.setObjectName("DistanceTillStop")
        self.verticalLayout_4.addWidget(self.DistanceTillStop)

       #AUTHOIRTY OUTPUT
        self.lcdAuth = QtWidgets.QLCDNumber(self.groupBox_9)
        self.lcdAuth.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdAuth.setObjectName("lcdAuth")
        self.lcdAuth.setDigitCount(5)
        self.verticalLayout_4.addWidget(self.lcdAuth)
        self.gridLayout_2.addWidget(self.groupBox_9, 2, 3, 1, 1)
        self.Mode_Box = QtWidgets.QGroupBox(self.centralwidget)
        self.Mode_Box.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Mode_Box.setFont(font)
        self.Mode_Box.setStyleSheet("background-color: rgb(233, 247, 255);")
        self.Mode_Box.setAlignment(QtCore.Qt.AlignCenter)
        self.Mode_Box.setObjectName("Mode_Box")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Mode_Box)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        ## MANUAL MODE BUTTON
        self.buttonMan = QtWidgets.QPushButton(self.Mode_Box)
        self.buttonMan.setCheckable(True)
        self.buttonMan.setChecked(True)
        self.buttonMan.setObjectName("buttonMan")
        self.horizontalLayout_2.addWidget(self.buttonMan)
        ## AUTOMATIC MODE BUTTON
        self.buttonAuto = QtWidgets.QPushButton(self.Mode_Box)
        self.buttonAuto.setCheckable(True)
        self.buttonAuto.setChecked(False)
        self.buttonAuto.setObjectName("buttonAuto")
        self.horizontalLayout_2.addWidget(self.buttonAuto)
        self.gridLayout_2.addWidget(self.Mode_Box, 0, 0, 1, 1)
        self.groupBox_8 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_8.setStyleSheet("background-color: rgb(233, 247, 255);")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Speed_Limit = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Speed_Limit.setFont(font)
        self.Speed_Limit.setAlignment(QtCore.Qt.AlignCenter)
        self.Speed_Limit.setObjectName("Speed_Limit")
        self.horizontalLayout_5.addWidget(self.Speed_Limit)
        self.Commanded_Speed = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Commanded_Speed.setFont(font)
        self.Commanded_Speed.setAlignment(QtCore.Qt.AlignCenter)
        self.Commanded_Speed.setObjectName("Commanded_Speed")
        self.horizontalLayout_5.addWidget(self.Commanded_Speed)
        self.Current_Speed = QtWidgets.QLabel(self.groupBox_8)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Current_Speed.setFont(font)
        self.Current_Speed.setAlignment(QtCore.Qt.AlignCenter)
        self.Current_Speed.setObjectName("Current_Speed")
        self.horizontalLayout_5.addWidget(self.Current_Speed)
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lcdSpdLim = QtWidgets.QLCDNumber(self.groupBox_8)
        self.lcdSpdLim.setDigitCount(3)
        self.lcdSpdLim.setObjectName("lcdSpdLim")
        self.horizontalLayout_6.addWidget(self.lcdSpdLim)
        self.lcdCmdSpd = QtWidgets.QLCDNumber(self.groupBox_8)
        self.lcdCmdSpd.setDigitCount(3)
        self.lcdCmdSpd.setObjectName("lcdCmdSpd")
        self.horizontalLayout_6.addWidget(self.lcdCmdSpd)
        self.lcdCurSpd = QtWidgets.QLCDNumber(self.groupBox_8)
        self.lcdCurSpd.setDigitCount(5)
        self.lcdCurSpd.setObjectName("lcdCurSpd")
        self.horizontalLayout_6.addWidget(self.lcdCurSpd)
        self.gridLayout_5.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_8, 4, 0, 1, 4)

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(20)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("background-color: rgb(229, 255, 204);")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lcdKi = QtWidgets.QLCDNumber(self.groupBox_3)
        self.lcdKi.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdKi.setSmallDecimalPoint(True)
        self.lcdKi.setDigitCount(6)
        self.lcdKi.setObjectName("lcdKi")
        self.lcdKi.display(8000)
        self.gridLayout_3.addWidget(self.lcdKi, 0, 0, 1, 1)
        self.lcdKp = QtWidgets.QLCDNumber(self.groupBox_3)
        self.lcdKp.setSmallDecimalPoint(True)
        self.lcdKp.setDigitCount(6)
        self.lcdKp.setObjectName("lcdKp")
        self.lcdKp.display(10)
        self.gridLayout_3.addWidget(self.lcdKp, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.inputKp = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.inputKp.setObjectName("inputKp")
        self.inputKp.setMaximum(999999)
        self.horizontalLayout_4.addWidget(self.inputKp)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.inputKi = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.inputKi.setObjectName("inputKi")
        self.inputKi.setMaximum(999999)
        # NOTE THESE VALUES ARE FLIPPED
        self.inputKi.setValue(8000)
        self.inputKp.setValue(2)
        self.horizontalLayout_3.addWidget(self.inputKi)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 0, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.vertSliderPow.setDisabled(True)
        self.vertSliderBrk.setValue(1)
        




        self.retranslateUi(MainWindow)
        """
        self.buttonMan.clicked['bool'].connect(self.TrainController)  # type: ignore
        self.buttonAuto.clicked['bool'].connect(self.set_auto)  # type: ignore
        self.inputKi.valueChanged['double'].connect(self.lcdKi.display()) # type: ignore
        self.inputKp.valueChanged['double'].connect(self.lcdKp.display()) # type: ignore
        self.buttonHDon.clicked['bool'].connect(self.buttonHDoff.toggle)  # type: ignore
        self.buttonHDoff.clicked['bool'].connect(self.buttonHDon.toggle)  # type: ignore
        self.lineEditAnn.textChanged['QString'].connect(self.SpkrOut.setText)  # type: ignore
        self.CurStatOut.windowIconTextChanged['QString'].connect(self.SpkrOut.setText)  # type: ignore
        #self.vertSliderBrk.valueChanged.connect(lambda : self.calBrakeOutput())
        #self.vertSliderPow.valueChanged.connect(lambda : self.calAccelOutput())  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.groupBox_3.setTitle("FOR TRAIN ENGINEER ONLY")
        # self.inputKp.valueChanged.connect(lambda : self.onKpValueChanged())
        # self.inputKi.valueChanged.connect(lambda : self.onKiValueChanged())
        #self.temp.valueChanged.connect(self.tempControl)
        #self.Ebrake.clicked.connect(lambda : self.ebrake_enable())

        #if the button is checked, it will call HARDWARE FUCNTION ONLY

        #self.buttonDoorR.clicked.connect(chad function)
        #self.buttonDoorL.clicked.connect(chad function)
    """

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Brake"))
        self.groupBox_2.setTitle(_translate("MainWindow", "POWER"))
        self.label_20.setText(_translate("MainWindow", "FAILURES"))
        self.PwrFail.setText(_translate("MainWindow", "Power"))
        self.BrkFail.setText(_translate("MainWindow", "Brakes"))
        self.SigFail.setText(_translate("MainWindow", "Signal Pickup"))
        self.label_11.setText(_translate("MainWindow", "Accelerate %"))
        self.undergrnd_ind.setText(_translate("MainWindow", "Underground"))
        #self.trainSel.setItemText(0, _translate("MainWindow", "Train 1"))
        #self.trainSel.setItemText(1, _translate("MainWindow", "Train 2"))
        #self.trainSel.setItemText(2, _translate("MainWindow", "Train 3"))
        self.Ebrake.setText(_translate("MainWindow", "Emergency Brake"))
        self.CabinConditionsBox.setTitle(_translate("MainWindow", "Cabin Conditions"))
        self.buttonDoorR.setText(_translate("MainWindow", "Right"))
        self.label_13.setText(_translate("MainWindow", "Doors"))
        self.IntLights.setText(_translate("MainWindow", "Int Litghs"))
        self.buttonHDon.setText(_translate("MainWindow", "On"))
        self.buttonDoorL.setText(_translate("MainWindow", "Left"))
        self.buttonHDoff.setText(_translate("MainWindow", "Off"))
        self.label.setText(_translate("MainWindow", "Headlights"))
        self.label_14.setText(_translate("MainWindow", "Cabin Temp °F"))
        self.Announcement.setText(_translate("MainWindow", "Annoucement :"))
        self.lineEditAnn.setPlaceholderText(_translate("MainWindow", "Annoucement"))
        self.CurrentOutput.setText(_translate("MainWindow", "Current Output : "))
        self.CurrentStation.setText(_translate("MainWindow", "Next Station : "))
        self.SpeakerOuputs.setText(_translate("MainWindow", "Speaker Outputs"))
        self.CurStatOut.setText(_translate("MainWindow", "Yard"))
        self.DistanceTillStop.setText(_translate("MainWindow", "Distance until Stop (ft)"))
        self.Mode_Box.setTitle(_translate("MainWindow", "Mode"))
        self.buttonMan.setText(_translate("MainWindow", "Manual"))
        self.buttonAuto.setText(_translate("MainWindow", "Auto"))
        self.Speed_Limit.setText(_translate("MainWindow", "Speed Limit (mph)"))
        self.Commanded_Speed.setText(_translate("MainWindow", "Commanded Speed (mph)"))
        self.Current_Speed.setText(_translate("MainWindow", "Current Speed (mph)"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Power"))
        self.label_4.setText(_translate("MainWindow", "Ki"))
        self.label_3.setText(_translate("MainWindow", "Kp"))


