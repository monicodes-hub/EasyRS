# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'routing.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import resources_routing_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(536, 393)
        icon = QIcon()
        icon.addFile(u":/icons/resources/app_logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"/* Dialog background */\n"
"QDialog {\n"
"    background-color: #a595fa;\n"
"}\n"
"\n"
"/* GroupBox: rounded, white font */\n"
"QGroupBox#groupBox {\n"
"    border: 2px solid #7c6fc2;\n"
"    border-radius: 20px;\n"
"    margin-top: 20px;\n"
"    padding: 14px 10px 10px 10px;\n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"    font-size: 14pt;\n"
"    color: #fff;\n"
"}\n"
"\n"
"/* GroupBox title: left, no background, white */\n"
"QGroupBox#groupBox::title {\n"
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
"/* Input field for routingID: rounded, slightly darker background, white text */\n"
"QLineEdit#routingID_input {\n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"    font-size: 12pt;\n"
"    color: #fff;\n"
"    background-color: #7c6fc2;\n"
"    border-radius: 10px;\n"
""
                        "    padding: 0px 8px;\n"
"    border: 2px solid #7c6fc2;\n"
"}\n"
"\n"
"/* Info label inside groupBox: white, italic, slightly smaller */\n"
"QLabel#example_info {\n"
"    color: #fff;\n"
"    font-size: 10pt;\n"
"    font-style: italic;\n"
"    font-family: 'Segoe UI', Segoe, Arial, sans-serif;\n"
"}\n"
"\n"
"/* OK Button: prominent, white text, hover effect */\n"
"QPushButton#ok_button {\n"
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
"QPushButton#cancel_butto"
                        "n {\n"
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
"    background-color: #9587e3;\n"
"    border: 2px solid #fff;\n"
"    box-shadow: 0 0 0 2px #fff;\n"
"}\n"
"QPushButton#cancel_button:pressed {\n"
"    background-color: #6a5fb2;\n"
"}\n"
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
        self.frame1_header.setMaximumSize(QSize(16777215, 100))
        self.frame1_header.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame1_header.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame1_header)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.logo_header = QLabel(self.frame1_header)
        self.logo_header.setObjectName(u"logo_header")
        self.logo_header.setPixmap(QPixmap(u":/logos/resources/header_logo.png"))
        self.logo_header.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.logo_header)


        self.verticalLayout.addWidget(self.frame1_header)

        self.frame2_body = QFrame(Dialog)
        self.frame2_body.setObjectName(u"frame2_body")
        self.frame2_body.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame2_body.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame2_body)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox = QGroupBox(self.frame2_body)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.routingID_input = QLineEdit(self.groupBox)
        self.routingID_input.setObjectName(u"routingID_input")

        self.verticalLayout_4.addWidget(self.routingID_input)

        self.example_info = QLabel(self.groupBox)
        self.example_info.setObjectName(u"example_info")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setItalic(True)
        self.example_info.setFont(font)

        self.verticalLayout_4.addWidget(self.example_info)


        self.verticalLayout_5.addWidget(self.groupBox)

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


        self.verticalLayout_5.addWidget(self.frame_okcancel, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.frame2_body)

        self.frame3_footer = QFrame(Dialog)
        self.frame3_footer.setObjectName(u"frame3_footer")
        self.frame3_footer.setMaximumSize(QSize(16777215, 100))
        self.frame3_footer.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame3_footer.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame3_footer)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.logo_footer = QLabel(self.frame3_footer)
        self.logo_footer.setObjectName(u"logo_footer")
        self.logo_footer.setMaximumSize(QSize(16777215, 100))
        self.logo_footer.setPixmap(QPixmap(u":/logos/resources/footer_logo.png"))
        self.logo_footer.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout_3.addWidget(self.logo_footer)


        self.verticalLayout.addWidget(self.frame3_footer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"EasyRepSift - Routing", None))
        self.logo_header.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Introduce el conector a filtrar:", None))
#if QT_CONFIG(statustip)
        self.routingID_input.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.example_info.setText(QCoreApplication.translate("Dialog", u"Para m\u00e1s de un conector, separar por comas (p. ej. 61014,61038).", None))
        self.ok_button.setText("")
        self.cancel_button.setText("")
        self.logo_footer.setText("")
    # retranslateUi

