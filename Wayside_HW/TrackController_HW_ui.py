# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrackController_HW.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_TrackController_HW(object):
    def setupUi(self, TrackController_HW):
        if not TrackController_HW.objectName():
            TrackController_HW.setObjectName(u"TrackController_HW")
        TrackController_HW.resize(702, 600)
        TrackController_HW.setMinimumSize(QSize(700, 600))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(234, 234, 234, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        TrackController_HW.setPalette(palette)
        self.centralwidget = QWidget(TrackController_HW)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_10 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelTitle = QLabel(self.centralwidget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(22)
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.labelTitle.setAutoFillBackground(True)
        self.labelTitle.setFrameShape(QFrame.StyledPanel)
        self.labelTitle.setTextFormat(Qt.AutoText)
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelTitle)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelLineColor = QLabel(self.centralwidget)
        self.labelLineColor.setObjectName(u"labelLineColor")
        self.labelLineColor.setMinimumSize(QSize(300, 0))
        self.labelLineColor.setMaximumSize(QSize(230, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(18)
        font1.setBold(False)
        self.labelLineColor.setFont(font1)
        self.labelLineColor.setFrameShape(QFrame.StyledPanel)
        self.labelLineColor.setTextFormat(Qt.AutoText)
        self.labelLineColor.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelLineColor)

        self.labelSections = QLabel(self.centralwidget)
        self.labelSections.setObjectName(u"labelSections")
        self.labelSections.setEnabled(True)
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.labelSections.setFont(font2)
        self.labelSections.setFrameShape(QFrame.StyledPanel)
        self.labelSections.setTextFormat(Qt.AutoText)
        self.labelSections.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelSections)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_10.addLayout(self.verticalLayout)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frameMode = QFrame(self.centralwidget)
        self.frameMode.setObjectName(u"frameMode")
        self.frameMode.setFrameShape(QFrame.Panel)
        self.frameMode.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frameMode)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelMode = QLabel(self.frameMode)
        self.labelMode.setObjectName(u"labelMode")
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(24)
        font3.setBold(True)
        self.labelMode.setFont(font3)
        self.labelMode.setFrameShape(QFrame.NoFrame)
        self.labelMode.setTextFormat(Qt.AutoText)
        self.labelMode.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.labelMode)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkBoxAutomatic = QCheckBox(self.frameMode)
        self.checkBoxAutomatic.setObjectName(u"checkBoxAutomatic")
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(16)
        self.checkBoxAutomatic.setFont(font4)
        self.checkBoxAutomatic.setChecked(True)

        self.horizontalLayout_2.addWidget(self.checkBoxAutomatic)

        self.checkBoxManual = QCheckBox(self.frameMode)
        self.checkBoxManual.setObjectName(u"checkBoxManual")
        self.checkBoxManual.setFont(font4)

        self.horizontalLayout_2.addWidget(self.checkBoxManual)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_9.addWidget(self.frameMode)

        self.groupBoxManual = QGroupBox(self.centralwidget)
        self.groupBoxManual.setObjectName(u"groupBoxManual")
        self.groupBoxManual.setEnabled(True)
        self.groupBoxManual.setMinimumSize(QSize(260, 350))
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(12)
        font5.setBold(True)
        self.groupBoxManual.setFont(font5)
        self.groupBoxManual.setCheckable(False)
        self.groupBoxManual.setChecked(False)
        self.verticalLayout_6 = QVBoxLayout(self.groupBoxManual)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelSection = QLabel(self.groupBoxManual)
        self.labelSection.setObjectName(u"labelSection")
        self.labelSection.setEnabled(True)
        font6 = QFont()
        font6.setFamilies([u"Times New Roman"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.labelSection.setFont(font6)

        self.horizontalLayout_4.addWidget(self.labelSection)

        self.comboBoxSection = QComboBox(self.groupBoxManual)
        self.comboBoxSection.setObjectName(u"comboBoxSection")
        self.comboBoxSection.setEnabled(True)
        self.comboBoxSection.setDuplicatesEnabled(False)

        self.horizontalLayout_4.addWidget(self.comboBoxSection)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelBlock = QLabel(self.groupBoxManual)
        self.labelBlock.setObjectName(u"labelBlock")
        self.labelBlock.setEnabled(True)
        self.labelBlock.setFont(font6)

        self.horizontalLayout_5.addWidget(self.labelBlock)

        self.comboBoxBlock = QComboBox(self.groupBoxManual)
        self.comboBoxBlock.setObjectName(u"comboBoxBlock")
        self.comboBoxBlock.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.comboBoxBlock)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.frameLight = QFrame(self.groupBoxManual)
        self.frameLight.setObjectName(u"frameLight")
        self.frameLight.setFrameShape(QFrame.Panel)
        self.frameLight.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameLight)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelLight = QLabel(self.frameLight)
        self.labelLight.setObjectName(u"labelLight")
        self.labelLight.setEnabled(True)
        self.labelLight.setFont(font6)
        self.labelLight.setFrameShape(QFrame.NoFrame)
        self.labelLight.setLineWidth(-2)
        self.labelLight.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.labelLight)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pushButtonRed = QPushButton(self.frameLight)
        self.pushButtonRed.setObjectName(u"pushButtonRed")
        self.pushButtonRed.setEnabled(True)
        self.pushButtonRed.setFlat(False)

        self.horizontalLayout_8.addWidget(self.pushButtonRed)

        self.pushButtonGreen = QPushButton(self.frameLight)
        self.pushButtonGreen.setObjectName(u"pushButtonGreen")
        self.pushButtonGreen.setEnabled(True)

        self.horizontalLayout_8.addWidget(self.pushButtonGreen)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.verticalLayout_6.addWidget(self.frameLight)

        self.frameSwitch = QFrame(self.groupBoxManual)
        self.frameSwitch.setObjectName(u"frameSwitch")
        self.frameSwitch.setFrameShape(QFrame.Panel)
        self.frameSwitch.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameSwitch)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelSwitch = QLabel(self.frameSwitch)
        self.labelSwitch.setObjectName(u"labelSwitch")
        self.labelSwitch.setEnabled(True)
        self.labelSwitch.setFont(font6)
        self.labelSwitch.setFrameShape(QFrame.NoFrame)
        self.labelSwitch.setLineWidth(-2)
        self.labelSwitch.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelSwitch)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButtonLeft = QPushButton(self.frameSwitch)
        self.pushButtonLeft.setObjectName(u"pushButtonLeft")
        self.pushButtonLeft.setEnabled(True)

        self.horizontalLayout_7.addWidget(self.pushButtonLeft)

        self.pushButtonRight = QPushButton(self.frameSwitch)
        self.pushButtonRight.setObjectName(u"pushButtonRight")
        self.pushButtonRight.setEnabled(True)

        self.horizontalLayout_7.addWidget(self.pushButtonRight)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)


        self.verticalLayout_6.addWidget(self.frameSwitch)

        self.frameCrossing = QFrame(self.groupBoxManual)
        self.frameCrossing.setObjectName(u"frameCrossing")
        self.frameCrossing.setFrameShape(QFrame.Panel)
        self.frameCrossing.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frameCrossing)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.labelCrossing = QLabel(self.frameCrossing)
        self.labelCrossing.setObjectName(u"labelCrossing")
        self.labelCrossing.setEnabled(True)
        self.labelCrossing.setFont(font6)
        self.labelCrossing.setFrameShape(QFrame.NoFrame)
        self.labelCrossing.setLineWidth(-2)
        self.labelCrossing.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.labelCrossing)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButtonUp = QPushButton(self.frameCrossing)
        self.pushButtonUp.setObjectName(u"pushButtonUp")
        self.pushButtonUp.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.pushButtonUp)

        self.pushButtonDown = QPushButton(self.frameCrossing)
        self.pushButtonDown.setObjectName(u"pushButtonDown")
        self.pushButtonDown.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.pushButtonDown)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout_6.addWidget(self.frameCrossing)


        self.verticalLayout_9.addWidget(self.groupBoxManual)


        self.horizontalLayout_11.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBoxWaysideLayout = QGroupBox(self.centralwidget)
        self.groupBoxWaysideLayout.setObjectName(u"groupBoxWaysideLayout")
        self.groupBoxWaysideLayout.setMinimumSize(QSize(410, 300))
        self.groupBoxWaysideLayout.setFont(font5)
        self.gridLayout_3 = QGridLayout(self.groupBoxWaysideLayout)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelWaysideLayout = QLabel(self.groupBoxWaysideLayout)
        self.labelWaysideLayout.setObjectName(u"labelWaysideLayout")
        self.labelWaysideLayout.setFrameShape(QFrame.Box)
        self.labelWaysideLayout.setLineWidth(1)
        self.labelWaysideLayout.setPixmap(QPixmap(u"Wayside.jpg"))
        self.labelWaysideLayout.setScaledContents(True)

        self.gridLayout_3.addWidget(self.labelWaysideLayout, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.groupBoxWaysideLayout)

        self.frameOccupied = QFrame(self.centralwidget)
        self.frameOccupied.setObjectName(u"frameOccupied")
        self.frameOccupied.setMinimumSize(QSize(410, 150))
        self.frameOccupied.setFrameShape(QFrame.Panel)
        self.frameOccupied.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frameOccupied)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labelOccupied = QLabel(self.frameOccupied)
        self.labelOccupied.setObjectName(u"labelOccupied")
        self.labelOccupied.setFont(font6)

        self.horizontalLayout_9.addWidget(self.labelOccupied)

        self.lineEditOccupied = QLineEdit(self.frameOccupied)
        self.lineEditOccupied.setObjectName(u"lineEditOccupied")
        font7 = QFont()
        font7.setFamilies([u"Times New Roman"])
        font7.setPointSize(12)
        self.lineEditOccupied.setFont(font7)
        self.lineEditOccupied.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.lineEditOccupied)


        self.verticalLayout_11.addLayout(self.horizontalLayout_9)


        self.verticalLayout_7.addWidget(self.frameOccupied)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.horizontalLayout_11.addLayout(self.verticalLayout_8)


        self.verticalLayout_10.addLayout(self.horizontalLayout_11)

        TrackController_HW.setCentralWidget(self.centralwidget)

        self.retranslateUi(TrackController_HW)

        QMetaObject.connectSlotsByName(TrackController_HW)
    # setupUi

    def retranslateUi(self, TrackController_HW):
        TrackController_HW.setWindowTitle(QCoreApplication.translate("TrackController_HW", u"Wayside #1", None))
        self.labelTitle.setText(QCoreApplication.translate("TrackController_HW", u"Wayside #1 (Hardware)", None))
        self.labelLineColor.setText(QCoreApplication.translate("TrackController_HW", u"Line: Green", None))
        self.labelSections.setText(QCoreApplication.translate("TrackController_HW", u"Sections: A B C D E F G H T U V W X Y Z", None))
        self.labelMode.setText(QCoreApplication.translate("TrackController_HW", u"Mode", None))
        self.checkBoxAutomatic.setText(QCoreApplication.translate("TrackController_HW", u"Automatic", None))
        self.checkBoxManual.setText(QCoreApplication.translate("TrackController_HW", u"Manual", None))
        self.groupBoxManual.setTitle(QCoreApplication.translate("TrackController_HW", u"Manual", None))
        self.labelSection.setText(QCoreApplication.translate("TrackController_HW", u"Section", None))
        self.comboBoxSection.setPlaceholderText(QCoreApplication.translate("TrackController_HW", u"-", None))
        self.labelBlock.setText(QCoreApplication.translate("TrackController_HW", u"Block", None))
        self.comboBoxBlock.setPlaceholderText(QCoreApplication.translate("TrackController_HW", u"-", None))
        self.labelLight.setText(QCoreApplication.translate("TrackController_HW", u"Light", None))
        self.pushButtonRed.setText(QCoreApplication.translate("TrackController_HW", u"Red", None))
        self.pushButtonGreen.setText(QCoreApplication.translate("TrackController_HW", u"Green", None))
        self.labelSwitch.setText(QCoreApplication.translate("TrackController_HW", u"Switch", None))
        self.pushButtonLeft.setText(QCoreApplication.translate("TrackController_HW", u"Left", None))
        self.pushButtonRight.setText(QCoreApplication.translate("TrackController_HW", u"Right", None))
        self.labelCrossing.setText(QCoreApplication.translate("TrackController_HW", u"Crossing", None))
        self.pushButtonUp.setText(QCoreApplication.translate("TrackController_HW", u"Up", None))
        self.pushButtonDown.setText(QCoreApplication.translate("TrackController_HW", u"Down", None))
        self.groupBoxWaysideLayout.setTitle(QCoreApplication.translate("TrackController_HW", u"Wayside #1: Layout", None))
        self.labelWaysideLayout.setText("")
        self.labelOccupied.setText(QCoreApplication.translate("TrackController_HW", u"Occupied", None))
    # retranslateUi

