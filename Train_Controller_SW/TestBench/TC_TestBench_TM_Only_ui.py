# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TC_TestBench_TM_Only.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLCDNumber, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QRadioButton,
    QSizePolicy, QSpinBox, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 705)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 0, 129, 634))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_17 = QLabel(self.layoutWidget)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_2.addWidget(self.label_17)

        self.currspdin = QSpinBox(self.layoutWidget)
        self.currspdin.setObjectName(u"currspdin")

        self.verticalLayout_2.addWidget(self.currspdin)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.cmdspdin = QSpinBox(self.layoutWidget)
        self.cmdspdin.setObjectName(u"cmdspdin")

        self.verticalLayout_2.addWidget(self.cmdspdin)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.spdlimin = QSpinBox(self.layoutWidget)
        self.spdlimin.setObjectName(u"spdlimin")

        self.verticalLayout_2.addWidget(self.spdlimin)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.spinBox_3 = QSpinBox(self.layoutWidget)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.verticalLayout_2.addWidget(self.spinBox_3)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_2.addWidget(self.label_15)

        self.spinBox = QSpinBox(self.layoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(9999)

        self.verticalLayout_2.addWidget(self.spinBox)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.ebrakein = QRadioButton(self.layoutWidget)
        self.ebrakein.setObjectName(u"ebrakein")

        self.verticalLayout_2.addWidget(self.ebrakein)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_2.addWidget(self.label_9)

        self.beaconin = QLineEdit(self.layoutWidget)
        self.beaconin.setObjectName(u"beaconin")

        self.verticalLayout_2.addWidget(self.beaconin)

        self.label_14 = QLabel(self.layoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_2.addWidget(self.label_14)

        self.currtempin = QSpinBox(self.layoutWidget)
        self.currtempin.setObjectName(u"currtempin")

        self.verticalLayout_2.addWidget(self.currtempin)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.underground = QRadioButton(self.layoutWidget)
        self.underground.setObjectName(u"underground")

        self.verticalLayout_2.addWidget(self.underground)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_2.addWidget(self.label_11)

        self.pwrfailin = QRadioButton(self.layoutWidget)
        self.pwrfailin.setObjectName(u"pwrfailin")

        self.verticalLayout_2.addWidget(self.pwrfailin)

        self.brkfail = QRadioButton(self.layoutWidget)
        self.brkfail.setObjectName(u"brkfail")

        self.verticalLayout_2.addWidget(self.brkfail)

        self.sigfail = QRadioButton(self.layoutWidget)
        self.sigfail.setObjectName(u"sigfail")

        self.verticalLayout_2.addWidget(self.sigfail)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_2.addWidget(self.label_12)

        self.radioButton_3 = QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.verticalLayout_2.addWidget(self.radioButton_3)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(490, 60, 111, 449))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.layoutWidget1)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pow_out = QLCDNumber(self.layoutWidget1)
        self.pow_out.setObjectName(u"pow_out")

        self.verticalLayout.addWidget(self.pow_out)

        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout.addWidget(self.label_13)

        self.door_out = QLCDNumber(self.layoutWidget1)
        self.door_out.setObjectName(u"door_out")

        self.verticalLayout.addWidget(self.door_out)

        self.ExtLight = QLabel(self.layoutWidget1)
        self.ExtLight.setObjectName(u"ExtLight")

        self.verticalLayout.addWidget(self.ExtLight)

        self.lcdNumber = QLCDNumber(self.layoutWidget1)
        self.lcdNumber.setObjectName(u"lcdNumber")

        self.verticalLayout.addWidget(self.lcdNumber)

        self.InteriorLight = QLabel(self.layoutWidget1)
        self.InteriorLight.setObjectName(u"InteriorLight")

        self.verticalLayout.addWidget(self.InteriorLight)

        self.int_light = QLCDNumber(self.layoutWidget1)
        self.int_light.setObjectName(u"int_light")

        self.verticalLayout.addWidget(self.int_light)

        self.Desired_Temp = QLabel(self.layoutWidget1)
        self.Desired_Temp.setObjectName(u"Desired_Temp")

        self.verticalLayout.addWidget(self.Desired_Temp)

        self.des_temp = QLCDNumber(self.layoutWidget1)
        self.des_temp.setObjectName(u"des_temp")

        self.verticalLayout.addWidget(self.des_temp)

        self.DisableEbrake = QLabel(self.layoutWidget1)
        self.DisableEbrake.setObjectName(u"DisableEbrake")

        self.verticalLayout.addWidget(self.DisableEbrake)

        self.EbrakeStat = QCheckBox(self.layoutWidget1)
        self.EbrakeStat.setObjectName(u"EbrakeStat")
        self.EbrakeStat.setCheckable(True)

        self.verticalLayout.addWidget(self.EbrakeStat)

        self.label_6 = QLabel(self.layoutWidget1)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.Anon_Out = QLabel(self.layoutWidget1)
        self.Anon_Out.setObjectName(u"Anon_Out")

        self.verticalLayout.addWidget(self.Anon_Out)

        self.label_16 = QLabel(self.layoutWidget1)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout.addWidget(self.label_16)

        self.brakeen = QRadioButton(self.layoutWidget1)
        self.brakeen.setObjectName(u"brakeen")

        self.verticalLayout.addWidget(self.brakeen)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"From Train Controller", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Curr Spd", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CMD SPEED", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"SPEED LIM", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"SPEED LIM", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Pass Ebrake", None))
        self.ebrakein.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Beacon", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Curr Temp", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Underground", None))
        self.underground.setText(QCoreApplication.translate("MainWindow", u"underground", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Failures ", None))
        self.pwrfailin.setText(QCoreApplication.translate("MainWindow", u"pwrfail", None))
        self.brkfail.setText(QCoreApplication.translate("MainWindow", u"brkfail", None))
        self.sigfail.setText(QCoreApplication.translate("MainWindow", u"sigfail", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Block Passed", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"blockpassed", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"To Train Controller", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Door", None))
        self.ExtLight.setText(QCoreApplication.translate("MainWindow", u"Ext Light", None))
        self.InteriorLight.setText(QCoreApplication.translate("MainWindow", u"Interior Light", None))
        self.Desired_Temp.setText(QCoreApplication.translate("MainWindow", u"Desired Temp", None))
        self.DisableEbrake.setText(QCoreApplication.translate("MainWindow", u"Disable Ebrake", None))
        self.EbrakeStat.setText(QCoreApplication.translate("MainWindow", u"Ebrake On", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Annoucement ", None))
        self.Anon_Out.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Service Brake", None))
        self.brakeen.setText(QCoreApplication.translate("MainWindow", u"enabled", None))
    # retranslateUi

