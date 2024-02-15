# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrackControllerHW_UIdUZXTY.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_TrackControllerUI(object):
    def setupUi(self, TrackControllerUI):
        if not TrackControllerUI.objectName():
            TrackControllerUI.setObjectName(u"TrackControllerUI")
        TrackControllerUI.resize(748, 402)
        TrackControllerUI.setBaseSize(QSize(550, 400))
        palette = QPalette()
        brush = QBrush(QColor(215, 227, 240, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        TrackControllerUI.setPalette(palette)
        TrackControllerUI.setMouseTracking(True)
        TrackControllerUI.setLayoutDirection(Qt.RightToLeft)
        TrackControllerUI.setAutoFillBackground(False)
        self.centralwidget = QWidget(TrackControllerUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonSave = QPushButton(self.centralwidget)
        self.buttonSave.setObjectName(u"buttonSave")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(10)
        self.buttonSave.setFont(font)

        self.horizontalLayout.addWidget(self.buttonSave)

        self.buttonBrowse = QPushButton(self.centralwidget)
        self.buttonBrowse.setObjectName(u"buttonBrowse")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        self.buttonBrowse.setFont(font1)

        self.horizontalLayout.addWidget(self.buttonBrowse)

        self.lineEditBrowse = QLineEdit(self.centralwidget)
        self.lineEditBrowse.setObjectName(u"lineEditBrowse")
        self.lineEditBrowse.setFont(font1)
        self.lineEditBrowse.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEditBrowse)

        self.labelUpload = QLabel(self.centralwidget)
        self.labelUpload.setObjectName(u"labelUpload")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(14)
        self.labelUpload.setFont(font2)

        self.horizontalLayout.addWidget(self.labelUpload)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labelCrossingJunction = QLabel(self.centralwidget)
        self.labelCrossingJunction.setObjectName(u"labelCrossingJunction")
        self.labelCrossingJunction.setFont(font)

        self.verticalLayout_3.addWidget(self.labelCrossingJunction)

        self.labelPhoto = QLabel(self.centralwidget)
        self.labelPhoto.setObjectName(u"labelPhoto")
        self.labelPhoto.setMaximumSize(QSize(440, 250))
        self.labelPhoto.setPixmap(QPixmap(u"../../../../../../Documents/TrackController/blueline.png"))
        self.labelPhoto.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.labelPhoto)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.checkGreen = QCheckBox(self.centralwidget)
        self.checkGreen.setObjectName(u"checkGreen")
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(12)
        self.checkGreen.setFont(font3)

        self.horizontalLayout_2.addWidget(self.checkGreen)

        self.checkRed = QCheckBox(self.centralwidget)
        self.checkRed.setObjectName(u"checkRed")
        self.checkRed.setFont(font3)

        self.horizontalLayout_2.addWidget(self.checkRed)

        self.checkBlue = QCheckBox(self.centralwidget)
        self.checkBlue.setObjectName(u"checkBlue")
        self.checkBlue.setFont(font3)

        self.horizontalLayout_2.addWidget(self.checkBlue)

        self.labelSelectLine = QLabel(self.centralwidget)
        self.labelSelectLine.setObjectName(u"labelSelectLine")
        self.labelSelectLine.setFont(font2)

        self.horizontalLayout_2.addWidget(self.labelSelectLine)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBoxWayside = QComboBox(self.centralwidget)
        self.comboBoxWayside.addItem("")
        self.comboBoxWayside.addItem("")
        self.comboBoxWayside.addItem("")
        self.comboBoxWayside.setObjectName(u"comboBoxWayside")
        self.comboBoxWayside.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.comboBoxWayside)

        self.labelSelectWayside = QLabel(self.centralwidget)
        self.labelSelectWayside.setObjectName(u"labelSelectWayside")
        self.labelSelectWayside.setFont(font2)

        self.horizontalLayout_4.addWidget(self.labelSelectWayside)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.comboBoxCrossing = QComboBox(self.centralwidget)
        self.comboBoxCrossing.setObjectName(u"comboBoxCrossing")
        self.comboBoxCrossing.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_5.addWidget(self.comboBoxCrossing)

        self.labelCrossing = QLabel(self.centralwidget)
        self.labelCrossing.setObjectName(u"labelCrossing")
        self.labelCrossing.setFont(font3)

        self.horizontalLayout_5.addWidget(self.labelCrossing)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.comboBoxJunction = QComboBox(self.centralwidget)
        self.comboBoxJunction.setObjectName(u"comboBoxJunction")
        self.comboBoxJunction.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_7.addWidget(self.comboBoxJunction)

        self.labelJunction = QLabel(self.centralwidget)
        self.labelJunction.setObjectName(u"labelJunction")
        self.labelJunction.setFont(font3)

        self.horizontalLayout_7.addWidget(self.labelJunction)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_3)

        self.labelMode = QLabel(self.centralwidget)
        self.labelMode.setObjectName(u"labelMode")
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(20)
        self.labelMode.setFont(font4)

        self.verticalLayout_2.addWidget(self.labelMode, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkManual = QCheckBox(self.centralwidget)
        self.checkManual.setObjectName(u"checkManual")
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(16)
        self.checkManual.setFont(font5)

        self.horizontalLayout_6.addWidget(self.checkManual)

        self.checkAuto = QCheckBox(self.centralwidget)
        self.checkAuto.setObjectName(u"checkAuto")
        self.checkAuto.setFont(font5)

        self.horizontalLayout_6.addWidget(self.checkAuto)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEditOccupiedBlocks = QLineEdit(self.centralwidget)
        self.lineEditOccupiedBlocks.setObjectName(u"lineEditOccupiedBlocks")
        self.lineEditOccupiedBlocks.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.lineEditOccupiedBlocks)

        self.labelOcuppiedBlocks = QLabel(self.centralwidget)
        self.labelOcuppiedBlocks.setObjectName(u"labelOcuppiedBlocks")
        self.labelOcuppiedBlocks.setFont(font2)

        self.horizontalLayout_9.addWidget(self.labelOcuppiedBlocks)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEditClosedBlocks = QLineEdit(self.centralwidget)
        self.lineEditClosedBlocks.setObjectName(u"lineEditClosedBlocks")
        self.lineEditClosedBlocks.setReadOnly(True)

        self.horizontalLayout_10.addWidget(self.lineEditClosedBlocks)

        self.labelClosedBlocks = QLabel(self.centralwidget)
        self.labelClosedBlocks.setObjectName(u"labelClosedBlocks")
        self.labelClosedBlocks.setFont(font2)

        self.horizontalLayout_10.addWidget(self.labelClosedBlocks)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        TrackControllerUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(TrackControllerUI)

        QMetaObject.connectSlotsByName(TrackControllerUI)
    # setupUi

    def retranslateUi(self, TrackControllerUI):
        TrackControllerUI.setWindowTitle(QCoreApplication.translate("TrackControllerUI", u"Track Controller (HW)", None))
        self.buttonSave.setText(QCoreApplication.translate("TrackControllerUI", u"Save", None))
        self.buttonBrowse.setText(QCoreApplication.translate("TrackControllerUI", u"Browse", None))
        self.labelUpload.setText(QCoreApplication.translate("TrackControllerUI", u"Upload PLC File:", None))
        self.labelCrossingJunction.setText(QCoreApplication.translate("TrackControllerUI", u"Crossing/Junction View:", None))
        self.labelPhoto.setText("")
        self.checkGreen.setText(QCoreApplication.translate("TrackControllerUI", u"Green", None))
        self.checkRed.setText(QCoreApplication.translate("TrackControllerUI", u"Red", None))
        self.checkBlue.setText(QCoreApplication.translate("TrackControllerUI", u"Blue", None))
        self.labelSelectLine.setText(QCoreApplication.translate("TrackControllerUI", u"Select Line:", None))
        self.comboBoxWayside.setItemText(0, QCoreApplication.translate("TrackControllerUI", u"1", None))
        self.comboBoxWayside.setItemText(1, QCoreApplication.translate("TrackControllerUI", u"2", None))
        self.comboBoxWayside.setItemText(2, QCoreApplication.translate("TrackControllerUI", u"3", None))

        self.comboBoxWayside.setPlaceholderText(QCoreApplication.translate("TrackControllerUI", u"Select", None))
        self.labelSelectWayside.setText(QCoreApplication.translate("TrackControllerUI", u"Select Wayside:", None))
        self.comboBoxCrossing.setPlaceholderText(QCoreApplication.translate("TrackControllerUI", u"Select", None))
        self.labelCrossing.setText(QCoreApplication.translate("TrackControllerUI", u"Select Crossing:", None))
        self.comboBoxJunction.setPlaceholderText(QCoreApplication.translate("TrackControllerUI", u"Select", None))
        self.labelJunction.setText(QCoreApplication.translate("TrackControllerUI", u"Select Junction:", None))
        self.labelMode.setText(QCoreApplication.translate("TrackControllerUI", u"Mode:", None))
        self.checkManual.setText(QCoreApplication.translate("TrackControllerUI", u"Manual", None))
        self.checkAuto.setText(QCoreApplication.translate("TrackControllerUI", u"Automatic", None))
        self.labelOcuppiedBlocks.setText(QCoreApplication.translate("TrackControllerUI", u"Occupied Blocks:", None))
        self.labelClosedBlocks.setText(QCoreApplication.translate("TrackControllerUI", u"Closed Blocks:", None))
    # retranslateUi

