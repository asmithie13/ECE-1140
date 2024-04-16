# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testBench.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QWidget)

class Ui_TestBench(object):
    def setupUi(self, TestBench):
        if not TestBench.objectName():
            TestBench.setObjectName(u"TestBench")
        TestBench.resize(571, 665)
        self.centralwidget = QWidget(TestBench)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayout = QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.KI = QDoubleSpinBox(self.centralwidget)
        self.KI.setObjectName(u"KI")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.KI)

        self.SpeedLimit = QDoubleSpinBox(self.centralwidget)
        self.SpeedLimit.setObjectName(u"SpeedLimit")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.SpeedLimit)

        self.CurSpeed = QDoubleSpinBox(self.centralwidget)
        self.CurSpeed.setObjectName(u"CurSpeed")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.CurSpeed)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_7)

        self.Authority = QDoubleSpinBox(self.centralwidget)
        self.Authority.setObjectName(u"Authority")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.Authority)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_10)

        self.CabinTemp = QDoubleSpinBox(self.centralwidget)
        self.CabinTemp.setObjectName(u"CabinTemp")
        self.CabinTemp.setMinimum(60.000000000000000)
        self.CabinTemp.setMaximum(90.000000000000000)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.CabinTemp)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.OpenLeft = QPushButton(self.centralwidget)
        self.OpenLeft.setObjectName(u"OpenLeft")
        self.OpenLeft.setCheckable(True)
        self.OpenLeft.setChecked(True)

        self.horizontalLayout.addWidget(self.OpenLeft)

        self.CloseLeft = QPushButton(self.centralwidget)
        self.CloseLeft.setObjectName(u"CloseLeft")
        self.CloseLeft.setCheckable(True)

        self.horizontalLayout.addWidget(self.CloseLeft)

        self.OpenRight = QPushButton(self.centralwidget)
        self.OpenRight.setObjectName(u"OpenRight")
        self.OpenRight.setCheckable(True)
        self.OpenRight.setChecked(True)

        self.horizontalLayout.addWidget(self.OpenRight)

        self.CloseRight = QPushButton(self.centralwidget)
        self.CloseRight.setObjectName(u"CloseRight")
        self.CloseRight.setCheckable(True)

        self.horizontalLayout.addWidget(self.CloseRight)


        self.formLayout.setLayout(12, QFormLayout.FieldRole, self.horizontalLayout)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_5)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.HLightOn = QPushButton(self.centralwidget)
        self.HLightOn.setObjectName(u"HLightOn")
        self.HLightOn.setCheckable(True)
        self.HLightOn.setChecked(True)

        self.horizontalLayout_3.addWidget(self.HLightOn)

        self.HLightOff = QPushButton(self.centralwidget)
        self.HLightOff.setObjectName(u"HLightOff")
        self.HLightOff.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.HLightOff)


        self.formLayout.setLayout(15, QFormLayout.FieldRole, self.horizontalLayout_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.KP = QDoubleSpinBox(self.centralwidget)
        self.KP.setObjectName(u"KP")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.KP)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_11)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_6)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_4)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.Power = QDoubleSpinBox(self.centralwidget)
        self.Power.setObjectName(u"Power")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Power)

        self.Brake = QDoubleSpinBox(self.centralwidget)
        self.Brake.setObjectName(u"Brake")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.Brake)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.CSpeed = QDoubleSpinBox(self.centralwidget)
        self.CSpeed.setObjectName(u"CSpeed")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.CSpeed)

        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_13)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.label_14)

        self.Station = QLineEdit(self.centralwidget)
        self.Station.setObjectName(u"Station")

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.Station)

        self.Announcement = QLineEdit(self.centralwidget)
        self.Announcement.setObjectName(u"Announcement")

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.Announcement)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.label_15)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.PowerFailure = QPushButton(self.centralwidget)
        self.PowerFailure.setObjectName(u"PowerFailure")
        self.PowerFailure.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.PowerFailure)

        self.BrakeFailure = QPushButton(self.centralwidget)
        self.BrakeFailure.setObjectName(u"BrakeFailure")
        self.BrakeFailure.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.BrakeFailure)

        self.SignalFailure = QPushButton(self.centralwidget)
        self.SignalFailure.setObjectName(u"SignalFailure")
        self.SignalFailure.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.SignalFailure)


        self.formLayout.setLayout(20, QFormLayout.FieldRole, self.horizontalLayout_4)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(21, QFormLayout.LabelRole, self.label_16)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Auto = QPushButton(self.centralwidget)
        self.Auto.setObjectName(u"Auto")
        self.Auto.setCheckable(True)
        self.Auto.setChecked(True)

        self.horizontalLayout_5.addWidget(self.Auto)

        self.Manual = QPushButton(self.centralwidget)
        self.Manual.setObjectName(u"Manual")
        self.Manual.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.Manual)


        self.formLayout.setLayout(21, QFormLayout.FieldRole, self.horizontalLayout_5)

        self.CabinLights = QSlider(self.centralwidget)
        self.CabinLights.setObjectName(u"CabinLights")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CabinLights.sizePolicy().hasHeightForWidth())
        self.CabinLights.setSizePolicy(sizePolicy)
        self.CabinLights.setOrientation(Qt.Horizontal)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.CabinLights)

        TestBench.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TestBench)
        self.statusbar.setObjectName(u"statusbar")
        TestBench.setStatusBar(self.statusbar)

        self.retranslateUi(TestBench)
        self.Auto.clicked["bool"].connect(self.Manual.toggle)
        self.Manual.clicked["bool"].connect(self.Auto.toggle)
        self.HLightOff.clicked["bool"].connect(self.HLightOn.toggle)
        self.HLightOn.clicked["bool"].connect(self.HLightOff.toggle)
        self.OpenLeft.clicked["bool"].connect(self.CloseLeft.toggle)
        self.OpenRight.clicked["bool"].connect(self.CloseRight.toggle)
        self.CloseLeft.clicked["bool"].connect(self.OpenLeft.toggle)
        self.CloseRight.clicked["bool"].connect(self.OpenRight.toggle)

        QMetaObject.connectSlotsByName(TestBench)
    # setupUi

    def retranslateUi(self, TestBench):
        TestBench.setWindowTitle(QCoreApplication.translate("TestBench", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("TestBench", u"Ki", None))
        self.label_7.setText(QCoreApplication.translate("TestBench", u"Authority", None))
        self.label_10.setText(QCoreApplication.translate("TestBench", u"Cabin Temp", None))
        self.label_9.setText(QCoreApplication.translate("TestBench", u"Doors", None))
        self.OpenLeft.setText(QCoreApplication.translate("TestBench", u"Open Left", None))
        self.CloseLeft.setText(QCoreApplication.translate("TestBench", u"Close Left", None))
        self.OpenRight.setText(QCoreApplication.translate("TestBench", u"Open Right", None))
        self.CloseRight.setText(QCoreApplication.translate("TestBench", u"Close Right", None))
        self.label_5.setText(QCoreApplication.translate("TestBench", u"Cabin Lights", None))
        self.label_8.setText(QCoreApplication.translate("TestBench", u"Headlights", None))
        self.HLightOn.setText(QCoreApplication.translate("TestBench", u"On", None))
        self.HLightOff.setText(QCoreApplication.translate("TestBench", u"Off", None))
        self.label_2.setText(QCoreApplication.translate("TestBench", u"Kp", None))
        self.label_11.setText(QCoreApplication.translate("TestBench", u"Power", None))
        self.label_6.setText(QCoreApplication.translate("TestBench", u"Speed Limit", None))
        self.label_4.setText(QCoreApplication.translate("TestBench", u"Current Speed", None))
        self.label_12.setText(QCoreApplication.translate("TestBench", u"Brake", None))
        self.label_3.setText(QCoreApplication.translate("TestBench", u"Commanded speed", None))
        self.label_13.setText(QCoreApplication.translate("TestBench", u"Announce", None))
        self.label_14.setText(QCoreApplication.translate("TestBench", u"Station", None))
        self.label_15.setText(QCoreApplication.translate("TestBench", u"Failures", None))
        self.PowerFailure.setText(QCoreApplication.translate("TestBench", u"Power", None))
        self.BrakeFailure.setText(QCoreApplication.translate("TestBench", u"Brake", None))
        self.SignalFailure.setText(QCoreApplication.translate("TestBench", u"Signal", None))
        self.label_16.setText(QCoreApplication.translate("TestBench", u"Mode", None))
        self.Auto.setText(QCoreApplication.translate("TestBench", u"Auto", None))
        self.Manual.setText(QCoreApplication.translate("TestBench", u"Manual", None))
    # retranslateUi

