# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrainModel_UI.ui'
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
    QHBoxLayout, QLCDNumber, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModal)
        MainWindow.resize(1186, 720)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"background-color: rgb(233, 247, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(600, 0, 411, 41))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: rgb(158, 208, 255);\n"
"")
        self.label_2.setFrameShape(QFrame.StyledPanel)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(820, 40, 181, 261))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)

        self.length_of_vehicle_display = QLabel(self.verticalLayoutWidget_3)
        self.length_of_vehicle_display.setObjectName(u"length_of_vehicle_display")
        self.length_of_vehicle_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.length_of_vehicle_display)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_11)

        self.height_display = QLabel(self.verticalLayoutWidget_3)
        self.height_display.setObjectName(u"height_display")
        self.height_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.height_display)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_12)

        self.width_display = QLabel(self.verticalLayoutWidget_3)
        self.width_display.setObjectName(u"width_display")
        self.width_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.width_display)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_13)

        self.cspeed_display = QLabel(self.verticalLayoutWidget_3)
        self.cspeed_display.setObjectName(u"cspeed_display")
        self.cspeed_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.cspeed_display)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_14)

        self.grade_display = QLabel(self.verticalLayoutWidget_3)
        self.grade_display.setObjectName(u"grade_display")
        self.grade_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.grade_display)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_15)

        self.mass_display = QLabel(self.verticalLayoutWidget_3)
        self.mass_display.setObjectName(u"mass_display")
        self.mass_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.mass_display)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_16)

        self.pcount_display = QLabel(self.verticalLayoutWidget_3)
        self.pcount_display.setObjectName(u"pcount_display")
        self.pcount_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.pcount_display)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_17)

        self.ccount_display = QLabel(self.verticalLayoutWidget_3)
        self.ccount_display.setObjectName(u"ccount_display")
        self.ccount_display.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.ccount_display)

        self.Train_dropdown = QComboBox(self.centralwidget)
        self.Train_dropdown.addItem("")
        self.Train_dropdown.addItem("")
        self.Train_dropdown.addItem("")
        self.Train_dropdown.setObjectName(u"Train_dropdown")
        self.Train_dropdown.setGeometry(QRect(0, 0, 581, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.Train_dropdown.setFont(font1)
        self.Train_dropdown.setCursor(QCursor(Qt.PointingHandCursor))
        self.Train_dropdown.setStyleSheet(u"background-color: rgb(214, 214, 214);\n"
"selection-color: rgb(253, 253, 253);")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 30, 451, 281))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.groupBox_2.setFont(font2)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Power_label = QLabel(self.groupBox_2)
        self.Power_label.setObjectName(u"Power_label")
        self.Power_label.setFont(font2)
        self.Power_label.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.Power_label.setFrameShape(QFrame.Panel)

        self.verticalLayout_5.addWidget(self.Power_label)

        self.Acceleration_label = QLabel(self.groupBox_2)
        self.Acceleration_label.setObjectName(u"Acceleration_label")
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.Acceleration_label.setFont(font3)
        self.Acceleration_label.setStyleSheet(u"background-color: rgb(197, 197, 197);\n"
"font: 75 10pt \"Times New Roman\";")
        self.Acceleration_label.setFrameShape(QFrame.Panel)

        self.verticalLayout_5.addWidget(self.Acceleration_label)

        self.Acc_Velo_label = QLabel(self.groupBox_2)
        self.Acc_Velo_label.setObjectName(u"Acc_Velo_label")
        self.Acc_Velo_label.setFont(font2)
        self.Acc_Velo_label.setStyleSheet(u"background-color: rgb(197, 197, 197);")
        self.Acc_Velo_label.setFrameShape(QFrame.Panel)

        self.verticalLayout_5.addWidget(self.Acc_Velo_label)

        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(450, 30, 121, 281))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Power_value_lcd = QLCDNumber(self.verticalLayoutWidget_5)
        self.Power_value_lcd.setObjectName(u"Power_value_lcd")
        self.Power_value_lcd.setProperty("intValue", 743)

        self.verticalLayout_6.addWidget(self.Power_value_lcd)

        self.Acceleration_value_lcd = QLCDNumber(self.verticalLayoutWidget_5)
        self.Acceleration_value_lcd.setObjectName(u"Acceleration_value_lcd")
        self.Acceleration_value_lcd.setProperty("intValue", 39)

        self.verticalLayout_6.addWidget(self.Acceleration_value_lcd)

        self.Acc_Velo_value_lcd = QLCDNumber(self.verticalLayoutWidget_5)
        self.Acc_Velo_value_lcd.setObjectName(u"Acc_Velo_value_lcd")
        self.Acc_Velo_value_lcd.setProperty("intValue", 40)

        self.verticalLayout_6.addWidget(self.Acc_Velo_value_lcd)

        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(10, 410, 181, 201))
        self.verticalLayoutWidget_6.setFont(font2)
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.int_lights_label = QLabel(self.verticalLayoutWidget_6)
        self.int_lights_label.setObjectName(u"int_lights_label")
        self.int_lights_label.setFont(font2)
        self.int_lights_label.setFrameShape(QFrame.Box)

        self.verticalLayout_7.addWidget(self.int_lights_label)

        self.ext_lights_label = QLabel(self.verticalLayoutWidget_6)
        self.ext_lights_label.setObjectName(u"ext_lights_label")
        self.ext_lights_label.setFont(font2)
        self.ext_lights_label.setFrameShape(QFrame.Box)

        self.verticalLayout_7.addWidget(self.ext_lights_label)

        self.verticalLayoutWidget_7 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(210, 410, 111, 201))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(9)
        font4.setBold(True)
        self.verticalLayoutWidget_7.setFont(font4)
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.int_lights_value = QLabel(self.verticalLayoutWidget_7)
        self.int_lights_value.setObjectName(u"int_lights_value")
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        self.int_lights_value.setFont(font5)
        self.int_lights_value.setStyleSheet(u"background-color: rgb(192, 192, 192);\n"
"font: 75 12pt \"Times New Roman\";")
        self.int_lights_value.setFrameShape(QFrame.Box)

        self.verticalLayout_8.addWidget(self.int_lights_value)

        self.ext_lights_value = QLabel(self.verticalLayoutWidget_7)
        self.ext_lights_value.setObjectName(u"ext_lights_value")
        self.ext_lights_value.setFont(font5)
        self.ext_lights_value.setStyleSheet(u"background-color: rgb(192, 192, 192);\n"
"font: 75 12pt \"Times New Roman\";")
        self.ext_lights_value.setFrameShape(QFrame.Box)

        self.verticalLayout_8.addWidget(self.ext_lights_value)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(320, 400, 21, 211))
        self.line_4.setFont(font4)
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(660, 400, 21, 211))
        self.line_5.setFont(font4)
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.verticalLayoutWidget_10 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(350, 410, 181, 201))
        self.verticalLayoutWidget_10.setFont(font2)
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.right_door_label = QLabel(self.verticalLayoutWidget_10)
        self.right_door_label.setObjectName(u"right_door_label")
        self.right_door_label.setFont(font2)
        self.right_door_label.setFrameShape(QFrame.Box)

        self.verticalLayout_11.addWidget(self.right_door_label)

        self.left_doors_label = QLabel(self.verticalLayoutWidget_10)
        self.left_doors_label.setObjectName(u"left_doors_label")
        self.left_doors_label.setFont(font2)
        self.left_doors_label.setFrameShape(QFrame.Box)

        self.verticalLayout_11.addWidget(self.left_doors_label)

        self.verticalLayoutWidget_11 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(550, 410, 111, 201))
        self.verticalLayoutWidget_11.setFont(font4)
        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.right_doors_value = QLabel(self.verticalLayoutWidget_11)
        self.right_doors_value.setObjectName(u"right_doors_value")
        self.right_doors_value.setFont(font3)
        self.right_doors_value.setStyleSheet(u"background-color: rgb(192, 192, 192);\n"
"font: 75 10pt \"Times New Roman\";")
        self.right_doors_value.setFrameShape(QFrame.Box)

        self.verticalLayout_12.addWidget(self.right_doors_value)

        self.left_doors_value = QLabel(self.verticalLayoutWidget_11)
        self.left_doors_value.setObjectName(u"left_doors_value")
        self.left_doors_value.setFont(font3)
        self.left_doors_value.setStyleSheet(u"background-color: rgb(192, 192, 192);\n"
"font: 75 10pt \"Times New Roman\";")
        self.left_doors_value.setFrameShape(QFrame.Box)

        self.verticalLayout_12.addWidget(self.left_doors_value)

        self.verticalLayoutWidget_12 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(690, 410, 311, 203))
        self.verticalLayoutWidget_12.setFont(font2)
        self.verticalLayout_13 = QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.cabin_temp_label = QLabel(self.verticalLayoutWidget_12)
        self.cabin_temp_label.setObjectName(u"cabin_temp_label")
        self.cabin_temp_label.setFont(font2)
        self.cabin_temp_label.setFrameShape(QFrame.Box)

        self.verticalLayout_13.addWidget(self.cabin_temp_label)

        self.cabin_temp_value = QLabel(self.verticalLayoutWidget_12)
        self.cabin_temp_value.setObjectName(u"cabin_temp_value")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cabin_temp_value.sizePolicy().hasHeightForWidth())
        self.cabin_temp_value.setSizePolicy(sizePolicy)
        font6 = QFont()
        font6.setFamilies([u"Times New Roman"])
        font6.setPointSize(18)
        font6.setBold(True)
        font6.setItalic(False)
        self.cabin_temp_value.setFont(font6)
        self.cabin_temp_value.setLayoutDirection(Qt.LeftToRight)
        self.cabin_temp_value.setStyleSheet(u"background-color: rgb(192, 192, 192);\n"
"color: rgb(60, 60, 60)")
        self.cabin_temp_value.setFrameShape(QFrame.Box)
        self.cabin_temp_value.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.cabin_temp_value)

        self.brake_fail_label = QLabel(self.centralwidget)
        self.brake_fail_label.setObjectName(u"brake_fail_label")
        self.brake_fail_label.setGeometry(QRect(10, 320, 151, 71))
        self.brake_fail_label.setFont(font2)
        self.brake_fail_label.setStyleSheet(u"background-color: rgb(195, 16, 40);")
        self.brake_fail_label.setFrameShape(QFrame.Box)
        self.signal_fail_label = QLabel(self.centralwidget)
        self.signal_fail_label.setObjectName(u"signal_fail_label")
        self.signal_fail_label.setGeometry(QRect(350, 320, 151, 71))
        self.signal_fail_label.setFont(font2)
        self.signal_fail_label.setStyleSheet(u"background-color: rgb(195, 16, 40);")
        self.signal_fail_label.setFrameShape(QFrame.Box)
        self.engine_fail_label = QLabel(self.centralwidget)
        self.engine_fail_label.setObjectName(u"engine_fail_label")
        self.engine_fail_label.setGeometry(QRect(690, 320, 141, 71))
        self.engine_fail_label.setFont(font2)
        self.engine_fail_label.setStyleSheet(u"background-color: rgb(195, 16, 40);")
        self.engine_fail_label.setFrameShape(QFrame.Box)
        self.ad_label = QLabel(self.centralwidget)
        self.ad_label.setObjectName(u"ad_label")
        self.ad_label.setGeometry(QRect(1010, 150, 181, 471))
        self.ad_label.setStyleSheet(u"background-color: rgb(162, 162, 162);")
        self.ad_label.setPixmap(QPixmap(u"../../Tanvi's Tr Mod/bk_ad.png"))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(320, 320, 21, 71))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy1)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(660, 320, 21, 71))
        sizePolicy1.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy1)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(600, 40, 291, 271))
        font7 = QFont()
        font7.setFamilies([u"Times New Roman"])
        font7.setPointSize(9)
        self.layoutWidget.setFont(font7)
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_9)

        self.LengthVehicle_label = QLabel(self.layoutWidget)
        self.LengthVehicle_label.setObjectName(u"LengthVehicle_label")
        self.LengthVehicle_label.setEnabled(True)
        self.LengthVehicle_label.setFont(font5)
        self.LengthVehicle_label.setStyleSheet(u"font: 75 12pt \"Times New Roman\";")
        self.LengthVehicle_label.setFrameShape(QFrame.NoFrame)
        self.LengthVehicle_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.LengthVehicle_label)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_8)

        self.Height_label = QLabel(self.layoutWidget)
        self.Height_label.setObjectName(u"Height_label")
        self.Height_label.setEnabled(True)
        self.Height_label.setFont(font5)
        self.Height_label.setStyleSheet(u"font: 75 12pt \"Times New Roman\";")
        self.Height_label.setFrameShape(QFrame.NoFrame)
        self.Height_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.Height_label)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_7)

        self.Width_label = QLabel(self.layoutWidget)
        self.Width_label.setObjectName(u"Width_label")
        self.Width_label.setFont(font5)
        self.Width_label.setStyleSheet(u"font: 75 12pt \"Times New Roman\";")
        self.Width_label.setFrameShape(QFrame.NoFrame)
        self.Width_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.Width_label)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_6)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)
        self.label.setStyleSheet(u"font: 75 10pt \"Times New Roman\";")

        self.verticalLayout_4.addWidget(self.label)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_5)

        self.Grade_label = QLabel(self.layoutWidget)
        self.Grade_label.setObjectName(u"Grade_label")
        self.Grade_label.setFont(font5)
        self.Grade_label.setStyleSheet(u"font: 75 12pt \"Times New Roman\";")
        self.Grade_label.setFrameShape(QFrame.NoFrame)
        self.Grade_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.Grade_label)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.mass_vehicle_label = QLabel(self.layoutWidget)
        self.mass_vehicle_label.setObjectName(u"mass_vehicle_label")
        self.mass_vehicle_label.setFont(font5)
        self.mass_vehicle_label.setStyleSheet(u"font: 75 12pt \"Times New Roman\";")
        self.mass_vehicle_label.setFrameShape(QFrame.NoFrame)
        self.mass_vehicle_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.mass_vehicle_label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.Passenger_count_label = QLabel(self.layoutWidget)
        self.Passenger_count_label.setObjectName(u"Passenger_count_label")
        self.Passenger_count_label.setFont(font5)
        self.Passenger_count_label.setStyleSheet(u"font: 75 12pt \"Times New Roman\";")
        self.Passenger_count_label.setFrameShape(QFrame.NoFrame)
        self.Passenger_count_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.Passenger_count_label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.Crew_count_label = QLabel(self.layoutWidget)
        self.Crew_count_label.setObjectName(u"Crew_count_label")
        self.Crew_count_label.setFont(font5)
        self.Crew_count_label.setStyleSheet(u"font: 75 12pt \"Times New Roman\";")
        self.Crew_count_label.setFrameShape(QFrame.NoFrame)
        self.Crew_count_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.Crew_count_label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(180, 340, 131, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bf_enable = QPushButton(self.horizontalLayoutWidget)
        self.bf_enable.setObjectName(u"bf_enable")
        self.bf_enable.setAutoFillBackground(False)
        self.bf_enable.setStyleSheet(u"")
        self.bf_enable.setCheckable(False)
        self.bf_enable.setChecked(False)
        self.bf_enable.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.bf_enable)

        self.bf_disable = QPushButton(self.horizontalLayoutWidget)
        self.bf_disable.setObjectName(u"bf_disable")
        self.bf_disable.setStyleSheet(u"background-color : rgb(38, 207, 4)")
        self.bf_disable.setCheckable(False)

        self.horizontalLayout.addWidget(self.bf_disable)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(520, 340, 131, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sig_fail_enable = QPushButton(self.horizontalLayoutWidget_2)
        self.sig_fail_enable.setObjectName(u"sig_fail_enable")

        self.horizontalLayout_2.addWidget(self.sig_fail_enable)

        self.sig_fail_disable = QPushButton(self.horizontalLayoutWidget_2)
        self.sig_fail_disable.setObjectName(u"sig_fail_disable")
        self.sig_fail_disable.setStyleSheet(u"background-color : rgb(38, 207, 4)")

        self.horizontalLayout_2.addWidget(self.sig_fail_disable)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(860, 340, 131, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.en_fail_enable = QPushButton(self.horizontalLayoutWidget_5)
        self.en_fail_enable.setObjectName(u"en_fail_enable")

        self.horizontalLayout_5.addWidget(self.en_fail_enable)

        self.en_fail_disable = QPushButton(self.horizontalLayoutWidget_5)
        self.en_fail_disable.setObjectName(u"en_fail_disable")
        self.en_fail_disable.setStyleSheet(u"background-color : rgb(38, 207, 4)")

        self.horizontalLayout_5.addWidget(self.en_fail_disable)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(580, 0, 16, 311))
        self.line.setStyleSheet(u"color: rgb(4, 4, 4);\n"
"font: 22pt \"MS Shell Dlg 2\";")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(1050, 240, 111, 20))
        self.label_3.setStyleSheet(u"font: 6pt \"MS Shell Dlg 2\";")
        self.ebrake = QPushButton(self.centralwidget)
        self.ebrake.setObjectName(u"ebrake")
        self.ebrake.setGeometry(QRect(0, 620, 1191, 71))
        font8 = QFont()
        font8.setFamilies([u"Times New Roman"])
        font8.setPointSize(18)
        font8.setBold(True)
        self.ebrake.setFont(font8)
        self.ebrake.setCursor(QCursor(Qt.PointingHandCursor))
        self.ebrake.setStyleSheet(u"background-color: rgb(195, 16, 40);\n"
"selection-color: rgb(99, 99, 99);\n"
"")
        self.ebrake.setCheckable(False)
        self.ebrake.setAutoRepeat(True)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(1010, 0, 181, 151))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.ann_label = QLabel(self.verticalLayoutWidget)
        self.ann_label.setObjectName(u"ann_label")
        self.ann_label.setStyleSheet(u"background-color: rgb(197, 197, 197);\n"
"font: 75 10pt \"Times New Roman\";")

        self.verticalLayout.addWidget(self.ann_label)

        self.ann_out_label = QLabel(self.verticalLayoutWidget)
        self.ann_out_label.setObjectName(u"ann_out_label")
        self.ann_out_label.setStyleSheet(u"font: 12pt \"Times New Roman\";")
        self.ann_out_label.setFrameShape(QFrame.StyledPanel)
        self.ann_out_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.ann_out_label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.line_5.raise_()
        self.line_4.raise_()
        self.line.raise_()
        self.layoutWidget.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.Train_dropdown.raise_()
        self.groupBox_2.raise_()
        self.verticalLayoutWidget_5.raise_()
        self.verticalLayoutWidget_6.raise_()
        self.verticalLayoutWidget_7.raise_()
        self.verticalLayoutWidget_10.raise_()
        self.verticalLayoutWidget_11.raise_()
        self.verticalLayoutWidget_12.raise_()
        self.brake_fail_label.raise_()
        self.signal_fail_label.raise_()
        self.engine_fail_label.raise_()
        self.ad_label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.horizontalLayoutWidget_5.raise_()
        self.label_3.raise_()
        self.ebrake.raise_()
        self.verticalLayoutWidget.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.bf_enable.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LIVE TRAIN STATISTICS", None))
        self.length_of_vehicle_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">70</p></body></html>", None))
        self.height_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">15</p></body></html>", None))
        self.width_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">56</p></body></html>", None))
        self.cspeed_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">15.83</p></body></html>", None))
        self.grade_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">0.3</p></body></html>", None))
        self.mass_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">12000</p></body></html>", None))
        self.pcount_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">74</p></body></html>", None))
        self.ccount_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\">2</p></body></html>", None))
        self.Train_dropdown.setItemText(0, QCoreApplication.translate("MainWindow", u"Train 1", None))
        self.Train_dropdown.setItemText(1, QCoreApplication.translate("MainWindow", u"Train 2", None))
        self.Train_dropdown.setItemText(2, QCoreApplication.translate("MainWindow", u"Train 3", None))

        self.groupBox_2.setTitle("")
        self.Power_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">POWER (kW)</span></p></body></html>", None))
        self.Acceleration_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">ACCELERATION (ft/s</span><span style=\" font-size:16pt; font-weight:600; vertical-align:super;\">2</span><span style=\" font-size:16pt; font-weight:600;\">)</span></p></body></html>", None))
        self.Acc_Velo_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">ACTUAL VELOCITY (mph)</span></p></body></html>", None))
        self.int_lights_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Interior </p><p align=\"center\">Lights</p></body></html>", None))
        self.ext_lights_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Exterior</p><p align=\"center\">Lights</p></body></html>", None))
        self.int_lights_value.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#464646;\">OFF</span></p></body></html>", None))
        self.ext_lights_value.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#464646;\">ON</span></p></body></html>", None))
        self.right_door_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Right </p><p align=\"center\">Doors</p></body></html>", None))
        self.left_doors_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Left</p><p align=\"center\">Doors</p></body></html>", None))
        self.right_doors_value.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#464646;\">CLOSED</span></p></body></html>", None))
        self.left_doors_value.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; color:#464646;\">CLOSED</span></p></body></html>", None))
        self.cabin_temp_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">CABIN </p><p align=\"center\">TEMPERATURE</p></body></html>", None))
        self.cabin_temp_value.setText(QCoreApplication.translate("MainWindow", u"68 F", None))
        self.brake_fail_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">BRAKE</p><p align=\"center\">FAILURE</p></body></html>", None))
        self.signal_fail_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SIGNAL </p><p align=\"center\">FAILURE</p></body></html>", None))
        self.engine_fail_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">ENGINE</p><p align=\"center\">FAILURE</p></body></html>", None))
        self.ad_label.setText("")
        self.LengthVehicle_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Length of Vehicle (ft) :</span></p></body></html>", None))
        self.Height_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Height (ft) :</span></p></body></html>", None))
        self.Width_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Width (ft) :</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed (mph)", None))
        self.Grade_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Grade (%) :</span></p></body></html>", None))
        self.mass_vehicle_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Mass of  Vehicle (lbs) :</span></p></body></html>", None))
        self.Passenger_count_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Passenger Count :</span></p></body></html>", None))
        self.Crew_count_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Crew Count :</span></p></body></html>", None))
        self.bf_enable.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.bf_disable.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.sig_fail_enable.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.sig_fail_disable.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.en_fail_enable.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.en_fail_disable.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">ADVERTISEMENTS:</p></body></html>", None))
        self.ebrake.setText(QCoreApplication.translate("MainWindow", u"EMERGENCY BRAKE", None))
        self.ann_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">ANNOUNCEMENTS</span></p></body></html>", None))
        self.ann_out_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">The Train will depart from Herron Station at 10am</span></p></body></html>", None))
    # retranslateUi

