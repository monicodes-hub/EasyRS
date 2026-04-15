# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow - copia.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
import resources_mainwindow_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(529, 531)
        icon = QIcon()
        icon.addFile(u":/icons/resources/app_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/* Main window background */\n"
"\n"
"QMainWindow, #centralwidget {\n"
"\n"
"/* border-image hace que la imagen se adapte al tama\u00f1o de la ventana sin repetirse */\n"
"\n"
"	border-image: url(:/background/resources/background_2.0.png) 0 0 0 0 stretch stretch;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/* GroupBox: slightly darker, rounded corners, SEGOE UI, 14pt, white text */\n"
"\n"
"QGroupBox {\n"
"\n"
"    /* Un borde cyan semitransparente da un efecto cristal muy moderno */\n"
"    border: 2px solid rgba(34, 9, 67, 0.4); \n"
"    border-radius: 20px; \n"
"    margin-top: 15px;    \n"
"    padding: 16px; \n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"}\n"
"\n"
"\n"
"\n"
"/* GroupBox title: white, bold, with background and padding */\n"
"\n"
"QGroupBox::title {\n"
"\n"
"subcontrol-origin: margin;\n"
"\n"
"subcontrol-position: top left;\n"
"\n"
"left: 20px;\n"
"\n"
"padding: 0 5px 0 5px;\n"
"\n"
"color: #7bc1d4;\n"
"\n"
"font-weight: bold;\n"
"\n"
"font-family: 'Segoe UI', Se"
                        "goe, Arial, sans-serif;\n"
"\n"
"font-size: 14pt;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/* Frames: transparent to let main bg show through */\n"
"\n"
"QFrame {\n"
"\n"
"background: transparent;\n"
"\n"
"border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/* Buttons: only for button1_routing and button2_conversations, white text */\n"
"\n"
"QPushButton#button1_routing, QPushButton#button2_conversations {\n"
"\n"
"font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"\n"
"font-size: 14pt;\n"
"\n"
"color: #fff;\n"
"\n"
"background-color: #7c6fc2;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"padding: 8px 16px;\n"
"\n"
"\n"
"\n"
"border: 2px solid transparent;\n"
"\n"
"transition: border 0.2s, box-shadow 0.2s;\n"
"\n"
"}\n"
"\n"
"QPushButton#button1_routing:hover, QPushButton#button2_conversations:hover {\n"
"	background-color: #7c6fc2;\n"
"    /* Efecto Ne\u00f3n: Cambiamos el color del borde para simular un resplandor cyan */\n"
"    border: 2px solid #7bc1d4; \n"
"}\n"
"	/*background-color: #625090;\n"
""
                        "	border: 2px solid #614f90;\n"
"	box-shadow: 0 0 0 2px #7bc1d4;\n"
"}*/\n"
"\n"
"\n"
"QPushButton#button1_routing:pressed, QPushButton#button2_conversations:pressed {\n"
"    background-color: #220943;\n"
"    border: 2px solid #625090;\n"
"	padding: 9px 17px 7px 19px;\n"
"}\n"
"\n"
"	/*background-color: #6a5fb2;\n"
"}*/\n"
"\n"
"\n"
"/* Other buttons: subtle style, rounded, white text */\n"
"\n"
"QPushButton {\n"
"\n"
"background-color: #220943;\n"
"\n"
"color: #7bc1d4;\n"
"\n"
"border-radius: 10px;\n"
"\n"
"padding: 6px 18px;\n"
"\n"
"font-size: 15px;\n"
"\n"
"\n"
"\n"
"border: 2px solid transparent;\n"
"\n"
"transition: border 0.2s, box-shadow 0.2s;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #625090;\n"
"    color: #ffffff; /* Al pasar el rat\u00f3n, el texto pasa a blanco para contrastar */\n"
"    border: 1px solid #7bc1d4; /* El borde se ilumina */\n"
"}\n"
"\n"
"/*background-color: #625090;\n"
"\n"
"border: 2px solid #fff;\n"
"\n"
"box-shadow: 0 0 0 2px #7bc1d4;\n"
"\n"
"}*/\n"
"\n"
""
                        "QPushButton:pressed {\n"
"    background-color: #2F1651;\n"
"    color: #ffffff; /* Al pasar el rat\u00f3n, el texto pasa a blanco para contrastar */\n"
"    border: 1px solid #7bc1d4; /* El borde se ilumina */\n"
"	padding: 9px 17px 7px 19px;\n"
"}\n"
"\n"
"/*background-color: #6a5fb2;\n"
"\n"
"}*/\n"
"\n"
"\n"
"\n"
"/* Labels: white text for headers/footers */\n"
"\n"
"QLabel#logo_header, QLabel#logo_footer {\n"
"\n"
"color: #fff;\n"
"\n"
"font-size: 18px;\n"
"\n"
"font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/* Status bar: match main color, white text */\n"
"\n"
"QStatusBar {\n"
"\n"
"background: #2A0E4F;\n"
"\n"
"color: #7bc1d4;\n"
"\n"
"border-top: 1px solid #220943;\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 140))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

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
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        self.groupBox.setFont(font)
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
        self.pushButton.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Seleccione el tipo de reporte:", None))
#if QT_CONFIG(statustip)
        self.pushButton_2.setStatusTip(QCoreApplication.translate("MainWindow", u"Seleccione el archivo 9. CDR Routing interacciones y chatbots", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u" Diagram Reports - CDR Routing", None))
#if QT_CONFIG(statustip)
        self.pushButton_3.setStatusTip(QCoreApplication.translate("MainWindow", u"Seleccione el archivo 2. Conversaciones", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u" Interacciones y Chats - Conversaciones", None))
    # retranslateUi

