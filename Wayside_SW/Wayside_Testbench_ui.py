# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Wayside_Testbench.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_14 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_7.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_7)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_6.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_6)

        self.modeInput = QPushButton(self.centralwidget)
        self.modeInput.setObjectName(u"modeInput")

        self.horizontalLayout_4.addWidget(self.modeInput)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_8)

        self.addBlock = QLineEdit(self.centralwidget)
        self.addBlock.setObjectName(u"addBlock")

        self.horizontalLayout_5.addWidget(self.addBlock)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.removeBlock = QLineEdit(self.centralwidget)
        self.removeBlock.setObjectName(u"removeBlock")

        self.horizontalLayout_5.addWidget(self.removeBlock)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_14.addLayout(self.verticalLayout_3)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_14.addWidget(self.line)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_5.addWidget(self.label_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_12.addWidget(self.label_3)

        self.tbBlockMenu = QComboBox(self.centralwidget)
        self.tbBlockMenu.setObjectName(u"tbBlockMenu")

        self.horizontalLayout_12.addWidget(self.tbBlockMenu)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)

        self.horizontalLayout_10.addWidget(self.label_20)

        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        self.label_19.setFont(font3)

        self.horizontalLayout_10.addWidget(self.label_19)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.horizontalLayout_11.addWidget(self.label_21)

        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)

        self.horizontalLayout_11.addWidget(self.label_22)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font2)

        self.horizontalLayout_13.addWidget(self.label_23)

        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)

        self.horizontalLayout_13.addWidget(self.label_24)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.comSpeed = QLabel(self.centralwidget)
        self.comSpeed.setObjectName(u"comSpeed")

        self.horizontalLayout_6.addWidget(self.comSpeed)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_13)

        self.authOut = QLabel(self.centralwidget)
        self.authOut.setObjectName(u"authOut")

        self.horizontalLayout_7.addWidget(self.authOut)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.horizontalLayout_9.addWidget(self.label_17)

        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_9.addWidget(self.label_18)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.horizontalLayout_8.addWidget(self.label_15)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_8.addWidget(self.label_16)


        self.verticalLayout_6.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_14.addLayout(self.verticalLayout_6)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Test Inputs", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Train ID, Speed, Authority.", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.modeInput.setText(QCoreApplication.translate("MainWindow", u"PUSH", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Select Occupied Block:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Discard Occupied Block:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Test Outputs", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Selected Block:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Light:", None))
        self.label_19.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Crossing:", None))
        self.label_22.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Switch:", None))
        self.label_24.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed (mph):", None))
        self.comSpeed.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Authority (ft):", None))
        self.authOut.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Authority (bool):", None))
        self.label_4.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Block Occupancy:", None))
        self.label_18.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"MANUAL", None))
    # retranslateUi

