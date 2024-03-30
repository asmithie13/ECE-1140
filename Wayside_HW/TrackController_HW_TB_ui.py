# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrackController_HW_TB.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_WaysideTestBench(object):
    def setupUi(self, WaysideTestBench):
        if not WaysideTestBench.objectName():
            WaysideTestBench.setObjectName(u"WaysideTestBench")
        WaysideTestBench.resize(700, 455)
        WaysideTestBench.setMinimumSize(QSize(700, 455))
        self.centralwidget = QWidget(WaysideTestBench)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelTitle = QLabel(self.centralwidget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(24)
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.labelTitle.setFrameShape(QFrame.Panel)
        self.labelTitle.setFrameShadow(QFrame.Raised)
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelTitle)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Panel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelInputs = QLabel(self.frame)
        self.labelInputs.setObjectName(u"labelInputs")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.labelInputs.setFont(font1)
        self.labelInputs.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelInputs)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelOccupancies = QLabel(self.frame)
        self.labelOccupancies.setObjectName(u"labelOccupancies")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(14)
        font2.setBold(True)
        self.labelOccupancies.setFont(font2)

        self.horizontalLayout.addWidget(self.labelOccupancies)

        self.comboBoxOccupancies = QComboBox(self.frame)
        self.comboBoxOccupancies.setObjectName(u"comboBoxOccupancies")
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(12)
        self.comboBoxOccupancies.setFont(font3)

        self.horizontalLayout.addWidget(self.comboBoxOccupancies)

        self.pushButtonClearOcc = QPushButton(self.frame)
        self.pushButtonClearOcc.setObjectName(u"pushButtonClearOcc")
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(12)
        font4.setBold(True)
        self.pushButtonClearOcc.setFont(font4)

        self.horizontalLayout.addWidget(self.pushButtonClearOcc)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelClosures = QLabel(self.frame)
        self.labelClosures.setObjectName(u"labelClosures")
        self.labelClosures.setFont(font2)

        self.horizontalLayout_2.addWidget(self.labelClosures)

        self.comboBoxClosures = QComboBox(self.frame)
        self.comboBoxClosures.setObjectName(u"comboBoxClosures")
        self.comboBoxClosures.setFont(font3)

        self.horizontalLayout_2.addWidget(self.comboBoxClosures)

        self.pushButtonClearClose = QPushButton(self.frame)
        self.pushButtonClearClose.setObjectName(u"pushButtonClearClose")
        self.pushButtonClearClose.setFont(font4)

        self.horizontalLayout_2.addWidget(self.pushButtonClearClose)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.verticalLayout.addWidget(self.label_3)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setBold(True)
        self.groupBox.setFont(font5)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.labelTrainIDIn = QLabel(self.groupBox)
        self.labelTrainIDIn.setObjectName(u"labelTrainIDIn")
        self.labelTrainIDIn.setFont(font2)

        self.horizontalLayout_13.addWidget(self.labelTrainIDIn)

        self.lineEditTrainIDIn = QLineEdit(self.groupBox)
        self.lineEditTrainIDIn.setObjectName(u"lineEditTrainIDIn")
        self.lineEditTrainIDIn.setFont(font4)

        self.horizontalLayout_13.addWidget(self.lineEditTrainIDIn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelAuthIn = QLabel(self.groupBox)
        self.labelAuthIn.setObjectName(u"labelAuthIn")
        self.labelAuthIn.setFont(font2)

        self.horizontalLayout_3.addWidget(self.labelAuthIn)

        self.lineEditAuthIn = QLineEdit(self.groupBox)
        self.lineEditAuthIn.setObjectName(u"lineEditAuthIn")
        self.lineEditAuthIn.setFont(font4)

        self.horizontalLayout_3.addWidget(self.lineEditAuthIn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelSpeedIn = QLabel(self.groupBox)
        self.labelSpeedIn.setObjectName(u"labelSpeedIn")
        self.labelSpeedIn.setFont(font2)

        self.horizontalLayout_4.addWidget(self.labelSpeedIn)

        self.lineEditSpeedIn = QLineEdit(self.groupBox)
        self.lineEditSpeedIn.setObjectName(u"lineEditSpeedIn")
        self.lineEditSpeedIn.setFont(font4)

        self.horizontalLayout_4.addWidget(self.lineEditSpeedIn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.pushButtonSendSpeedAuth = QPushButton(self.groupBox)
        self.pushButtonSendSpeedAuth.setObjectName(u"pushButtonSendSpeedAuth")
        self.pushButtonSendSpeedAuth.setFont(font4)

        self.verticalLayout_3.addWidget(self.pushButtonSendSpeedAuth)


        self.verticalLayout.addWidget(self.groupBox)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.verticalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.verticalLayout.addWidget(self.label_7)


        self.horizontalLayout_11.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Panel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelOutputs = QLabel(self.frame_2)
        self.labelOutputs.setObjectName(u"labelOutputs")
        self.labelOutputs.setFont(font1)
        self.labelOutputs.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelOutputs)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelBlockStates = QLabel(self.frame_2)
        self.labelBlockStates.setObjectName(u"labelBlockStates")
        self.labelBlockStates.setFont(font2)

        self.horizontalLayout_5.addWidget(self.labelBlockStates)

        self.comboBoxBlockStates = QComboBox(self.frame_2)
        self.comboBoxBlockStates.setObjectName(u"comboBoxBlockStates")
        self.comboBoxBlockStates.setFont(font3)
        self.comboBoxBlockStates.setEditable(True)

        self.horizontalLayout_5.addWidget(self.comboBoxBlockStates)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelLight = QLabel(self.frame_2)
        self.labelLight.setObjectName(u"labelLight")
        self.labelLight.setFont(font3)

        self.horizontalLayout_6.addWidget(self.labelLight)

        self.lineEditLight = QLineEdit(self.frame_2)
        self.lineEditLight.setObjectName(u"lineEditLight")
        self.lineEditLight.setFont(font3)
        self.lineEditLight.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEditLight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.labelSwitch = QLabel(self.frame_2)
        self.labelSwitch.setObjectName(u"labelSwitch")
        self.labelSwitch.setFont(font3)

        self.horizontalLayout_7.addWidget(self.labelSwitch)

        self.lineEditSwitch = QLineEdit(self.frame_2)
        self.lineEditSwitch.setObjectName(u"lineEditSwitch")
        self.lineEditSwitch.setFont(font3)
        self.lineEditSwitch.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.lineEditSwitch)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.labelCrossing = QLabel(self.frame_2)
        self.labelCrossing.setObjectName(u"labelCrossing")
        self.labelCrossing.setFont(font3)

        self.horizontalLayout_8.addWidget(self.labelCrossing)

        self.lineEditCrossing = QLineEdit(self.frame_2)
        self.lineEditCrossing.setObjectName(u"lineEditCrossing")
        self.lineEditCrossing.setFont(font3)
        self.lineEditCrossing.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.lineEditCrossing)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.labelTrainIDOut = QLabel(self.frame_2)
        self.labelTrainIDOut.setObjectName(u"labelTrainIDOut")
        self.labelTrainIDOut.setFont(font2)

        self.horizontalLayout_14.addWidget(self.labelTrainIDOut)

        self.lineEditTrainIDOut = QLineEdit(self.frame_2)
        self.lineEditTrainIDOut.setObjectName(u"lineEditTrainIDOut")
        self.lineEditTrainIDOut.setFont(font4)
        self.lineEditTrainIDOut.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.lineEditTrainIDOut)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labelAuthOut = QLabel(self.frame_2)
        self.labelAuthOut.setObjectName(u"labelAuthOut")
        self.labelAuthOut.setFont(font2)

        self.horizontalLayout_9.addWidget(self.labelAuthOut)

        self.lineEditAuthOut = QLineEdit(self.frame_2)
        self.lineEditAuthOut.setObjectName(u"lineEditAuthOut")
        self.lineEditAuthOut.setFont(font3)

        self.horizontalLayout_9.addWidget(self.lineEditAuthOut)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.labelSpeedOut = QLabel(self.frame_2)
        self.labelSpeedOut.setObjectName(u"labelSpeedOut")
        self.labelSpeedOut.setFont(font2)

        self.horizontalLayout_10.addWidget(self.labelSpeedOut)

        self.lineEditSpeedOut = QLineEdit(self.frame_2)
        self.lineEditSpeedOut.setObjectName(u"lineEditSpeedOut")
        self.lineEditSpeedOut.setFont(font3)
        self.lineEditSpeedOut.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.lineEditSpeedOut)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.labelOccOut = QLabel(self.frame_2)
        self.labelOccOut.setObjectName(u"labelOccOut")
        self.labelOccOut.setFont(font2)

        self.horizontalLayout_12.addWidget(self.labelOccOut)

        self.lineEditOccupancies = QLineEdit(self.frame_2)
        self.lineEditOccupancies.setObjectName(u"lineEditOccupancies")
        self.lineEditOccupancies.setFont(font3)
        self.lineEditOccupancies.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.lineEditOccupancies)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_11.addWidget(self.frame_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        WaysideTestBench.setCentralWidget(self.centralwidget)

        self.retranslateUi(WaysideTestBench)

        QMetaObject.connectSlotsByName(WaysideTestBench)
    # setupUi

    def retranslateUi(self, WaysideTestBench):
        WaysideTestBench.setWindowTitle(QCoreApplication.translate("WaysideTestBench", u"Wayside #1 -TestBench", None))
        self.labelTitle.setText(QCoreApplication.translate("WaysideTestBench", u"Wayside #1 (Hardware) - TestBench", None))
        self.labelInputs.setText(QCoreApplication.translate("WaysideTestBench", u"Inputs", None))
        self.labelOccupancies.setText(QCoreApplication.translate("WaysideTestBench", u"Occupancies:", None))
        self.pushButtonClearOcc.setText(QCoreApplication.translate("WaysideTestBench", u"Clear", None))
        self.label.setText(QCoreApplication.translate("WaysideTestBench", u"List of Blocks - From Track Model", None))
        self.labelClosures.setText(QCoreApplication.translate("WaysideTestBench", u"Closures:", None))
        self.pushButtonClearClose.setText(QCoreApplication.translate("WaysideTestBench", u"Clear", None))
        self.label_2.setText(QCoreApplication.translate("WaysideTestBench", u"List of Blocks - From CTC Office", None))
        self.label_3.setText(QCoreApplication.translate("WaysideTestBench", u"All closures must be added to the occupancy list.", None))
        self.groupBox.setTitle(QCoreApplication.translate("WaysideTestBench", u"Per-Train Speed and Authority", None))
        self.labelTrainIDIn.setText(QCoreApplication.translate("WaysideTestBench", u"Train ID:", None))
        self.labelAuthIn.setText(QCoreApplication.translate("WaysideTestBench", u"Per-Train Authority:", None))
        self.labelSpeedIn.setText(QCoreApplication.translate("WaysideTestBench", u"Per-Train Speed:", None))
        self.pushButtonSendSpeedAuth.setText(QCoreApplication.translate("WaysideTestBench", u"Send", None))
        self.label_6.setText(QCoreApplication.translate("WaysideTestBench", u"Speed and authority are passed-along", None))
        self.label_7.setText(QCoreApplication.translate("WaysideTestBench", u"to train controller. Wayside authority is Boolean.", None))
        self.labelOutputs.setText(QCoreApplication.translate("WaysideTestBench", u"Outputs", None))
        self.labelBlockStates.setText(QCoreApplication.translate("WaysideTestBench", u"Block States:", None))
        self.labelLight.setText(QCoreApplication.translate("WaysideTestBench", u"Light:", None))
        self.labelSwitch.setText(QCoreApplication.translate("WaysideTestBench", u"Switch:", None))
        self.labelCrossing.setText(QCoreApplication.translate("WaysideTestBench", u"Crossing:", None))
        self.labelTrainIDOut.setText(QCoreApplication.translate("WaysideTestBench", u"Train ID:", None))
        self.labelAuthOut.setText(QCoreApplication.translate("WaysideTestBench", u"Per-Train Authority:", None))
        self.labelSpeedOut.setText(QCoreApplication.translate("WaysideTestBench", u"Per-Speed Authority:", None))
        self.labelOccOut.setText(QCoreApplication.translate("WaysideTestBench", u"Occupancies:", None))
    # retranslateUi

