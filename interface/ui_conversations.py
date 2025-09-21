# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'conversationsCssJqV.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)
import resources_conversations_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(536, 539)
        icon = QIcon()
        icon.addFile(u":/icons/resources/app_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"/* Dialog background */\n"
"QDialog {\n"
"    background-color: #a595fa;\n"
"}\n"
"\n"
"/* GroupBoxes: slightly darker, rounded, white font */\n"
"QGroupBox {\n"
"    border: 2px solid #7c6fc2;\n"
"    border-radius: 20px;\n"
"    margin-top: 20px;\n"
"    padding: 16px 10px 10px 10px; /* More top padding for title */\n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    color: #fff;\n"
"}\n"
"\n"
"/* GroupBox title: left, no background, white, bold */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    left: 15px;\n"
"    padding: 0 5px;\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"/* ComboBox: white text, rounded, matching background */\n"
"QComboBox#select_agent {\n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"    font-size: 12pt;\n"
"    color: #fff;\n"
"    background-color: #7c6fc2;\n"
"    border-r"
                        "adius: 10px;\n"
"    padding: 0px 8px;\n"
"    border: 5px solid #7c6fc2;\n"
"}\n"
"QComboBox#select_agent QAbstractItemView {\n"
"    background: #9587e3;\n"
"    color: #fff;\n"
"    selection-background-color: #7c6fc2;\n"
"    selection-color: #fff;\n"
"}\n"
"\n"
"QRadioButton#conversations_all::indicator,\n"
"QRadioButton#conversations_unanswered::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #7c6fc2;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QRadioButton#conversations_all::indicator:checked,\n"
"QRadioButton#conversations_unanswered::indicator:checked {\n"
"    background-color: #7c6fc2;\n"
"    border: 2px solid #fff;\n"
"}\n"
"\n"
"/* Radio buttons: white text, larger font */\n"
"QRadioButton#conversations_all, QRadioButton#conversations_unanswered {\n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"    font-size: 12pt;\n"
"    color: #fff;\n"
"}\n"
"\n"
"/* OK Button: prominent, white text, hover effect */\n"
"QPush"
                        "Button#ok_button {\n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"    font-size: 15pt;\n"
"    color: #fff;\n"
"    background-color: #7c6fc2;\n"
"    border-radius: 10px;\n"
"    padding: 6px 18px;\n"
"    font-weight: bold;\n"
"    border: 2px solid transparent;\n"
"    transition: border 0.2s, box-shadow 0.2s;\n"
"}\n"
"QPushButton#ok_button:hover {\n"
"    background-color: #9587e3;\n"
"    border: 2px solid #fff;\n"
"    box-shadow: 0 0 0 2px #fff;\n"
"}\n"
"QPushButton#ok_button:pressed {\n"
"    background-color: #6a5fb2;\n"
"}\n"
"\n"
"/* CANCEL Button: prominent, white text, hover effect */\n"
"QPushButton#cancel_button {\n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"    font-size: 15pt;\n"
"    color: #fff;\n"
"    background-color: #7c6fc2;\n"
"    border-radius: 10px;\n"
"    padding: 6px 18px;\n"
"    font-weight: bold;\n"
"    border: 2px solid transparent;\n"
"    transition: border 0.2s, box-shadow 0.2s;\n"
"}\n"
"QPushButton#cancel_button:hover {\n"
"    backgr"
                        "ound-color: #9587e3;\n"
"    border: 2px solid #fff;\n"
"    box-shadow: 0 0 0 2px #fff;\n"
"}\n"
"QPushButton#cancel_button:pressed {\n"
"    background-color: #6a5fb2;\n"
"}\n"
"\n"
"\n"
"/* Header/Footer labels: white, bold, larger */\n"
"QLabel#logo_header, QLabel#logo_footer {\n"
"    color: #fff;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Frames: transparent */\n"
"QFrame {\n"
"    background: transparent;\n"
"    border: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame1_header = QFrame(Dialog)
        self.frame1_header.setObjectName(u"frame1_header")
        self.frame1_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame1_header.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame1_header)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.logo_header = QLabel(self.frame1_header)
        self.logo_header.setObjectName(u"logo_header")
        self.logo_header.setPixmap(QPixmap(u":/logos/resources/header_logo.png"))
        self.logo_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.logo_header)


        self.verticalLayout.addWidget(self.frame1_header, 0, Qt.AlignmentFlag.AlignTop)

        self.frame2_body = QFrame(Dialog)
        self.frame2_body.setObjectName(u"frame2_body")
        self.frame2_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame2_body.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame2_body)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox1 = QGroupBox(self.frame2_body)
        self.groupBox1.setObjectName(u"groupBox1")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.select_agent = QComboBox(self.groupBox1)
        self.select_agent.setObjectName(u"select_agent")

        self.verticalLayout_5.addWidget(self.select_agent)


        self.verticalLayout_2.addWidget(self.groupBox1)

        self.groupBox2 = QGroupBox(self.frame2_body)
        self.groupBox2.setObjectName(u"groupBox2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.conversations_all = QRadioButton(self.groupBox2)
        self.conversations_all.setObjectName(u"conversations_all")

        self.verticalLayout_6.addWidget(self.conversations_all)

        self.conversations_unanswered = QRadioButton(self.groupBox2)
        self.conversations_unanswered.setObjectName(u"conversations_unanswered")

        self.verticalLayout_6.addWidget(self.conversations_unanswered)


        self.verticalLayout_2.addWidget(self.groupBox2)

        self.frame_okcancel = QFrame(self.frame2_body)
        self.frame_okcancel.setObjectName(u"frame_okcancel")
        self.frame_okcancel.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_okcancel.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_okcancel)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ok_button = QPushButton(self.frame_okcancel)
        self.ok_button.setObjectName(u"ok_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/ok.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ok_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.ok_button)

        self.cancel_button = QPushButton(self.frame_okcancel)
        self.cancel_button.setObjectName(u"cancel_button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cancel_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.cancel_button)


        self.verticalLayout_2.addWidget(self.frame_okcancel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame2_body)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/logos/resources/footer_logo.png"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignmentFlag.AlignBottom)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"EasyRepSift - Conversaciones", None))
        self.logo_header.setText("")
        self.groupBox1.setTitle(QCoreApplication.translate("Dialog", u"Seleccione el agente:", None))
        self.groupBox2.setTitle(QCoreApplication.translate("Dialog", u"Seleccione el tipo de conversaci\u00f3n:", None))
        self.conversations_all.setText(QCoreApplication.translate("Dialog", u"Todas las conversaciones", None))
        self.conversations_unanswered.setText(QCoreApplication.translate("Dialog", u"Solo las conversaciones que se quedaron sin respuesta", None))
        self.ok_button.setText("")
        self.cancel_button.setText("")
        self.label.setText("")
    # retranslateUi

