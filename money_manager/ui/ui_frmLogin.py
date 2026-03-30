# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmLogin.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(474, 340)
        LoginScreen.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.lblManagerMoney = QLabel(LoginScreen)
        self.lblManagerMoney.setObjectName(u"lblManagerMoney")
        self.lblManagerMoney.setEnabled(True)
        self.lblManagerMoney.setGeometry(QRect(80, 40, 269, 49))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        self.lblManagerMoney.setFont(font)
        self.lblManagerMoney.setStyleSheet(u"color:rgb(85, 0, 255);\n"
"font: 28pt \"Segoe UI\";")
        self.widget = QWidget(LoginScreen)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 240, 301, 71))
        self.hlLoginClose = QHBoxLayout(self.widget)
        self.hlLoginClose.setObjectName(u"hlLoginClose")
        self.hlLoginClose.setContentsMargins(0, 0, 0, 0)
        self.btnLogin = QPushButton(self.widget)
        self.btnLogin.setObjectName(u"btnLogin")
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI Semilight"])
        font1.setPointSize(14)
        self.btnLogin.setFont(font1)

        self.hlLoginClose.addWidget(self.btnLogin)

        self.btnClose = QPushButton(self.widget)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setFont(font1)

        self.hlLoginClose.addWidget(self.btnClose)

        self.widget1 = QWidget(LoginScreen)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(70, 120, 301, 101))
        self.hlInput = QHBoxLayout(self.widget1)
        self.hlInput.setObjectName(u"hlInput")
        self.hlInput.setContentsMargins(0, 0, 0, 0)
        self.vlUsername = QVBoxLayout()
        self.vlUsername.setObjectName(u"vlUsername")
        self.lblUsername = QLabel(self.widget1)
        self.lblUsername.setObjectName(u"lblUsername")
        self.lblUsername.setEnabled(True)
        self.lblUsername.setFont(font1)

        self.vlUsername.addWidget(self.lblUsername)

        self.lblPassword = QLabel(self.widget1)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setFont(font1)
        self.lblPassword.setStyleSheet(u"color:rgb(255, 0, 0)")

        self.vlUsername.addWidget(self.lblPassword)


        self.hlInput.addLayout(self.vlUsername)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lneUsername = QLineEdit(self.widget1)
        self.lneUsername.setObjectName(u"lneUsername")

        self.verticalLayout_2.addWidget(self.lneUsername)

        self.lnePassword = QLineEdit(self.widget1)
        self.lnePassword.setObjectName(u"lnePassword")
        self.lnePassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.lnePassword)


        self.hlInput.addLayout(self.verticalLayout_2)


        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
        
        self.lblError = QLabel(LoginScreen)
        self.lblError.setGeometry(QRect(60, 215, 360, 25))
        self.lblError.setStyleSheet("color: red;")
        self.lblError.setObjectName("lblError")
        self.lblError.setText("")
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"Form", None))
        self.lblManagerMoney.setText(QCoreApplication.translate("LoginScreen", u"Manager Money", None))
        self.btnLogin.setText(QCoreApplication.translate("LoginScreen", u"Login", None))
        self.btnClose.setText(QCoreApplication.translate("LoginScreen", u"Close", None))
        self.lblUsername.setText(QCoreApplication.translate("LoginScreen", u"Username", None))
        self.lblPassword.setText(QCoreApplication.translate("LoginScreen", u"Password", None))
    # retranslateUi

