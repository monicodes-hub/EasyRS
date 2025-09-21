# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)
import resources_mainwindow_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(536, 415)
        icon = QIcon()
        icon.addFile(u":/icons/resources/app_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/* Main window background */\n"
"QMainWindow, QWidget {\n"
"    background-color: #a595fa;\n"
"}\n"
"\n"
"/* GroupBox: slightly darker, rounded corners, SEGOE UI, 14pt, white text */\n"
"QGroupBox {\n"
"\n"
"    border: 2px solid #7c6fc2;\n"
"    border-radius: 20px; /* More rounded */\n"
"    margin-top: 20px;    /* More space for the title */\n"
"    padding: 8px; /* Extra top padding for title */\n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    color: #fff;\n"
"}\n"
"\n"
"/* GroupBox title: white, bold, with background and padding */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 20px;\n"
"    padding: 0 5px 0 5px;\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"/* Frames: transparent to let main bg show through */\n"
"QFrame {\n"
"    background: transparent;\n"
"    border: "
                        "none;\n"
"}\n"
"\n"
"/* Buttons: only for button1_routing and button2_conversations, white text */\n"
"QPushButton#button1_routing, QPushButton#button2_conversations {\n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    color: #fff;\n"
"    background-color: #7c6fc2;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px;\n"
"\n"
"    border: 2px solid transparent;\n"
"    transition: border 0.2s, box-shadow 0.2s;\n"
"}\n"
"QPushButton#button1_routing:hover, QPushButton#button2_conversations:hover {\n"
"    background-color: #9587e3;\n"
"    border: 2px solid #7c6fc2;\n"
"    box-shadow: 0 0 0 2px #fff;\n"
"}\n"
"QPushButton#button1_routing:pressed, QPushButton#button2_conversations:pressed {\n"
"    background-color: #6a5fb2;\n"
"}\n"
"\n"
"/* Other buttons: subtle style, rounded, white text */\n"
"QPushButton {\n"
"    background-color: #7c6fc2;\n"
"    color: #fff;\n"
"    border-radius: 10px;\n"
"    padding: 6px 18px;\n"
"    font-size: 15px;\n"
"\n"
"    border: 2p"
                        "x solid transparent;\n"
"    transition: border 0.2s, box-shadow 0.2s;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #9587e3;\n"
"    border: 2px solid #fff;\n"
"    box-shadow: 0 0 0 2px #fff;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #6a5fb2;\n"
"}\n"
"\n"
"/* Labels: white text for headers/footers */\n"
"QLabel#logo_header, QLabel#logo_footer {\n"
"    color: #fff;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Status bar: match main color, white text */\n"
"QStatusBar {\n"
"    background: #a595fa;\n"
"    color: #fff;\n"
"    border-top: 1px solid #7c6fc2;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/logos/resources/header_logo.png"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignRight)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/folder_open.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.pushButton_2, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.pushButton_3, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_2.addWidget(self.groupBox, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/logos/resources/footer_logo.png"))
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EasyRepSift", None))
        self.label.setText("")
        self.pushButton.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Seleccione el tipo de reporte:", None))
#if QT_CONFIG(statustip)
        self.pushButton_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Seleccione el archivo que empiece por \"HistVR\"", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" Diagram Reports - CDR Routing", None))
#if QT_CONFIG(statustip)
        self.pushButton_3.setStatusTip(QCoreApplication.translate("MainWindow", u"Seleccione el archivo que empiece por \"HistChat\"", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u" Interacciones y Chats - Conversaciones", None))
        self.label_2.setText("")
    # retranslateUi

