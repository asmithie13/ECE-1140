# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUI.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_MainUIWindow(object):
    def setupUi(self, MainUIWindow):
        if not MainUIWindow.objectName():
            MainUIWindow.setObjectName(u"MainUIWindow")
        MainUIWindow.resize(424, 455)
        MainUIWindow.setStyleSheet(u"background-color: rgb(233, 247, 255);")
        self.MainColumnLayout = QWidget(MainUIWindow)
        self.MainColumnLayout.setObjectName(u"MainColumnLayout")
        self.pushButton = QPushButton(self.MainColumnLayout)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 50, 61, 61))
        icon = QIcon()
        icon.addFile(u"logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(70, 70))
        self.label = QLabel(self.MainColumnLayout)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 351, 16))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.SpeedBox = QGroupBox(self.MainColumnLayout)
        self.SpeedBox.setObjectName(u"SpeedBox")
        self.SpeedBox.setGeometry(QRect(100, 40, 242, 80))
        self.SpeedBox.setStyleSheet(u"QGroupBox {\n"
"    background-color: white;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.SpeedBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SpeedSliderLayout = QHBoxLayout()
        self.SpeedSliderLayout.setSpacing(18)
        self.SpeedSliderLayout.setObjectName(u"SpeedSliderLayout")
        self.SpeedSliderLayout.setContentsMargins(3, -1, 3, -1)
        self.label_3 = QLabel(self.SpeedBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")

        self.SpeedSliderLayout.addWidget(self.label_3)

        self.SpeedSlider = QSlider(self.SpeedBox)
        self.SpeedSlider.setObjectName(u"SpeedSlider")
        self.SpeedSlider.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")
        self.SpeedSlider.setMinimum(1)
        self.SpeedSlider.setMaximum(100)
        self.SpeedSlider.setSingleStep(10)
        self.SpeedSlider.setOrientation(Qt.Horizontal)

        self.SpeedSliderLayout.addWidget(self.SpeedSlider)

        self.label_4 = QLabel(self.SpeedBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")

        self.SpeedSliderLayout.addWidget(self.label_4)


        self.verticalLayout.addLayout(self.SpeedSliderLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PauseButton = QPushButton(self.SpeedBox)
        self.PauseButton.setObjectName(u"PauseButton")
        self.PauseButton.setCheckable(True)
        self.PauseButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.PauseButton)

        self.CurrentSpeedLabel = QLabel(self.SpeedBox)
        self.CurrentSpeedLabel.setObjectName(u"CurrentSpeedLabel")
        self.CurrentSpeedLabel.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.CurrentSpeedLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.layoutWidget = QWidget(self.MainColumnLayout)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(120, 130, 221, 292))
        self.layoutWidget.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.WaysideSW_Button = QPushButton(self.layoutWidget)
        self.WaysideSW_Button.setObjectName(u"WaysideSW_Button")
        self.WaysideSW_Button.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")

        self.gridLayout.addWidget(self.WaysideSW_Button, 2, 0, 1, 1)

        self.WaysideHW_Button = QPushButton(self.layoutWidget)
        self.WaysideHW_Button.setObjectName(u"WaysideHW_Button")
        self.WaysideHW_Button.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")

        self.gridLayout.addWidget(self.WaysideHW_Button, 3, 0, 1, 1)

        self.TrainModelButton = QPushButton(self.layoutWidget)
        self.TrainModelButton.setObjectName(u"TrainModelButton")
        self.TrainModelButton.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")

        self.gridLayout.addWidget(self.TrainModelButton, 6, 0, 1, 1)

        self.TrainControllerHW_Button = QPushButton(self.layoutWidget)
        self.TrainControllerHW_Button.setObjectName(u"TrainControllerHW_Button")
        self.TrainControllerHW_Button.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")

        self.gridLayout.addWidget(self.TrainControllerHW_Button, 8, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.TrainSelecLabel = QLabel(self.layoutWidget)
        self.TrainSelecLabel.setObjectName(u"TrainSelecLabel")
        self.TrainSelecLabel.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.TrainSelecLabel, 0, 0, 1, 1)

        self.TrainSelect = QComboBox(self.layoutWidget)
        self.TrainSelect.setObjectName(u"TrainSelect")
        self.TrainSelect.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.TrainSelect, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 5, 0, 1, 1)

        self.TrainControllerSW_Button = QPushButton(self.layoutWidget)
        self.TrainControllerSW_Button.setObjectName(u"TrainControllerSW_Button")
        self.TrainControllerSW_Button.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")

        self.gridLayout.addWidget(self.TrainControllerSW_Button, 7, 0, 1, 1)

        self.CTC_Button = QPushButton(self.layoutWidget)
        self.CTC_Button.setObjectName(u"CTC_Button")
        self.CTC_Button.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")

        self.gridLayout.addWidget(self.CTC_Button, 1, 0, 1, 1)

        self.TrackModelButton = QPushButton(self.layoutWidget)
        self.TrackModelButton.setObjectName(u"TrackModelButton")
        self.TrackModelButton.setStyleSheet(u"\n"
"    background-color: white;\n"
"\n"
"")

        self.gridLayout.addWidget(self.TrackModelButton, 4, 0, 1, 1)

        MainUIWindow.setCentralWidget(self.MainColumnLayout)

        self.retranslateUi(MainUIWindow)

        QMetaObject.connectSlotsByName(MainUIWindow)
    # setupUi

    def retranslateUi(self, MainUIWindow):
        MainUIWindow.setWindowTitle(QCoreApplication.translate("MainUIWindow", u"Main UI", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainUIWindow", u"Orange Juice and the Cowboy Hats", None))
        self.SpeedBox.setTitle(QCoreApplication.translate("MainUIWindow", u"Simulation Speed Control", None))
        self.label_3.setText(QCoreApplication.translate("MainUIWindow", u"1x Speed", None))
        self.label_4.setText(QCoreApplication.translate("MainUIWindow", u"100x Speed", None))
        self.PauseButton.setText(QCoreApplication.translate("MainUIWindow", u"Start Simulation", None))
        self.CurrentSpeedLabel.setText(QCoreApplication.translate("MainUIWindow", u"Current Speed: 1x", None))
        self.WaysideSW_Button.setText(QCoreApplication.translate("MainUIWindow", u"Wayside SW", None))
        self.WaysideHW_Button.setText(QCoreApplication.translate("MainUIWindow", u"Wayside HW", None))
        self.TrainModelButton.setText(QCoreApplication.translate("MainUIWindow", u"Train Model", None))
        self.TrainControllerHW_Button.setText(QCoreApplication.translate("MainUIWindow", u"Train Controller HW", None))
        self.TrainSelecLabel.setText(QCoreApplication.translate("MainUIWindow", u"Select Train", None))
        self.TrainControllerSW_Button.setText(QCoreApplication.translate("MainUIWindow", u"Train Controller SW", None))
        self.CTC_Button.setText(QCoreApplication.translate("MainUIWindow", u"CTC", None))
        self.TrackModelButton.setText(QCoreApplication.translate("MainUIWindow", u"Track Model", None))
    # retranslateUi

