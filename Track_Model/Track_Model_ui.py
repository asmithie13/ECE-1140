# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Track_Model.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLCDNumber, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpinBox,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 750)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 500))
        MainWindow.setMaximumSize(QSize(942, 777))
        MainWindow.setStyleSheet(u"background-color: rgb(233, 247, 255);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_38 = QGridLayout()
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.line_select = QComboBox(self.centralwidget)
        self.line_select.addItem("")
        self.line_select.addItem("")
        self.line_select.addItem("")
        self.line_select.setObjectName(u"line_select")
        self.line_select.setStyleSheet(u"background-color: white;")

        self.gridLayout_38.addWidget(self.line_select, 0, 1, 1, 1)

        self.block_in_1 = QComboBox(self.centralwidget)
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.addItem("")
        self.block_in_1.setObjectName(u"block_in_1")
        self.block_in_1.setStyleSheet(u"background-color: white;\n"
"")

        self.gridLayout_38.addWidget(self.block_in_1, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_38, 1, 0, 1, 2)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMaximumSize(QSize(200, 122))
        self.groupBox_6.setStyleSheet(u"QGroupBox {\n"
"    background-color: white;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_1207 = QPushButton(self.groupBox_6)
        self.pushButton_1207.setObjectName(u"pushButton_1207")
        self.pushButton_1207.setFocusPolicy(Qt.NoFocus)
        self.pushButton_1207.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"		 background-color: white;\n"
"    }\n"
"\"\"\")\n"
"")
        icon = QIcon()
        icon.addFile(u"switch.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_1207.setIcon(icon)
        self.pushButton_1207.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton_1207, 0, 0, 1, 1)

        self.label_130 = QLabel(self.groupBox_6)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setStyleSheet(u"background-color: white\n"
"")

        self.gridLayout.addWidget(self.label_130, 0, 1, 1, 1)

        self.pushButton_1208 = QPushButton(self.groupBox_6)
        self.pushButton_1208.setObjectName(u"pushButton_1208")
        self.pushButton_1208.setFocusPolicy(Qt.NoFocus)
        self.pushButton_1208.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"		 background-color: white;\n"
"    }\n"
"\"\"\")\n"
"")
        icon1 = QIcon()
        icon1.addFile(u"crossing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_1208.setIcon(icon1)
        self.pushButton_1208.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.pushButton_1208, 1, 0, 1, 1)

        self.label_131 = QLabel(self.groupBox_6)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setStyleSheet(u"background-color: white\n"
"")

        self.gridLayout.addWidget(self.label_131, 1, 1, 1, 1)

        self.pushButton_1209 = QPushButton(self.groupBox_6)
        self.pushButton_1209.setObjectName(u"pushButton_1209")
        self.pushButton_1209.setFocusPolicy(Qt.NoFocus)
        self.pushButton_1209.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"		 background-color: rbg(233, 247, 255);\n"
"    }\n"
"\"\"\")\n"
"")
        icon2 = QIcon()
        icon2.addFile(u"light.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_1209.setIcon(icon2)
        self.pushButton_1209.setIconSize(QSize(40, 30))

        self.gridLayout.addWidget(self.pushButton_1209, 2, 0, 1, 1)

        self.label_132 = QLabel(self.groupBox_6)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setStyleSheet(u"background-color: white\n"
"")

        self.gridLayout.addWidget(self.label_132, 2, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_6, 5, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setMinimumSize(QSize(50, 55))
        self.groupBox_4.setMaximumSize(QSize(16777215, 55))
        self.groupBox_4.setStyleSheet(u"QGroupBox {\n"
"    background-color: white;\n"
"}\n"
"")
        self.gridLayout_41 = QGridLayout(self.groupBox_4)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.label_149 = QLabel(self.groupBox_4)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setStyleSheet(u"background-color: white;\n"
"\n"
"")

        self.gridLayout_41.addWidget(self.label_149, 0, 0, 1, 1)

        self.switch_out = QLabel(self.groupBox_4)
        self.switch_out.setObjectName(u"switch_out")
        self.switch_out.setStyleSheet(u"background: white")
        self.switch_out.setFrameShape(QFrame.Box)
        self.switch_out.setAlignment(Qt.AlignCenter)

        self.gridLayout_41.addWidget(self.switch_out, 0, 4, 1, 1)

        self.light_out = QLabel(self.groupBox_4)
        self.light_out.setObjectName(u"light_out")
        self.light_out.setLayoutDirection(Qt.LeftToRight)
        self.light_out.setStyleSheet(u"background: white")
        self.light_out.setFrameShape(QFrame.Box)
        self.light_out.setAlignment(Qt.AlignCenter)

        self.gridLayout_41.addWidget(self.light_out, 0, 1, 1, 1)

        self.label_148 = QLabel(self.groupBox_4)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setStyleSheet(u"background-color: white;\n"
"\n"
"")

        self.gridLayout_41.addWidget(self.label_148, 0, 3, 1, 1)

        self.line_6 = QFrame(self.groupBox_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_41.addWidget(self.line_6, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_4, 4, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMaximumSize(QSize(200, 400))
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    background-color: white;\n"
"}\n"
"")
        self.gridLayout_39 = QGridLayout(self.groupBox_2)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.label_135 = QLabel(self.groupBox_2)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setStyleSheet(u"background-color: rgb(white);")
        self.label_135.setFrameShape(QFrame.NoFrame)

        self.gridLayout_39.addWidget(self.label_135, 6, 0, 1, 1)

        self.label_138 = QLabel(self.groupBox_2)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setStyleSheet(u"background-color: rgb(white);")
        self.label_138.setFrameShape(QFrame.NoFrame)

        self.gridLayout_39.addWidget(self.label_138, 0, 0, 1, 1)

        self.cumm_elevation_in = QLabel(self.groupBox_2)
        self.cumm_elevation_in.setObjectName(u"cumm_elevation_in")
        self.cumm_elevation_in.setStyleSheet(u"background-color: rgb(white);")
        self.cumm_elevation_in.setFrameShape(QFrame.Box)

        self.gridLayout_39.addWidget(self.cumm_elevation_in, 5, 1, 1, 1)

        self.label_139 = QLabel(self.groupBox_2)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setStyleSheet(u"background-color: rgb(white);")
        self.label_139.setFrameShape(QFrame.NoFrame)

        self.gridLayout_39.addWidget(self.label_139, 5, 0, 1, 1)

        self.label_143 = QLabel(self.groupBox_2)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setStyleSheet(u"background-color: rgb(white);")
        self.label_143.setFrameShape(QFrame.NoFrame)

        self.gridLayout_39.addWidget(self.label_143, 10, 0, 1, 1)

        self.length_in = QLabel(self.groupBox_2)
        self.length_in.setObjectName(u"length_in")
        self.length_in.setStyleSheet(u"background-color: rgb(white);")
        self.length_in.setFrameShape(QFrame.Box)

        self.gridLayout_39.addWidget(self.length_in, 6, 1, 1, 1)

        self.label_133 = QLabel(self.groupBox_2)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setStyleSheet(u"background-color: rgb(white);")
        self.label_133.setFrameShape(QFrame.NoFrame)

        self.gridLayout_39.addWidget(self.label_133, 2, 0, 1, 1)

        self.cross_out = QLabel(self.groupBox_2)
        self.cross_out.setObjectName(u"cross_out")
        self.cross_out.setStyleSheet(u"background-color: rgb(white);")
        self.cross_out.setFrameShape(QFrame.Box)

        self.gridLayout_39.addWidget(self.cross_out, 10, 1, 1, 1)

        self.elevation_in = QLabel(self.groupBox_2)
        self.elevation_in.setObjectName(u"elevation_in")
        self.elevation_in.setStyleSheet(u"background-color: rgb(white);")
        self.elevation_in.setFrameShape(QFrame.Box)

        self.gridLayout_39.addWidget(self.elevation_in, 4, 1, 1, 1)

        self.block_num_in = QLabel(self.groupBox_2)
        self.block_num_in.setObjectName(u"block_num_in")
        self.block_num_in.setStyleSheet(u"background-color: rgb(white);")
        self.block_num_in.setFrameShape(QFrame.Box)

        self.gridLayout_39.addWidget(self.block_num_in, 0, 1, 1, 1)

        self.label_136 = QLabel(self.groupBox_2)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setStyleSheet(u"background-color: rgb(white);")
        self.label_136.setFrameShape(QFrame.NoFrame)

        self.gridLayout_39.addWidget(self.label_136, 9, 0, 1, 1)

        self.label_141 = QLabel(self.groupBox_2)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setStyleSheet(u"background-color: rgb(white);")
        self.label_141.setFrameShape(QFrame.NoFrame)

        self.gridLayout_39.addWidget(self.label_141, 11, 0, 1, 1)

        self.temp_out = QLabel(self.groupBox_2)
        self.temp_out.setObjectName(u"temp_out")
        self.temp_out.setStyleSheet(u"background-color: rgb(white);")
        self.temp_out.setFrameShape(QFrame.Box)

        self.gridLayout_39.addWidget(self.temp_out, 8, 1, 1, 1)

        self.grade_in = QLabel(self.groupBox_2)
        self.grade_in.setObjectName(u"grade_in")
        self.grade_in.setStyleSheet(u"background-color: rgb(white);")
        self.grade_in.setFrameShape(QFrame.Box)

        self.gridLayout_39.addWidget(self.grade_in, 3, 1, 1, 1)

        self.section_in = QLabel(self.groupBox_2)
        self.section_in.setObjectName(u"section_in")
        self.section_in.setStyleSheet(u"background-color: rgb(white);")
        self.section_in.setFrameShape(QFrame.Box)

        self.gridLayout_39.addWidget(self.section_in, 1, 1, 1, 1)

        self.label_142 = QLabel(self.groupBox_2)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setStyleSheet(u"background-color: rgb(white);")
        self.label_142.setFrameShape(QFrame.NoFrame)

        self.gridLayout_39.addWidget(self.label_142, 8, 0, 1, 1)

        self.under_out = QLabel(self.groupBox_2)
        self.under_out.setObjectName(u"under_out")
        sizePolicy.setHeightForWidth(self.under_out.sizePolicy().hasHeightForWidth())
        self.under_out.setSizePolicy(sizePolicy)
        self.under_out.setMinimumSize(QSize(64, 25))
        self.under_out.setStyleSheet(u"background-color: rgb(white);")
        self.under_out.setFrameShape(QFrame.Box)

        self.gridLayout_39.addWidget(self.under_out, 11, 1, 1, 1)

        self.label_144 = QLabel(self.groupBox_2)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setStyleSheet(u"background-color: rgb(white);")
        self.label_144.setFrameShape(QFrame.NoFrame)

        self.gridLayout_39.addWidget(self.label_144, 3, 0, 1, 1)

        self.label_134 = QLabel(self.groupBox_2)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setStyleSheet(u"background-color: rgb(white);")
        self.label_134.setFrameShape(QFrame.NoFrame)

        self.gridLayout_39.addWidget(self.label_134, 1, 0, 1, 1)

        self.label_140 = QLabel(self.groupBox_2)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setStyleSheet(u"background-color: rgb(white);")
        self.label_140.setFrameShape(QFrame.NoFrame)

        self.gridLayout_39.addWidget(self.label_140, 7, 0, 1, 1)

        self.occupancy_in = QLabel(self.groupBox_2)
        self.occupancy_in.setObjectName(u"occupancy_in")
        self.occupancy_in.setStyleSheet(u"background-color: rgb(white);")
        self.occupancy_in.setFrameShape(QFrame.Box)

        self.gridLayout_39.addWidget(self.occupancy_in, 2, 1, 1, 1)

        self.heaters_out = QLabel(self.groupBox_2)
        self.heaters_out.setObjectName(u"heaters_out")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.heaters_out.sizePolicy().hasHeightForWidth())
        self.heaters_out.setSizePolicy(sizePolicy2)
        self.heaters_out.setMinimumSize(QSize(64, 25))
        self.heaters_out.setStyleSheet(u"background-color: rgb(white);")
        self.heaters_out.setFrameShape(QFrame.Box)

        self.gridLayout_39.addWidget(self.heaters_out, 9, 1, 1, 1)

        self.label_137 = QLabel(self.groupBox_2)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setStyleSheet(u"background-color: rgb(white);")
        self.label_137.setFrameShape(QFrame.NoFrame)

        self.gridLayout_39.addWidget(self.label_137, 4, 0, 1, 1)

        self.speed_in = QLabel(self.groupBox_2)
        self.speed_in.setObjectName(u"speed_in")
        self.speed_in.setStyleSheet(u"background-color: rgb(white);")
        self.speed_in.setFrameShape(QFrame.Box)

        self.gridLayout_39.addWidget(self.speed_in, 7, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_2, 2, 2, 1, 1)

        self.groupBox_13 = QGroupBox(self.centralwidget)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMaximumSize(QSize(200, 16777215))
        self.groupBox_13.setStyleSheet(u"QGroupBox {\n"
"    background-color: white;\n"
"}\n"
"")
        self.gridLayout_42 = QGridLayout(self.groupBox_13)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.label_150 = QLabel(self.groupBox_13)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setStyleSheet(u"background-color: rgb(white);")

        self.gridLayout_42.addWidget(self.label_150, 0, 0, 1, 1)

        self.spinBox_6 = QSpinBox(self.groupBox_13)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setStyleSheet(u"background-color: rgb(white);")

        self.gridLayout_42.addWidget(self.spinBox_6, 0, 1, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_13, 0, 2, 2, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setMaximumSize(QSize(16777215, 122))
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    background-color: white;\n"
"}\n"
"")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_145 = QLabel(self.groupBox)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setStyleSheet(u"background-color: rgb(white);")
        self.label_145.setFrameShape(QFrame.Box)

        self.gridLayout_3.addWidget(self.label_145, 1, 0, 1, 1)

        self.label_147 = QLabel(self.groupBox)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setStyleSheet(u"background-color: rgb(white);")
        self.label_147.setFrameShape(QFrame.Box)

        self.gridLayout_3.addWidget(self.label_147, 3, 0, 1, 1)

        self.block_in_2 = QComboBox(self.groupBox)
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.addItem("")
        self.block_in_2.setObjectName(u"block_in_2")
        self.block_in_2.setStyleSheet(u"background-color: white;\n"
"")

        self.gridLayout_3.addWidget(self.block_in_2, 0, 0, 1, 1)

        self.set_power_failure = QPushButton(self.groupBox)
        self.set_power_failure.setObjectName(u"set_power_failure")
        sizePolicy.setHeightForWidth(self.set_power_failure.sizePolicy().hasHeightForWidth())
        self.set_power_failure.setSizePolicy(sizePolicy)
        self.set_power_failure.setMinimumSize(QSize(221, 23))
        self.set_power_failure.setStyleSheet(u"background-color: rgb(white);")

        self.gridLayout_3.addWidget(self.set_power_failure, 3, 1, 1, 1)

        self.label_146 = QLabel(self.groupBox)
        self.label_146.setObjectName(u"label_146")
        sizePolicy2.setHeightForWidth(self.label_146.sizePolicy().hasHeightForWidth())
        self.label_146.setSizePolicy(sizePolicy2)
        self.label_146.setStyleSheet(u"background-color: rgb(white);")
        self.label_146.setFrameShape(QFrame.Box)

        self.gridLayout_3.addWidget(self.label_146, 2, 0, 1, 1)

        self.reset_button = QPushButton(self.groupBox)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setStyleSheet(u"background-color: rgb(white);")

        self.gridLayout_3.addWidget(self.reset_button, 0, 1, 1, 1)

        self.set_track_failure = QPushButton(self.groupBox)
        self.set_track_failure.setObjectName(u"set_track_failure")
        sizePolicy.setHeightForWidth(self.set_track_failure.sizePolicy().hasHeightForWidth())
        self.set_track_failure.setSizePolicy(sizePolicy)
        self.set_track_failure.setMinimumSize(QSize(221, 23))
        self.set_track_failure.setStyleSheet(u"background-color: rgb(white);")

        self.gridLayout_3.addWidget(self.set_track_failure, 2, 1, 1, 1)

        self.set_broken_rail = QPushButton(self.groupBox)
        self.set_broken_rail.setObjectName(u"set_broken_rail")
        sizePolicy.setHeightForWidth(self.set_broken_rail.sizePolicy().hasHeightForWidth())
        self.set_broken_rail.setSizePolicy(sizePolicy)
        self.set_broken_rail.setMinimumSize(QSize(221, 23))
        self.set_broken_rail.setStyleSheet(u"background-color: rgb(white);")

        self.gridLayout_3.addWidget(self.set_broken_rail, 1, 1, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"QGroupBox {\n"
"    background-color: white;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(self.groupBox_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton_1210 = QPushButton(self.groupBox_7)
        self.pushButton_1210.setObjectName(u"pushButton_1210")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_1210.sizePolicy().hasHeightForWidth())
        self.pushButton_1210.setSizePolicy(sizePolicy4)
        self.pushButton_1210.setFocusPolicy(Qt.NoFocus)
        self.pushButton_1210.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"		 background-color: grey;\n"
"    }\n"
"\"\"\")\n"
"")
        self.pushButton_1210.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.pushButton_1210, 0, 0, 1, 1)

        self.label_151 = QLabel(self.groupBox_7)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setStyleSheet(u"background-color: white\n"
"")

        self.gridLayout_2.addWidget(self.label_151, 0, 1, 1, 1)

        self.pushButton_1211 = QPushButton(self.groupBox_7)
        self.pushButton_1211.setObjectName(u"pushButton_1211")
        sizePolicy4.setHeightForWidth(self.pushButton_1211.sizePolicy().hasHeightForWidth())
        self.pushButton_1211.setSizePolicy(sizePolicy4)
        self.pushButton_1211.setFocusPolicy(Qt.NoFocus)
        self.pushButton_1211.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"		 background-color: yellow;\n"
"    }\n"
"\"\"\")\n"
"")
        self.pushButton_1211.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.pushButton_1211, 1, 0, 1, 1)

        self.label_152 = QLabel(self.groupBox_7)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setStyleSheet(u"background-color: white\n"
"")

        self.gridLayout_2.addWidget(self.label_152, 1, 1, 1, 1)

        self.pushButton_1212 = QPushButton(self.groupBox_7)
        self.pushButton_1212.setObjectName(u"pushButton_1212")
        sizePolicy4.setHeightForWidth(self.pushButton_1212.sizePolicy().hasHeightForWidth())
        self.pushButton_1212.setSizePolicy(sizePolicy4)
        self.pushButton_1212.setFocusPolicy(Qt.NoFocus)
        self.pushButton_1212.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"		 background-color: tan;\n"
"    }\n"
"\"\"\")\n"
"")
        self.pushButton_1212.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.pushButton_1212, 2, 0, 1, 1)

        self.label_153 = QLabel(self.groupBox_7)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setStyleSheet(u"background-color: white\n"
"")

        self.gridLayout_2.addWidget(self.label_153, 2, 1, 1, 1)

        self.pushButton_1213 = QPushButton(self.groupBox_7)
        self.pushButton_1213.setObjectName(u"pushButton_1213")
        sizePolicy4.setHeightForWidth(self.pushButton_1213.sizePolicy().hasHeightForWidth())
        self.pushButton_1213.setSizePolicy(sizePolicy4)
        self.pushButton_1213.setFocusPolicy(Qt.NoFocus)
        self.pushButton_1213.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"		 background-color: orange;\n"
"    }\n"
"\"\"\")\n"
"")
        self.pushButton_1213.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.pushButton_1213, 3, 0, 1, 1)

        self.label_154 = QLabel(self.groupBox_7)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setStyleSheet(u"background-color: white\n"
"")

        self.gridLayout_2.addWidget(self.label_154, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_7, 0, 2, 4, 1)


        self.gridLayout_5.addWidget(self.groupBox, 5, 0, 1, 2)

        self.clock_in = QLCDNumber(self.centralwidget)
        self.clock_in.setObjectName(u"clock_in")

        self.gridLayout_5.addWidget(self.clock_in, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"background-color : rgb(38, 207, 4)")
        icon3 = QIcon()
        icon3.addFile(u"974868-200.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)

        self.gridLayout_5.addWidget(self.pushButton, 0, 1, 1, 1)

        self.green_line = QGroupBox(self.centralwidget)
        self.green_line.setObjectName(u"green_line")
        self.green_line.setEnabled(True)
        sizePolicy.setHeightForWidth(self.green_line.sizePolicy().hasHeightForWidth())
        self.green_line.setSizePolicy(sizePolicy)
        self.green_line.setMinimumSize(QSize(560, 450))
        self.green_line.setMaximumSize(QSize(16777215, 450))
        self.gridLayout_4 = QGridLayout(self.green_line)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.K68 = QPushButton(self.green_line)
        self.K68.setObjectName(u"K68")
        self.K68.setMinimumSize(QSize(10, 10))
        self.K68.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.K68, 32, 50, 2, 1)

        self.E17 = QPushButton(self.green_line)
        self.E17.setObjectName(u"E17")
        self.E17.setMinimumSize(QSize(10, 10))
        self.E17.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.E17, 0, 8, 1, 2)

        self.W132 = QPushButton(self.green_line)
        self.W132.setObjectName(u"W132")
        self.W132.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W132, 22, 16, 2, 2)

        self.Q99 = QPushButton(self.green_line)
        self.Q99.setObjectName(u"Q99")
        self.Q99.setMinimumSize(QSize(10, 10))
        self.Q99.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.Q99, 37, 11, 2, 2)

        self.F26 = QPushButton(self.green_line)
        self.F26.setObjectName(u"F26")
        self.F26.setMinimumSize(QSize(10, 10))
        self.F26.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.F26, 9, 2, 1, 1)

        self.K63 = QPushButton(self.green_line)
        self.K63.setObjectName(u"K63")
        self.K63.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.K63, 24, 50, 1, 1)

        self.N78 = QPushButton(self.green_line)
        self.N78.setObjectName(u"N78")
        self.N78.setMinimumSize(QSize(10, 10))
        self.N78.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.N78, 40, 27, 1, 2)

        self.W133 = QPushButton(self.green_line)
        self.W133.setObjectName(u"W133")
        self.W133.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W133, 22, 14, 2, 2)

        self.G30 = QPushButton(self.green_line)
        self.G30.setObjectName(u"G30")
        self.G30.setMinimumSize(QSize(10, 10))
        self.G30.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.G30, 14, 2, 2, 1)

        self.W130 = QPushButton(self.green_line)
        self.W130.setObjectName(u"W130")
        self.W130.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W130, 22, 20, 2, 2)

        self.L73 = QPushButton(self.green_line)
        self.L73.setObjectName(u"L73")
        self.L73.setMinimumSize(QSize(10, 10))
        self.L73.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.L73, 40, 41, 1, 2)

        self.N84 = QPushButton(self.green_line)
        self.N84.setObjectName(u"N84")
        self.N84.setMinimumSize(QSize(10, 10))
        self.N84.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.N84, 40, 15, 1, 2)

        self.F22 = QPushButton(self.green_line)
        self.F22.setObjectName(u"F22")
        self.F22.setMinimumSize(QSize(10, 10))
        self.F22.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.F22, 4, 2, 2, 1)

        self.Q100 = QPushButton(self.green_line)
        self.Q100.setObjectName(u"Q100")
        self.Q100.setMinimumSize(QSize(10, 10))
        self.Q100.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.Q100, 39, 12, 1, 1)

        self.N79 = QPushButton(self.green_line)
        self.N79.setObjectName(u"N79")
        self.N79.setMinimumSize(QSize(10, 10))
        self.N79.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.N79, 40, 25, 1, 2)

        self.L69 = QPushButton(self.green_line)
        self.L69.setObjectName(u"L69")
        self.L69.setMinimumSize(QSize(10, 10))
        self.L69.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.L69, 34, 50, 2, 1)

        self.U110 = QPushButton(self.green_line)
        self.U110.setObjectName(u"U110")
        self.U110.setMinimumSize(QSize(10, 10))
        self.U110.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.U110, 33, 47, 2, 2)

        self.U113 = QPushButton(self.green_line)
        self.U113.setObjectName(u"U113")
        self.U113.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.U113, 27, 47, 2, 2)

        self.P96 = QPushButton(self.green_line)
        self.P96.setObjectName(u"P96")
        self.P96.setMinimumSize(QSize(10, 10))
        self.P96.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.P96, 31, 9, 2, 2)

        self.B6 = QPushButton(self.green_line)
        self.B6.setObjectName(u"B6")
        self.B6.setMinimumSize(QSize(10, 10))
        self.B6.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.B6, 5, 33, 2, 2)

        self.Y149 = QPushButton(self.green_line)
        self.Y149.setObjectName(u"Y149")
        self.Y149.setMinimumSize(QSize(10, 10))
        self.Y149.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.Y149, 13, 0, 2, 1)

        self.N77 = QPushButton(self.green_line)
        self.N77.setObjectName(u"N77")
        self.N77.setMinimumSize(QSize(10, 10))
        self.N77.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.N77, 40, 30, 1, 2)

        self.O88 = QPushButton(self.green_line)
        self.O88.setObjectName(u"O88")
        self.O88.setMinimumSize(QSize(10, 10))
        self.O88.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.O88, 40, 8, 1, 2)

        self.W135 = QPushButton(self.green_line)
        self.W135.setObjectName(u"W135")
        self.W135.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W135, 22, 12, 2, 1)

        self.Z150 = QPushButton(self.green_line)
        self.Z150.setObjectName(u"Z150")
        self.Z150.setMinimumSize(QSize(10, 10))
        self.Z150.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.Z150, 11, 1, 2, 1)

        self.R101 = QPushButton(self.green_line)
        self.R101.setObjectName(u"R101")
        self.R101.setMinimumSize(QSize(10, 10))
        self.R101.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.R101, 39, 31, 1, 2)

        self.N80 = QPushButton(self.green_line)
        self.N80.setObjectName(u"N80")
        self.N80.setMinimumSize(QSize(10, 10))
        self.N80.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.N80, 40, 23, 1, 2)

        self.S103 = QPushButton(self.green_line)
        self.S103.setObjectName(u"S103")
        self.S103.setMinimumSize(QSize(10, 10))
        self.S103.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.S103, 38, 35, 2, 2)

        self.T107 = QPushButton(self.green_line)
        self.T107.setObjectName(u"T107")
        self.T107.setMinimumSize(QSize(10, 10))
        self.T107.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.T107, 38, 43, 2, 2)

        self.K66 = QPushButton(self.green_line)
        self.K66.setObjectName(u"K66")
        self.K66.setMinimumSize(QSize(10, 10))
        self.K66.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.K66, 28, 50, 2, 1)

        self.D16 = QPushButton(self.green_line)
        self.D16.setObjectName(u"D16")
        self.D16.setMinimumSize(QSize(10, 10))
        self.D16.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.D16, 0, 11, 1, 2)

        self.Q98 = QPushButton(self.green_line)
        self.Q98.setObjectName(u"Q98")
        self.Q98.setMinimumSize(QSize(10, 10))
        self.Q98.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.Q98, 35, 10, 2, 2)

        self.E19 = QPushButton(self.green_line)
        self.E19.setObjectName(u"E19")
        self.E19.setMinimumSize(QSize(10, 10))
        self.E19.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.E19, 0, 3, 1, 2)

        self.P95 = QPushButton(self.green_line)
        self.P95.setObjectName(u"P95")
        self.P95.setMinimumSize(QSize(10, 10))
        self.P95.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.P95, 30, 7, 2, 2)

        self.F21 = QPushButton(self.green_line)
        self.F21.setObjectName(u"F21")
        self.F21.setMinimumSize(QSize(10, 10))
        self.F21.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.F21, 2, 2, 2, 1)

        self.D14 = QPushButton(self.green_line)
        self.D14.setObjectName(u"D14")
        self.D14.setMinimumSize(QSize(10, 10))
        self.D14.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.D14, 0, 17, 1, 2)

        self.B4 = QPushButton(self.green_line)
        self.B4.setObjectName(u"B4")
        self.B4.setMinimumSize(QSize(10, 10))
        self.B4.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.B4, 4, 29, 2, 2)

        self.E20 = QPushButton(self.green_line)
        self.E20.setObjectName(u"E20")
        self.E20.setMinimumSize(QSize(10, 10))
        self.E20.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.E20, 1, 2, 1, 1)

        self.W136 = QPushButton(self.green_line)
        self.W136.setObjectName(u"W136")
        self.W136.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W136, 22, 10, 2, 2)

        self.Y148 = QPushButton(self.green_line)
        self.Y148.setObjectName(u"Y148")
        self.Y148.setMinimumSize(QSize(10, 10))
        self.Y148.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.Y148, 15, 0, 2, 1)

        self.N83 = QPushButton(self.green_line)
        self.N83.setObjectName(u"N83")
        self.N83.setMinimumSize(QSize(10, 10))
        self.N83.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.N83, 40, 17, 1, 2)

        self.M76 = QPushButton(self.green_line)
        self.M76.setObjectName(u"M76")
        self.M76.setMinimumSize(QSize(10, 10))
        self.M76.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.M76, 40, 33, 1, 2)

        self.T105 = QPushButton(self.green_line)
        self.T105.setObjectName(u"T105")
        self.T105.setMinimumSize(QSize(10, 10))
        self.T105.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.T105, 38, 40, 2, 1)

        self.P92 = QPushButton(self.green_line)
        self.P92.setObjectName(u"P92")
        self.P92.setMinimumSize(QSize(10, 10))
        self.P92.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.P92, 35, 5, 2, 1)

        self.U111 = QPushButton(self.green_line)
        self.U111.setObjectName(u"U111")
        self.U111.setMinimumSize(QSize(10, 10))
        self.U111.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.U111, 31, 47, 2, 2)

        self.W137 = QPushButton(self.green_line)
        self.W137.setObjectName(u"W137")
        self.W137.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W137, 22, 8, 2, 2)

        self.N81 = QPushButton(self.green_line)
        self.N81.setObjectName(u"N81")
        self.N81.setMinimumSize(QSize(10, 10))
        self.N81.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.N81, 40, 21, 1, 2)

        self.G31 = QPushButton(self.green_line)
        self.G31.setObjectName(u"G31")
        self.G31.setMinimumSize(QSize(10, 10))
        self.G31.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.G31, 16, 2, 2, 1)

        self.O87 = QPushButton(self.green_line)
        self.O87.setObjectName(u"O87")
        self.O87.setMinimumSize(QSize(10, 10))
        self.O87.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.O87, 40, 10, 1, 2)

        self.S104 = QPushButton(self.green_line)
        self.S104.setObjectName(u"S104")
        self.S104.setMinimumSize(QSize(10, 10))
        self.S104.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.S104, 38, 38, 2, 2)

        self.P93 = QPushButton(self.green_line)
        self.P93.setObjectName(u"P93")
        self.P93.setMinimumSize(QSize(10, 10))
        self.P93.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.P93, 33, 5, 2, 1)

        self.A1 = QPushButton(self.green_line)
        self.A1.setObjectName(u"A1")
        self.A1.setMinimumSize(QSize(10, 10))
        self.A1.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.A1, 1, 25, 1, 2)

        self.L70 = QPushButton(self.green_line)
        self.L70.setObjectName(u"L70")
        self.L70.setMinimumSize(QSize(10, 10))
        self.L70.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.L70, 36, 50, 2, 1)

        self.F27 = QPushButton(self.green_line)
        self.F27.setObjectName(u"F27")
        self.F27.setMinimumSize(QSize(10, 10))
        self.F27.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.F27, 10, 2, 1, 1)

        self.K67 = QPushButton(self.green_line)
        self.K67.setObjectName(u"K67")
        self.K67.setMinimumSize(QSize(10, 10))
        self.K67.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.K67, 30, 50, 2, 1)

        self.D13 = QPushButton(self.green_line)
        self.D13.setObjectName(u"D13")
        self.D13.setMinimumSize(QSize(10, 10))
        self.D13.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.D13, 0, 21, 1, 2)

        self.F24 = QPushButton(self.green_line)
        self.F24.setObjectName(u"F24")
        self.F24.setMinimumSize(QSize(10, 10))
        self.F24.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.F24, 7, 2, 1, 1)

        self.Y147 = QPushButton(self.green_line)
        self.Y147.setObjectName(u"Y147")
        self.Y147.setMinimumSize(QSize(10, 10))
        self.Y147.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.Y147, 17, 0, 2, 1)

        self.D15 = QPushButton(self.green_line)
        self.D15.setObjectName(u"D15")
        self.D15.setMinimumSize(QSize(10, 10))
        self.D15.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.D15, 0, 13, 1, 2)

        self.L72 = QPushButton(self.green_line)
        self.L72.setObjectName(u"L72")
        self.L72.setMinimumSize(QSize(10, 10))
        self.L72.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.L72, 40, 46, 1, 2)

        self.W134 = QPushButton(self.green_line)
        self.W134.setObjectName(u"W134")
        self.W134.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W134, 22, 13, 2, 1)

        self.W131 = QPushButton(self.green_line)
        self.W131.setObjectName(u"W131")
        self.W131.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W131, 22, 18, 2, 2)

        self.T106 = QPushButton(self.green_line)
        self.T106.setObjectName(u"T106")
        self.T106.setMinimumSize(QSize(10, 10))
        self.T106.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.T106, 38, 41, 2, 1)

        self.K64 = QPushButton(self.green_line)
        self.K64.setObjectName(u"K64")
        self.K64.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.K64, 25, 50, 1, 1)

        self.C11 = QPushButton(self.green_line)
        self.C11.setObjectName(u"C11")
        self.C11.setMinimumSize(QSize(10, 10))
        self.C11.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.C11, 0, 28, 2, 2)

        self.K65 = QPushButton(self.green_line)
        self.K65.setObjectName(u"K65")
        self.K65.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.K65, 26, 50, 2, 1)

        self.E18 = QPushButton(self.green_line)
        self.E18.setObjectName(u"E18")
        self.E18.setMinimumSize(QSize(10, 10))
        self.E18.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.E18, 0, 5, 1, 1)

        self.P91 = QPushButton(self.green_line)
        self.P91.setObjectName(u"P91")
        self.P91.setMinimumSize(QSize(10, 10))
        self.P91.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.P91, 37, 5, 2, 1)

        self.C9 = QPushButton(self.green_line)
        self.C9.setObjectName(u"C9")
        self.C9.setMinimumSize(QSize(10, 10))
        self.C9.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.C9, 2, 35, 1, 2)

        self.W138 = QPushButton(self.green_line)
        self.W138.setObjectName(u"W138")
        self.W138.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W138, 22, 6, 2, 2)

        self.P90 = QPushButton(self.green_line)
        self.P90.setObjectName(u"P90")
        self.P90.setMinimumSize(QSize(10, 10))
        self.P90.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.P90, 39, 5, 1, 2)

        self.G32 = QPushButton(self.green_line)
        self.G32.setObjectName(u"G32")
        self.G32.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.G32, 18, 2, 2, 1)

        self.C7 = QPushButton(self.green_line)
        self.C7.setObjectName(u"C7")
        self.C7.setMinimumSize(QSize(10, 10))
        self.C7.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.C7, 5, 35, 2, 2)

        self.F23 = QPushButton(self.green_line)
        self.F23.setObjectName(u"F23")
        self.F23.setMinimumSize(QSize(10, 10))
        self.F23.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.F23, 6, 2, 1, 1)

        self.M74 = QPushButton(self.green_line)
        self.M74.setObjectName(u"M74")
        self.M74.setMinimumSize(QSize(10, 10))
        self.M74.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.M74, 40, 39, 1, 2)

        self.M75 = QPushButton(self.green_line)
        self.M75.setObjectName(u"M75")
        self.M75.setMinimumSize(QSize(10, 10))
        self.M75.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.M75, 40, 36, 1, 2)

        self.T108 = QPushButton(self.green_line)
        self.T108.setObjectName(u"T108")
        self.T108.setMinimumSize(QSize(10, 10))
        self.T108.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.T108, 37, 45, 2, 2)

        self.T109 = QPushButton(self.green_line)
        self.T109.setObjectName(u"T109")
        self.T109.setMinimumSize(QSize(10, 10))
        self.T109.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.T109, 35, 46, 2, 2)

        self.B5 = QPushButton(self.green_line)
        self.B5.setObjectName(u"B5")
        self.B5.setMinimumSize(QSize(10, 10))
        self.B5.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.B5, 5, 31, 2, 2)

        self.P94 = QPushButton(self.green_line)
        self.P94.setObjectName(u"P94")
        self.P94.setMinimumSize(QSize(10, 10))
        self.P94.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.P94, 31, 5, 2, 1)

        self.F28 = QPushButton(self.green_line)
        self.F28.setObjectName(u"F28")
        self.F28.setMinimumSize(QSize(10, 10))
        self.F28.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.F28, 11, 2, 1, 1)

        self.N82 = QPushButton(self.green_line)
        self.N82.setObjectName(u"N82")
        self.N82.setMinimumSize(QSize(10, 10))
        self.N82.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.N82, 40, 19, 1, 2)

        self.G29 = QPushButton(self.green_line)
        self.G29.setObjectName(u"G29")
        self.G29.setMinimumSize(QSize(10, 10))
        self.G29.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.G29, 12, 2, 2, 1)

        self.A3 = QPushButton(self.green_line)
        self.A3.setObjectName(u"A3")
        self.A3.setMinimumSize(QSize(10, 10))
        self.A3.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.A3, 3, 27, 2, 2)

        self.N85 = QPushButton(self.green_line)
        self.N85.setObjectName(u"N85")
        self.N85.setMinimumSize(QSize(10, 10))
        self.N85.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.N85, 40, 13, 1, 2)

        self.O86 = QPushButton(self.green_line)
        self.O86.setObjectName(u"O86")
        self.O86.setMinimumSize(QSize(10, 10))
        self.O86.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.O86, 40, 12, 1, 1)

        self.X146 = QPushButton(self.green_line)
        self.X146.setObjectName(u"X146")
        self.X146.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.X146, 19, 0, 2, 1)

        self.P97 = QPushButton(self.green_line)
        self.P97.setObjectName(u"P97")
        self.P97.setMinimumSize(QSize(10, 10))
        self.P97.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.P97, 33, 9, 2, 2)

        self.C8 = QPushButton(self.green_line)
        self.C8.setObjectName(u"C8")
        self.C8.setMinimumSize(QSize(10, 10))
        self.C8.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.C8, 3, 36, 2, 2)

        self.U114 = QPushButton(self.green_line)
        self.U114.setObjectName(u"U114")
        self.U114.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.U114, 25, 47, 2, 2)

        self.S102 = QPushButton(self.green_line)
        self.S102.setObjectName(u"S102")
        self.S102.setMinimumSize(QSize(10, 10))
        self.S102.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.S102, 38, 33, 2, 2)

        self.U112 = QPushButton(self.green_line)
        self.U112.setObjectName(u"U112")
        self.U112.setMinimumSize(QSize(10, 10))
        self.U112.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.U112, 29, 47, 2, 2)

        self.C10 = QPushButton(self.green_line)
        self.C10.setObjectName(u"C10")
        self.C10.setMinimumSize(QSize(10, 10))
        self.C10.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.C10, 1, 32, 1, 2)

        self.C12 = QPushButton(self.green_line)
        self.C12.setObjectName(u"C12")
        self.C12.setMinimumSize(QSize(10, 10))
        self.C12.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.C12, 0, 25, 1, 2)

        self.P89 = QPushButton(self.green_line)
        self.P89.setObjectName(u"P89")
        self.P89.setMinimumSize(QSize(10, 10))
        self.P89.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.P89, 40, 6, 1, 2)

        self.X145 = QPushButton(self.green_line)
        self.X145.setObjectName(u"X145")
        self.X145.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.X145, 21, 0, 1, 1)

        self.F25 = QPushButton(self.green_line)
        self.F25.setObjectName(u"F25")
        self.F25.setMinimumSize(QSize(10, 10))
        self.F25.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.F25, 8, 2, 1, 1)

        self.H33 = QPushButton(self.green_line)
        self.H33.setObjectName(u"H33")
        self.H33.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.H33, 20, 2, 2, 1)

        self.A2 = QPushButton(self.green_line)
        self.A2.setObjectName(u"A2")
        self.A2.setMinimumSize(QSize(10, 10))
        self.A2.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.A2, 2, 26, 1, 2)

        self.L71 = QPushButton(self.green_line)
        self.L71.setObjectName(u"L71")
        self.L71.setMinimumSize(QSize(10, 10))
        self.L71.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.L71, 39, 49, 1, 2)

        self.W139 = QPushButton(self.green_line)
        self.W139.setObjectName(u"W139")
        self.W139.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W139, 22, 5, 2, 1)

        self.W140 = QPushButton(self.green_line)
        self.W140.setObjectName(u"W140")
        self.W140.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W140, 22, 4, 2, 1)

        self.W141 = QPushButton(self.green_line)
        self.W141.setObjectName(u"W141")
        self.W141.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W141, 22, 3, 2, 1)

        self.W142 = QPushButton(self.green_line)
        self.W142.setObjectName(u"W142")
        self.W142.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W142, 22, 2, 2, 1)

        self.W143 = QPushButton(self.green_line)
        self.W143.setObjectName(u"W143")
        self.W143.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W143, 22, 1, 2, 1)

        self.X144 = QPushButton(self.green_line)
        self.X144.setObjectName(u"X144")
        self.X144.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.X144, 22, 0, 2, 1)

        self.H34 = QPushButton(self.green_line)
        self.H34.setObjectName(u"H34")
        self.H34.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.H34, 20, 3, 2, 1)

        self.H35 = QPushButton(self.green_line)
        self.H35.setObjectName(u"H35")
        self.H35.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.H35, 20, 4, 2, 1)

        self.I36 = QPushButton(self.green_line)
        self.I36.setObjectName(u"I36")
        self.I36.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I36, 20, 5, 2, 1)

        self.I37 = QPushButton(self.green_line)
        self.I37.setObjectName(u"I37")
        self.I37.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I37, 20, 6, 2, 2)

        self.I38 = QPushButton(self.green_line)
        self.I38.setObjectName(u"I38")
        self.I38.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I38, 20, 8, 2, 2)

        self.I39 = QPushButton(self.green_line)
        self.I39.setObjectName(u"I39")
        self.I39.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I39, 20, 10, 2, 2)

        self.I40 = QPushButton(self.green_line)
        self.I40.setObjectName(u"I40")
        self.I40.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I40, 20, 12, 2, 1)

        self.I41 = QPushButton(self.green_line)
        self.I41.setObjectName(u"I41")
        self.I41.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I41, 20, 13, 2, 1)

        self.I42 = QPushButton(self.green_line)
        self.I42.setObjectName(u"I42")
        self.I42.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I42, 20, 14, 2, 2)

        self.I43 = QPushButton(self.green_line)
        self.I43.setObjectName(u"I43")
        self.I43.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I43, 20, 16, 2, 2)

        self.I44 = QPushButton(self.green_line)
        self.I44.setObjectName(u"I44")
        self.I44.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I44, 20, 18, 2, 2)

        self.I45 = QPushButton(self.green_line)
        self.I45.setObjectName(u"I45")
        self.I45.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I45, 20, 20, 2, 2)

        self.I46 = QPushButton(self.green_line)
        self.I46.setObjectName(u"I46")
        self.I46.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I46, 20, 22, 2, 2)

        self.W129 = QPushButton(self.green_line)
        self.W129.setObjectName(u"W129")
        self.W129.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W129, 22, 22, 2, 2)

        self.I47 = QPushButton(self.green_line)
        self.I47.setObjectName(u"I47")
        self.I47.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I47, 20, 24, 2, 2)

        self.I48 = QPushButton(self.green_line)
        self.I48.setObjectName(u"I48")
        self.I48.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I48, 20, 26, 2, 2)

        self.W128 = QPushButton(self.green_line)
        self.W128.setObjectName(u"W128")
        self.W128.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W128, 22, 24, 2, 2)

        self.W127 = QPushButton(self.green_line)
        self.W127.setObjectName(u"W127")
        self.W127.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W127, 22, 26, 2, 2)

        self.I49 = QPushButton(self.green_line)
        self.I49.setObjectName(u"I49")
        self.I49.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I49, 20, 28, 2, 2)

        self.W126 = QPushButton(self.green_line)
        self.W126.setObjectName(u"W126")
        self.W126.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W126, 22, 28, 2, 2)

        self.I50 = QPushButton(self.green_line)
        self.I50.setObjectName(u"I50")
        self.I50.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I50, 20, 30, 2, 2)

        self.I51 = QPushButton(self.green_line)
        self.I51.setObjectName(u"I51")
        self.I51.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I51, 20, 32, 2, 2)

        self.W125 = QPushButton(self.green_line)
        self.W125.setObjectName(u"W125")
        self.W125.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W125, 22, 30, 2, 2)

        self.W124 = QPushButton(self.green_line)
        self.W124.setObjectName(u"W124")
        self.W124.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W124, 22, 32, 2, 2)

        self.W123 = QPushButton(self.green_line)
        self.W123.setObjectName(u"W123")
        self.W123.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W123, 22, 34, 2, 2)

        self.I52 = QPushButton(self.green_line)
        self.I52.setObjectName(u"I52")
        self.I52.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I52, 20, 34, 2, 2)

        self.I53 = QPushButton(self.green_line)
        self.I53.setObjectName(u"I53")
        self.I53.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I53, 20, 36, 2, 2)

        self.I54 = QPushButton(self.green_line)
        self.I54.setObjectName(u"I54")
        self.I54.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I54, 20, 38, 2, 2)

        self.W122 = QPushButton(self.green_line)
        self.W122.setObjectName(u"W122")
        self.W122.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.W122, 22, 37, 2, 2)

        self.I55 = QPushButton(self.green_line)
        self.I55.setObjectName(u"I55")
        self.I55.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I55, 20, 40, 2, 1)

        self.V121 = QPushButton(self.green_line)
        self.V121.setObjectName(u"V121")
        self.V121.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.V121, 22, 40, 2, 1)

        self.I56 = QPushButton(self.green_line)
        self.I56.setObjectName(u"I56")
        self.I56.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I56, 20, 41, 2, 1)

        self.I57 = QPushButton(self.green_line)
        self.I57.setObjectName(u"I57")
        self.I57.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.I57, 20, 42, 2, 2)

        self.J58 = QPushButton(self.green_line)
        self.J58.setObjectName(u"J58")
        self.J58.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.J58, 20, 44, 2, 2)

        self.J59 = QPushButton(self.green_line)
        self.J59.setObjectName(u"J59")
        self.J59.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.J59, 20, 46, 2, 2)

        self.V120 = QPushButton(self.green_line)
        self.V120.setObjectName(u"V120")
        self.V120.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.V120, 22, 41, 2, 1)

        self.V119 = QPushButton(self.green_line)
        self.V119.setObjectName(u"V119")
        self.V119.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.V119, 22, 42, 2, 2)

        self.V118 = QPushButton(self.green_line)
        self.V118.setObjectName(u"V118")
        self.V118.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.V118, 22, 44, 2, 2)

        self.J62 = QPushButton(self.green_line)
        self.J62.setObjectName(u"J62")
        self.J62.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.J62, 22, 50, 2, 1)

        self.J61 = QPushButton(self.green_line)
        self.J61.setObjectName(u"J61")
        self.J61.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.J61, 21, 49, 2, 1)

        self.V117 = QPushButton(self.green_line)
        self.V117.setObjectName(u"V117")
        self.V117.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.V117, 22, 46, 2, 1)

        self.U116 = QPushButton(self.green_line)
        self.U116.setObjectName(u"U116")
        sizePolicy.setHeightForWidth(self.U116.sizePolicy().hasHeightForWidth())
        self.U116.setSizePolicy(sizePolicy)
        self.U116.setMaximumSize(QSize(10, 10))
        self.U116.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.U116, 23, 48, 1, 1)

        self.U115 = QPushButton(self.green_line)
        self.U115.setObjectName(u"U115")
        sizePolicy.setHeightForWidth(self.U115.sizePolicy().hasHeightForWidth())
        self.U115.setSizePolicy(sizePolicy)
        self.U115.setMinimumSize(QSize(10, 2))
        self.U115.setMaximumSize(QSize(10, 10))
        self.U115.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.U115, 24, 48, 1, 1)

        self.J60 = QPushButton(self.green_line)
        self.J60.setObjectName(u"J60")
        self.J60.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: rgb(50,205,50)\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.J60, 20, 48, 2, 1)

        self.Y = QPushButton(self.green_line)
        self.Y.setObjectName(u"Y")
        self.Y.setStyleSheet(u"\n"
"    QPushButton {\n"
"        border-style: solid;\n"
"        border-width: 0.5px;\n"
"        border-color: black;\n"
"		 background-color: white\n"
"    }\n"
"\"\"\")\n"
"")

        self.gridLayout_4.addWidget(self.Y, 16, 45, 2, 4)


        self.gridLayout_5.addWidget(self.green_line, 2, 0, 2, 2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(200, 140))
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    background-color: white;\n"
"}\n"
"")
        self.gridLayout_36 = QGridLayout(self.groupBox_3)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_127 = QLabel(self.groupBox_3)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setStyleSheet(u"background-color: rgb(white);")
        self.label_127.setFrameShape(QFrame.NoFrame)

        self.gridLayout_36.addWidget(self.label_127, 1, 0, 1, 1)

        self.disembarking_out = QLabel(self.groupBox_3)
        self.disembarking_out.setObjectName(u"disembarking_out")
        self.disembarking_out.setStyleSheet(u"background-color: rgb(white);")
        self.disembarking_out.setFrameShape(QFrame.Box)

        self.gridLayout_36.addWidget(self.disembarking_out, 3, 1, 1, 1)

        self.station_in = QLabel(self.groupBox_3)
        self.station_in.setObjectName(u"station_in")
        self.station_in.setStyleSheet(u"background-color: rgb(white);")
        self.station_in.setFrameShape(QFrame.Box)

        self.gridLayout_36.addWidget(self.station_in, 0, 1, 1, 1)

        self.label_128 = QLabel(self.groupBox_3)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setStyleSheet(u"background-color: rgb(white);")
        self.label_128.setFrameShape(QFrame.NoFrame)

        self.gridLayout_36.addWidget(self.label_128, 2, 0, 1, 1)

        self.boarding_out = QLabel(self.groupBox_3)
        self.boarding_out.setObjectName(u"boarding_out")
        self.boarding_out.setStyleSheet(u"background-color: rgb(white);")
        self.boarding_out.setFrameShape(QFrame.Box)

        self.gridLayout_36.addWidget(self.boarding_out, 2, 1, 1, 1)

        self.label_126 = QLabel(self.groupBox_3)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setStyleSheet(u"background-color: rgb(white);")
        self.label_126.setFrameShape(QFrame.NoFrame)

        self.gridLayout_36.addWidget(self.label_126, 0, 0, 1, 1)

        self.ticket_out = QLabel(self.groupBox_3)
        self.ticket_out.setObjectName(u"ticket_out")
        self.ticket_out.setStyleSheet(u"background-color: rgb(white);")
        self.ticket_out.setFrameShape(QFrame.Box)

        self.gridLayout_36.addWidget(self.ticket_out, 1, 1, 1, 1)

        self.label_129 = QLabel(self.groupBox_3)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setStyleSheet(u"background-color: rgb(white);")
        self.label_129.setFrameShape(QFrame.NoFrame)

        self.gridLayout_36.addWidget(self.label_129, 3, 0, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_3, 3, 2, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.line_select.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Line", None))
        self.line_select.setItemText(1, QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.line_select.setItemText(2, QCoreApplication.translate("MainWindow", u"Red Line", None))

        self.block_in_1.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Block", None))
        self.block_in_1.setItemText(1, QCoreApplication.translate("MainWindow", u"Y0", None))
        self.block_in_1.setItemText(2, QCoreApplication.translate("MainWindow", u"Y1", None))
        self.block_in_1.setItemText(3, QCoreApplication.translate("MainWindow", u"Y2", None))
        self.block_in_1.setItemText(4, QCoreApplication.translate("MainWindow", u"A1", None))
        self.block_in_1.setItemText(5, QCoreApplication.translate("MainWindow", u"A2", None))
        self.block_in_1.setItemText(6, QCoreApplication.translate("MainWindow", u"A3", None))
        self.block_in_1.setItemText(7, QCoreApplication.translate("MainWindow", u"B4", None))
        self.block_in_1.setItemText(8, QCoreApplication.translate("MainWindow", u"B5", None))
        self.block_in_1.setItemText(9, QCoreApplication.translate("MainWindow", u"B6", None))
        self.block_in_1.setItemText(10, QCoreApplication.translate("MainWindow", u"C7", None))
        self.block_in_1.setItemText(11, QCoreApplication.translate("MainWindow", u"C8", None))
        self.block_in_1.setItemText(12, QCoreApplication.translate("MainWindow", u"C9", None))
        self.block_in_1.setItemText(13, QCoreApplication.translate("MainWindow", u"C10", None))
        self.block_in_1.setItemText(14, QCoreApplication.translate("MainWindow", u"C11", None))
        self.block_in_1.setItemText(15, QCoreApplication.translate("MainWindow", u"C12", None))
        self.block_in_1.setItemText(16, QCoreApplication.translate("MainWindow", u"D13", None))
        self.block_in_1.setItemText(17, QCoreApplication.translate("MainWindow", u"D14", None))
        self.block_in_1.setItemText(18, QCoreApplication.translate("MainWindow", u"D15", None))
        self.block_in_1.setItemText(19, QCoreApplication.translate("MainWindow", u"D16", None))
        self.block_in_1.setItemText(20, QCoreApplication.translate("MainWindow", u"E17", None))
        self.block_in_1.setItemText(21, QCoreApplication.translate("MainWindow", u"E18", None))
        self.block_in_1.setItemText(22, QCoreApplication.translate("MainWindow", u"E19", None))
        self.block_in_1.setItemText(23, QCoreApplication.translate("MainWindow", u"E20", None))
        self.block_in_1.setItemText(24, QCoreApplication.translate("MainWindow", u"F21", None))
        self.block_in_1.setItemText(25, QCoreApplication.translate("MainWindow", u"F22", None))
        self.block_in_1.setItemText(26, QCoreApplication.translate("MainWindow", u"F23", None))
        self.block_in_1.setItemText(27, QCoreApplication.translate("MainWindow", u"F24", None))
        self.block_in_1.setItemText(28, QCoreApplication.translate("MainWindow", u"F25", None))
        self.block_in_1.setItemText(29, QCoreApplication.translate("MainWindow", u"F26", None))
        self.block_in_1.setItemText(30, QCoreApplication.translate("MainWindow", u"F27", None))
        self.block_in_1.setItemText(31, QCoreApplication.translate("MainWindow", u"F28", None))
        self.block_in_1.setItemText(32, QCoreApplication.translate("MainWindow", u"G29", None))
        self.block_in_1.setItemText(33, QCoreApplication.translate("MainWindow", u"G30", None))
        self.block_in_1.setItemText(34, QCoreApplication.translate("MainWindow", u"G31", None))
        self.block_in_1.setItemText(35, QCoreApplication.translate("MainWindow", u"G32", None))
        self.block_in_1.setItemText(36, QCoreApplication.translate("MainWindow", u"H33", None))
        self.block_in_1.setItemText(37, QCoreApplication.translate("MainWindow", u"H34", None))
        self.block_in_1.setItemText(38, QCoreApplication.translate("MainWindow", u"H35", None))
        self.block_in_1.setItemText(39, QCoreApplication.translate("MainWindow", u"I36", None))
        self.block_in_1.setItemText(40, QCoreApplication.translate("MainWindow", u"I37", None))
        self.block_in_1.setItemText(41, QCoreApplication.translate("MainWindow", u"I38", None))
        self.block_in_1.setItemText(42, QCoreApplication.translate("MainWindow", u"I39", None))
        self.block_in_1.setItemText(43, QCoreApplication.translate("MainWindow", u"I40", None))
        self.block_in_1.setItemText(44, QCoreApplication.translate("MainWindow", u"I41", None))
        self.block_in_1.setItemText(45, QCoreApplication.translate("MainWindow", u"I42", None))
        self.block_in_1.setItemText(46, QCoreApplication.translate("MainWindow", u"I43", None))
        self.block_in_1.setItemText(47, QCoreApplication.translate("MainWindow", u"I44", None))
        self.block_in_1.setItemText(48, QCoreApplication.translate("MainWindow", u"I45", None))
        self.block_in_1.setItemText(49, QCoreApplication.translate("MainWindow", u"I46", None))
        self.block_in_1.setItemText(50, QCoreApplication.translate("MainWindow", u"I47", None))
        self.block_in_1.setItemText(51, QCoreApplication.translate("MainWindow", u"I48", None))
        self.block_in_1.setItemText(52, QCoreApplication.translate("MainWindow", u"I49", None))
        self.block_in_1.setItemText(53, QCoreApplication.translate("MainWindow", u"I50", None))
        self.block_in_1.setItemText(54, QCoreApplication.translate("MainWindow", u"I51", None))
        self.block_in_1.setItemText(55, QCoreApplication.translate("MainWindow", u"I52", None))
        self.block_in_1.setItemText(56, QCoreApplication.translate("MainWindow", u"I53", None))
        self.block_in_1.setItemText(57, QCoreApplication.translate("MainWindow", u"I54", None))
        self.block_in_1.setItemText(58, QCoreApplication.translate("MainWindow", u"I55", None))
        self.block_in_1.setItemText(59, QCoreApplication.translate("MainWindow", u"I56", None))
        self.block_in_1.setItemText(60, QCoreApplication.translate("MainWindow", u"I57", None))
        self.block_in_1.setItemText(61, QCoreApplication.translate("MainWindow", u"J58", None))
        self.block_in_1.setItemText(62, QCoreApplication.translate("MainWindow", u"J59", None))
        self.block_in_1.setItemText(63, QCoreApplication.translate("MainWindow", u"J60", None))
        self.block_in_1.setItemText(64, QCoreApplication.translate("MainWindow", u"J61", None))
        self.block_in_1.setItemText(65, QCoreApplication.translate("MainWindow", u"J62", None))
        self.block_in_1.setItemText(66, QCoreApplication.translate("MainWindow", u"K63", None))
        self.block_in_1.setItemText(67, QCoreApplication.translate("MainWindow", u"K64", None))
        self.block_in_1.setItemText(68, QCoreApplication.translate("MainWindow", u"K65", None))
        self.block_in_1.setItemText(69, QCoreApplication.translate("MainWindow", u"K66", None))
        self.block_in_1.setItemText(70, QCoreApplication.translate("MainWindow", u"K67", None))
        self.block_in_1.setItemText(71, QCoreApplication.translate("MainWindow", u"K68", None))
        self.block_in_1.setItemText(72, QCoreApplication.translate("MainWindow", u"L69", None))
        self.block_in_1.setItemText(73, QCoreApplication.translate("MainWindow", u"L70", None))
        self.block_in_1.setItemText(74, QCoreApplication.translate("MainWindow", u"L71", None))
        self.block_in_1.setItemText(75, QCoreApplication.translate("MainWindow", u"L72", None))
        self.block_in_1.setItemText(76, QCoreApplication.translate("MainWindow", u"L73", None))
        self.block_in_1.setItemText(77, QCoreApplication.translate("MainWindow", u"M74", None))
        self.block_in_1.setItemText(78, QCoreApplication.translate("MainWindow", u"M75", None))
        self.block_in_1.setItemText(79, QCoreApplication.translate("MainWindow", u"M76", None))
        self.block_in_1.setItemText(80, QCoreApplication.translate("MainWindow", u"N77", None))
        self.block_in_1.setItemText(81, QCoreApplication.translate("MainWindow", u"N78", None))
        self.block_in_1.setItemText(82, QCoreApplication.translate("MainWindow", u"N79", None))
        self.block_in_1.setItemText(83, QCoreApplication.translate("MainWindow", u"N80", None))
        self.block_in_1.setItemText(84, QCoreApplication.translate("MainWindow", u"N81", None))
        self.block_in_1.setItemText(85, QCoreApplication.translate("MainWindow", u"N82", None))
        self.block_in_1.setItemText(86, QCoreApplication.translate("MainWindow", u"N83", None))
        self.block_in_1.setItemText(87, QCoreApplication.translate("MainWindow", u"N84", None))
        self.block_in_1.setItemText(88, QCoreApplication.translate("MainWindow", u"N85", None))
        self.block_in_1.setItemText(89, QCoreApplication.translate("MainWindow", u"O86", None))
        self.block_in_1.setItemText(90, QCoreApplication.translate("MainWindow", u"O87", None))
        self.block_in_1.setItemText(91, QCoreApplication.translate("MainWindow", u"O88", None))
        self.block_in_1.setItemText(92, QCoreApplication.translate("MainWindow", u"P89", None))
        self.block_in_1.setItemText(93, QCoreApplication.translate("MainWindow", u"P90", None))
        self.block_in_1.setItemText(94, QCoreApplication.translate("MainWindow", u"P91", None))
        self.block_in_1.setItemText(95, QCoreApplication.translate("MainWindow", u"P92", None))
        self.block_in_1.setItemText(96, QCoreApplication.translate("MainWindow", u"P93", None))
        self.block_in_1.setItemText(97, QCoreApplication.translate("MainWindow", u"P94", None))
        self.block_in_1.setItemText(98, QCoreApplication.translate("MainWindow", u"P95", None))
        self.block_in_1.setItemText(99, QCoreApplication.translate("MainWindow", u"P96", None))
        self.block_in_1.setItemText(100, QCoreApplication.translate("MainWindow", u"P97", None))
        self.block_in_1.setItemText(101, QCoreApplication.translate("MainWindow", u"Q98", None))
        self.block_in_1.setItemText(102, QCoreApplication.translate("MainWindow", u"Q99", None))
        self.block_in_1.setItemText(103, QCoreApplication.translate("MainWindow", u"Q100", None))
        self.block_in_1.setItemText(104, QCoreApplication.translate("MainWindow", u"R101", None))
        self.block_in_1.setItemText(105, QCoreApplication.translate("MainWindow", u"S102", None))
        self.block_in_1.setItemText(106, QCoreApplication.translate("MainWindow", u"S103", None))
        self.block_in_1.setItemText(107, QCoreApplication.translate("MainWindow", u"S104", None))
        self.block_in_1.setItemText(108, QCoreApplication.translate("MainWindow", u"T105", None))
        self.block_in_1.setItemText(109, QCoreApplication.translate("MainWindow", u"T106", None))
        self.block_in_1.setItemText(110, QCoreApplication.translate("MainWindow", u"T107", None))
        self.block_in_1.setItemText(111, QCoreApplication.translate("MainWindow", u"T108", None))
        self.block_in_1.setItemText(112, QCoreApplication.translate("MainWindow", u"T109", None))
        self.block_in_1.setItemText(113, QCoreApplication.translate("MainWindow", u"U110", None))
        self.block_in_1.setItemText(114, QCoreApplication.translate("MainWindow", u"U111", None))
        self.block_in_1.setItemText(115, QCoreApplication.translate("MainWindow", u"U112", None))
        self.block_in_1.setItemText(116, QCoreApplication.translate("MainWindow", u"U113", None))
        self.block_in_1.setItemText(117, QCoreApplication.translate("MainWindow", u"U114", None))
        self.block_in_1.setItemText(118, QCoreApplication.translate("MainWindow", u"U115", None))
        self.block_in_1.setItemText(119, QCoreApplication.translate("MainWindow", u"U116", None))
        self.block_in_1.setItemText(120, QCoreApplication.translate("MainWindow", u"V117", None))
        self.block_in_1.setItemText(121, QCoreApplication.translate("MainWindow", u"V118", None))
        self.block_in_1.setItemText(122, QCoreApplication.translate("MainWindow", u"V119", None))
        self.block_in_1.setItemText(123, QCoreApplication.translate("MainWindow", u"V120", None))
        self.block_in_1.setItemText(124, QCoreApplication.translate("MainWindow", u"V121", None))
        self.block_in_1.setItemText(125, QCoreApplication.translate("MainWindow", u"W122", None))
        self.block_in_1.setItemText(126, QCoreApplication.translate("MainWindow", u"W123", None))
        self.block_in_1.setItemText(127, QCoreApplication.translate("MainWindow", u"W124", None))
        self.block_in_1.setItemText(128, QCoreApplication.translate("MainWindow", u"W125", None))
        self.block_in_1.setItemText(129, QCoreApplication.translate("MainWindow", u"W126", None))
        self.block_in_1.setItemText(130, QCoreApplication.translate("MainWindow", u"W127", None))
        self.block_in_1.setItemText(131, QCoreApplication.translate("MainWindow", u"W128", None))
        self.block_in_1.setItemText(132, QCoreApplication.translate("MainWindow", u"W129", None))
        self.block_in_1.setItemText(133, QCoreApplication.translate("MainWindow", u"W130", None))
        self.block_in_1.setItemText(134, QCoreApplication.translate("MainWindow", u"W131", None))
        self.block_in_1.setItemText(135, QCoreApplication.translate("MainWindow", u"W132", None))
        self.block_in_1.setItemText(136, QCoreApplication.translate("MainWindow", u"W133", None))
        self.block_in_1.setItemText(137, QCoreApplication.translate("MainWindow", u"W134", None))
        self.block_in_1.setItemText(138, QCoreApplication.translate("MainWindow", u"W135", None))
        self.block_in_1.setItemText(139, QCoreApplication.translate("MainWindow", u"W136", None))
        self.block_in_1.setItemText(140, QCoreApplication.translate("MainWindow", u"W137", None))
        self.block_in_1.setItemText(141, QCoreApplication.translate("MainWindow", u"W138", None))
        self.block_in_1.setItemText(142, QCoreApplication.translate("MainWindow", u"W139", None))
        self.block_in_1.setItemText(143, QCoreApplication.translate("MainWindow", u"W140", None))
        self.block_in_1.setItemText(144, QCoreApplication.translate("MainWindow", u"W141", None))
        self.block_in_1.setItemText(145, QCoreApplication.translate("MainWindow", u"W142", None))
        self.block_in_1.setItemText(146, QCoreApplication.translate("MainWindow", u"W143", None))
        self.block_in_1.setItemText(147, QCoreApplication.translate("MainWindow", u"X144", None))
        self.block_in_1.setItemText(148, QCoreApplication.translate("MainWindow", u"X145", None))
        self.block_in_1.setItemText(149, QCoreApplication.translate("MainWindow", u"X146", None))
        self.block_in_1.setItemText(150, QCoreApplication.translate("MainWindow", u"Y147", None))
        self.block_in_1.setItemText(151, QCoreApplication.translate("MainWindow", u"Y148", None))
        self.block_in_1.setItemText(152, QCoreApplication.translate("MainWindow", u"Y149", None))
        self.block_in_1.setItemText(153, QCoreApplication.translate("MainWindow", u"Z150", None))

        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Icons Guide", None))
        self.pushButton_1207.setText("")
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"Railway Switch", None))
        self.pushButton_1208.setText("")
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"Railway Crossing", None))
        self.pushButton_1209.setText("")
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"Track Lights", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"Lights: ", None))
        self.switch_out.setText("")
        self.light_out.setText("")
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"Switch Direction: ", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Block Data", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Block Length (ft):", None))
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Block Number:", None))
        self.cumm_elevation_in.setText("")
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Cummulative Elevation (ft):", None))
        self.label_143.setText(QCoreApplication.translate("MainWindow", u"Railway Crossings:", None))
        self.length_in.setText("")
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"Occupied:", None))
        self.cross_out.setText("")
        self.elevation_in.setText("")
        self.block_num_in.setText("")
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Track Heaters:", None))
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"Underground:", None))
        self.temp_out.setText("")
        self.grade_in.setText("")
        self.section_in.setText("")
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"Temperature (\u00b0F):", None))
        self.under_out.setText("")
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Block Grade (%):", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"Section: ", None))
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Speed Limit (mph):", None))
        self.occupancy_in.setText("")
        self.heaters_out.setText("")
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Elevation (ft):", None))
        self.speed_in.setText("")
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Temperature", None))
        self.label_150.setText(QCoreApplication.translate("MainWindow", u"Set Temperature (\u00b0F):", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Failure Modes", None))
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"Broken Rail", None))
        self.label_147.setText(QCoreApplication.translate("MainWindow", u"Power Failure", None))
        self.block_in_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Block", None))
        self.block_in_2.setItemText(1, QCoreApplication.translate("MainWindow", u"A1", None))
        self.block_in_2.setItemText(2, QCoreApplication.translate("MainWindow", u"A2", None))
        self.block_in_2.setItemText(3, QCoreApplication.translate("MainWindow", u"A3", None))
        self.block_in_2.setItemText(4, QCoreApplication.translate("MainWindow", u"B4", None))
        self.block_in_2.setItemText(5, QCoreApplication.translate("MainWindow", u"B5", None))
        self.block_in_2.setItemText(6, QCoreApplication.translate("MainWindow", u"B6", None))
        self.block_in_2.setItemText(7, QCoreApplication.translate("MainWindow", u"C7", None))
        self.block_in_2.setItemText(8, QCoreApplication.translate("MainWindow", u"C8", None))
        self.block_in_2.setItemText(9, QCoreApplication.translate("MainWindow", u"C9", None))
        self.block_in_2.setItemText(10, QCoreApplication.translate("MainWindow", u"C10", None))
        self.block_in_2.setItemText(11, QCoreApplication.translate("MainWindow", u"C11", None))
        self.block_in_2.setItemText(12, QCoreApplication.translate("MainWindow", u"C12", None))
        self.block_in_2.setItemText(13, QCoreApplication.translate("MainWindow", u"D13", None))
        self.block_in_2.setItemText(14, QCoreApplication.translate("MainWindow", u"D14", None))
        self.block_in_2.setItemText(15, QCoreApplication.translate("MainWindow", u"D15", None))
        self.block_in_2.setItemText(16, QCoreApplication.translate("MainWindow", u"D16", None))
        self.block_in_2.setItemText(17, QCoreApplication.translate("MainWindow", u"E17", None))
        self.block_in_2.setItemText(18, QCoreApplication.translate("MainWindow", u"E18", None))
        self.block_in_2.setItemText(19, QCoreApplication.translate("MainWindow", u"E19", None))
        self.block_in_2.setItemText(20, QCoreApplication.translate("MainWindow", u"E20", None))
        self.block_in_2.setItemText(21, QCoreApplication.translate("MainWindow", u"F21", None))
        self.block_in_2.setItemText(22, QCoreApplication.translate("MainWindow", u"F22", None))
        self.block_in_2.setItemText(23, QCoreApplication.translate("MainWindow", u"F23", None))
        self.block_in_2.setItemText(24, QCoreApplication.translate("MainWindow", u"F24", None))
        self.block_in_2.setItemText(25, QCoreApplication.translate("MainWindow", u"F25", None))
        self.block_in_2.setItemText(26, QCoreApplication.translate("MainWindow", u"F26", None))
        self.block_in_2.setItemText(27, QCoreApplication.translate("MainWindow", u"F27", None))
        self.block_in_2.setItemText(28, QCoreApplication.translate("MainWindow", u"F28", None))
        self.block_in_2.setItemText(29, QCoreApplication.translate("MainWindow", u"G29", None))
        self.block_in_2.setItemText(30, QCoreApplication.translate("MainWindow", u"G30", None))
        self.block_in_2.setItemText(31, QCoreApplication.translate("MainWindow", u"G31", None))
        self.block_in_2.setItemText(32, QCoreApplication.translate("MainWindow", u"G32", None))
        self.block_in_2.setItemText(33, QCoreApplication.translate("MainWindow", u"H33", None))
        self.block_in_2.setItemText(34, QCoreApplication.translate("MainWindow", u"H34", None))
        self.block_in_2.setItemText(35, QCoreApplication.translate("MainWindow", u"H35", None))
        self.block_in_2.setItemText(36, QCoreApplication.translate("MainWindow", u"I36", None))
        self.block_in_2.setItemText(37, QCoreApplication.translate("MainWindow", u"I37", None))
        self.block_in_2.setItemText(38, QCoreApplication.translate("MainWindow", u"I38", None))
        self.block_in_2.setItemText(39, QCoreApplication.translate("MainWindow", u"I39", None))
        self.block_in_2.setItemText(40, QCoreApplication.translate("MainWindow", u"I40", None))
        self.block_in_2.setItemText(41, QCoreApplication.translate("MainWindow", u"I41", None))
        self.block_in_2.setItemText(42, QCoreApplication.translate("MainWindow", u"I42", None))
        self.block_in_2.setItemText(43, QCoreApplication.translate("MainWindow", u"I43", None))
        self.block_in_2.setItemText(44, QCoreApplication.translate("MainWindow", u"I44", None))
        self.block_in_2.setItemText(45, QCoreApplication.translate("MainWindow", u"I45", None))
        self.block_in_2.setItemText(46, QCoreApplication.translate("MainWindow", u"I46", None))
        self.block_in_2.setItemText(47, QCoreApplication.translate("MainWindow", u"I47", None))
        self.block_in_2.setItemText(48, QCoreApplication.translate("MainWindow", u"I48", None))
        self.block_in_2.setItemText(49, QCoreApplication.translate("MainWindow", u"I49", None))
        self.block_in_2.setItemText(50, QCoreApplication.translate("MainWindow", u"I50", None))
        self.block_in_2.setItemText(51, QCoreApplication.translate("MainWindow", u"I51", None))
        self.block_in_2.setItemText(52, QCoreApplication.translate("MainWindow", u"I52", None))
        self.block_in_2.setItemText(53, QCoreApplication.translate("MainWindow", u"I53", None))
        self.block_in_2.setItemText(54, QCoreApplication.translate("MainWindow", u"I54", None))
        self.block_in_2.setItemText(55, QCoreApplication.translate("MainWindow", u"I55", None))
        self.block_in_2.setItemText(56, QCoreApplication.translate("MainWindow", u"I56", None))
        self.block_in_2.setItemText(57, QCoreApplication.translate("MainWindow", u"I57", None))
        self.block_in_2.setItemText(58, QCoreApplication.translate("MainWindow", u"J58", None))
        self.block_in_2.setItemText(59, QCoreApplication.translate("MainWindow", u"J59", None))
        self.block_in_2.setItemText(60, QCoreApplication.translate("MainWindow", u"J60", None))
        self.block_in_2.setItemText(61, QCoreApplication.translate("MainWindow", u"J61", None))
        self.block_in_2.setItemText(62, QCoreApplication.translate("MainWindow", u"J62", None))
        self.block_in_2.setItemText(63, QCoreApplication.translate("MainWindow", u"K63", None))
        self.block_in_2.setItemText(64, QCoreApplication.translate("MainWindow", u"K64", None))
        self.block_in_2.setItemText(65, QCoreApplication.translate("MainWindow", u"K65", None))
        self.block_in_2.setItemText(66, QCoreApplication.translate("MainWindow", u"K66", None))
        self.block_in_2.setItemText(67, QCoreApplication.translate("MainWindow", u"K67", None))
        self.block_in_2.setItemText(68, QCoreApplication.translate("MainWindow", u"K68", None))
        self.block_in_2.setItemText(69, QCoreApplication.translate("MainWindow", u"L69", None))
        self.block_in_2.setItemText(70, QCoreApplication.translate("MainWindow", u"L70", None))
        self.block_in_2.setItemText(71, QCoreApplication.translate("MainWindow", u"L71", None))
        self.block_in_2.setItemText(72, QCoreApplication.translate("MainWindow", u"L72", None))
        self.block_in_2.setItemText(73, QCoreApplication.translate("MainWindow", u"L73", None))
        self.block_in_2.setItemText(74, QCoreApplication.translate("MainWindow", u"M74", None))
        self.block_in_2.setItemText(75, QCoreApplication.translate("MainWindow", u"M75", None))
        self.block_in_2.setItemText(76, QCoreApplication.translate("MainWindow", u"M76", None))
        self.block_in_2.setItemText(77, QCoreApplication.translate("MainWindow", u"N77", None))
        self.block_in_2.setItemText(78, QCoreApplication.translate("MainWindow", u"N78", None))
        self.block_in_2.setItemText(79, QCoreApplication.translate("MainWindow", u"N79", None))
        self.block_in_2.setItemText(80, QCoreApplication.translate("MainWindow", u"N80", None))
        self.block_in_2.setItemText(81, QCoreApplication.translate("MainWindow", u"N81", None))
        self.block_in_2.setItemText(82, QCoreApplication.translate("MainWindow", u"N82", None))
        self.block_in_2.setItemText(83, QCoreApplication.translate("MainWindow", u"N83", None))
        self.block_in_2.setItemText(84, QCoreApplication.translate("MainWindow", u"N84", None))
        self.block_in_2.setItemText(85, QCoreApplication.translate("MainWindow", u"N85", None))
        self.block_in_2.setItemText(86, QCoreApplication.translate("MainWindow", u"O86", None))
        self.block_in_2.setItemText(87, QCoreApplication.translate("MainWindow", u"O87", None))
        self.block_in_2.setItemText(88, QCoreApplication.translate("MainWindow", u"O88", None))
        self.block_in_2.setItemText(89, QCoreApplication.translate("MainWindow", u"P89", None))
        self.block_in_2.setItemText(90, QCoreApplication.translate("MainWindow", u"P90", None))
        self.block_in_2.setItemText(91, QCoreApplication.translate("MainWindow", u"P91", None))
        self.block_in_2.setItemText(92, QCoreApplication.translate("MainWindow", u"P92", None))
        self.block_in_2.setItemText(93, QCoreApplication.translate("MainWindow", u"P93", None))
        self.block_in_2.setItemText(94, QCoreApplication.translate("MainWindow", u"P94", None))
        self.block_in_2.setItemText(95, QCoreApplication.translate("MainWindow", u"P95", None))
        self.block_in_2.setItemText(96, QCoreApplication.translate("MainWindow", u"P96", None))
        self.block_in_2.setItemText(97, QCoreApplication.translate("MainWindow", u"P97", None))
        self.block_in_2.setItemText(98, QCoreApplication.translate("MainWindow", u"Q98", None))
        self.block_in_2.setItemText(99, QCoreApplication.translate("MainWindow", u"Q99", None))
        self.block_in_2.setItemText(100, QCoreApplication.translate("MainWindow", u"Q100", None))
        self.block_in_2.setItemText(101, QCoreApplication.translate("MainWindow", u"R101", None))
        self.block_in_2.setItemText(102, QCoreApplication.translate("MainWindow", u"S102", None))
        self.block_in_2.setItemText(103, QCoreApplication.translate("MainWindow", u"S103", None))
        self.block_in_2.setItemText(104, QCoreApplication.translate("MainWindow", u"S104", None))
        self.block_in_2.setItemText(105, QCoreApplication.translate("MainWindow", u"T105", None))
        self.block_in_2.setItemText(106, QCoreApplication.translate("MainWindow", u"T106", None))
        self.block_in_2.setItemText(107, QCoreApplication.translate("MainWindow", u"T107", None))
        self.block_in_2.setItemText(108, QCoreApplication.translate("MainWindow", u"T108", None))
        self.block_in_2.setItemText(109, QCoreApplication.translate("MainWindow", u"T109", None))
        self.block_in_2.setItemText(110, QCoreApplication.translate("MainWindow", u"U110", None))
        self.block_in_2.setItemText(111, QCoreApplication.translate("MainWindow", u"U111", None))
        self.block_in_2.setItemText(112, QCoreApplication.translate("MainWindow", u"U112", None))
        self.block_in_2.setItemText(113, QCoreApplication.translate("MainWindow", u"U113", None))
        self.block_in_2.setItemText(114, QCoreApplication.translate("MainWindow", u"U114", None))
        self.block_in_2.setItemText(115, QCoreApplication.translate("MainWindow", u"U115", None))
        self.block_in_2.setItemText(116, QCoreApplication.translate("MainWindow", u"U116", None))
        self.block_in_2.setItemText(117, QCoreApplication.translate("MainWindow", u"V117", None))
        self.block_in_2.setItemText(118, QCoreApplication.translate("MainWindow", u"V118", None))
        self.block_in_2.setItemText(119, QCoreApplication.translate("MainWindow", u"V119", None))
        self.block_in_2.setItemText(120, QCoreApplication.translate("MainWindow", u"V120", None))
        self.block_in_2.setItemText(121, QCoreApplication.translate("MainWindow", u"V121", None))
        self.block_in_2.setItemText(122, QCoreApplication.translate("MainWindow", u"W122", None))
        self.block_in_2.setItemText(123, QCoreApplication.translate("MainWindow", u"W123", None))
        self.block_in_2.setItemText(124, QCoreApplication.translate("MainWindow", u"W124", None))
        self.block_in_2.setItemText(125, QCoreApplication.translate("MainWindow", u"W125", None))
        self.block_in_2.setItemText(126, QCoreApplication.translate("MainWindow", u"W126", None))
        self.block_in_2.setItemText(127, QCoreApplication.translate("MainWindow", u"W127", None))
        self.block_in_2.setItemText(128, QCoreApplication.translate("MainWindow", u"W128", None))
        self.block_in_2.setItemText(129, QCoreApplication.translate("MainWindow", u"W129", None))
        self.block_in_2.setItemText(130, QCoreApplication.translate("MainWindow", u"W130", None))
        self.block_in_2.setItemText(131, QCoreApplication.translate("MainWindow", u"W131", None))
        self.block_in_2.setItemText(132, QCoreApplication.translate("MainWindow", u"W132", None))
        self.block_in_2.setItemText(133, QCoreApplication.translate("MainWindow", u"W133", None))
        self.block_in_2.setItemText(134, QCoreApplication.translate("MainWindow", u"W134", None))
        self.block_in_2.setItemText(135, QCoreApplication.translate("MainWindow", u"W135", None))
        self.block_in_2.setItemText(136, QCoreApplication.translate("MainWindow", u"W136", None))
        self.block_in_2.setItemText(137, QCoreApplication.translate("MainWindow", u"W137", None))
        self.block_in_2.setItemText(138, QCoreApplication.translate("MainWindow", u"W138", None))
        self.block_in_2.setItemText(139, QCoreApplication.translate("MainWindow", u"W139", None))
        self.block_in_2.setItemText(140, QCoreApplication.translate("MainWindow", u"W140", None))
        self.block_in_2.setItemText(141, QCoreApplication.translate("MainWindow", u"W141", None))
        self.block_in_2.setItemText(142, QCoreApplication.translate("MainWindow", u"W142", None))
        self.block_in_2.setItemText(143, QCoreApplication.translate("MainWindow", u"W143", None))
        self.block_in_2.setItemText(144, QCoreApplication.translate("MainWindow", u"X144", None))
        self.block_in_2.setItemText(145, QCoreApplication.translate("MainWindow", u"X145", None))
        self.block_in_2.setItemText(146, QCoreApplication.translate("MainWindow", u"X146", None))
        self.block_in_2.setItemText(147, QCoreApplication.translate("MainWindow", u"Y147", None))
        self.block_in_2.setItemText(148, QCoreApplication.translate("MainWindow", u"Y148", None))
        self.block_in_2.setItemText(149, QCoreApplication.translate("MainWindow", u"Y149", None))
        self.block_in_2.setItemText(150, QCoreApplication.translate("MainWindow", u"Z150", None))

        self.set_power_failure.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"Track Circuit Failure", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
        self.set_track_failure.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.set_broken_rail.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Occupancy Color Guide", None))
        self.pushButton_1210.setText("")
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"Broken Rail", None))
        self.pushButton_1211.setText("")
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"Track Circuit", None))
        self.pushButton_1212.setText("")
        self.label_153.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.pushButton_1213.setText("")
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"Occupied", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Upload Track Layout", None))
        self.green_line.setTitle("")
        self.K68.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.E17.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.W132.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.Q99.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.F26.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.K63.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.N78.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.W133.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.G30.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.W130.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.L73.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.N84.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.F22.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.Q100.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.N79.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.L69.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.U110.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.U113.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.P96.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.B6.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.Y149.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.N77.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.O88.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.W135.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.Z150.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.R101.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.N80.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.S103.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.T107.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.K66.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.D16.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.Q98.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.E19.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.P95.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.F21.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.D14.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.B4.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.E20.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.W136.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.Y148.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.N83.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.M76.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.T105.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.P92.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.U111.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.W137.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.N81.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.G31.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.O87.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.S104.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.P93.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.A1.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.L70.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.F27.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.K67.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.D13.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.F24.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.Y147.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.D15.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.L72.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.W134.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.W131.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.T106.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.K64.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.C11.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.K65.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.E18.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.P91.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.C9.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.W138.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.P90.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.G32.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.C7.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.F23.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.M74.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.M75.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.T108.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.T109.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.B5.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.P94.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.F28.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.N82.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.G29.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.A3.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.N85.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.O86.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.X146.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.P97.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.C8.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.U114.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.S102.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.U112.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.C10.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.C12.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.P89.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.X145.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.F25.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.H33.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.A2.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.L71.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.W139.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.W140.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.W141.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.W142.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.W143.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.X144.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.H34.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.H35.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.I36.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I37.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I38.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I39.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I40.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I41.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I42.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I43.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I44.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I45.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I46.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.W129.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.I47.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I48.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.W128.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.W127.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.I49.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.W126.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.I50.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I51.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.W125.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.W124.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.W123.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.I52.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I53.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I54.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.W122.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.I55.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.V121.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.I56.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.I57.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.J58.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.J59.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.V120.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.V119.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.V118.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.J62.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.J61.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.V117.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.U116.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.U115.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.J60.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.Y.setText(QCoreApplication.translate("MainWindow", u"Yard", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Station Data", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Ticket Sales:", None))
        self.disembarking_out.setText("")
        self.station_in.setText("")
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"Passengers Boarding:", None))
        self.boarding_out.setText("")
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"Station Name:", None))
        self.ticket_out.setText("")
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Passengers Disembarking:", None))
    # retranslateUi

