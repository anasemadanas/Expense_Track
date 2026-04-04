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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(474, 340)
        LoginScreen.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.lblManagerMoney = QLabel(LoginScreen)
        self.lblManagerMoney.setObjectName(u"lblManagerMoney")
        self.lblManagerMoney.setEnabled(True)
        self.lblManagerMoney.setGeometry(QRect(100, 30, 269, 49))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        self.lblManagerMoney.setFont(font)
        self.lblManagerMoney.setStyleSheet(u"color:rgb(85, 0, 255);\n"
"font: 28pt \"Segoe UI\";")
        self.layoutWidget = QWidget(LoginScreen)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 240, 321, 71))
        self.hlLoginClose = QHBoxLayout(self.layoutWidget)
        self.hlLoginClose.setObjectName(u"hlLoginClose")
        self.hlLoginClose.setContentsMargins(0, 0, 0, 0)
        self.btnLogin = QPushButton(self.layoutWidget)
        self.btnLogin.setObjectName(u"btnLogin")
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI Semilight"])
        font1.setPointSize(14)
        self.btnLogin.setFont(font1)

        self.hlLoginClose.addWidget(self.btnLogin)

        self.btnClose = QPushButton(self.layoutWidget)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setFont(font1)

        self.hlLoginClose.addWidget(self.btnClose)

        self.layoutWidget1 = QWidget(LoginScreen)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(70, 100, 321, 121))
        self.gridLayoutInput = QGridLayout(self.layoutWidget1)
        self.gridLayoutInput.setObjectName(u"gridLayoutInput")
        self.gridLayoutInput.setContentsMargins(0, 0, 0, 0)
        self.lblUsername = QLabel(self.layoutWidget1)
        self.lblUsername.setObjectName(u"lblUsername")
        self.lblUsername.setEnabled(True)
        self.lblUsername.setFont(font1)

        self.gridLayoutInput.addWidget(self.lblUsername, 0, 0, 1, 1)

        self.lneUsername = QLineEdit(self.layoutWidget1)
        self.lneUsername.setObjectName(u"lneUsername")
        font2 = QFont()
        font2.setPointSize(14)
        self.lneUsername.setFont(font2)
        self.lneUsername.setMaxLength(20)

        self.gridLayoutInput.addWidget(self.lneUsername, 0, 1, 1, 1)

        self.lblPassword = QLabel(self.layoutWidget1)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setFont(font1)
        self.lblPassword.setStyleSheet(u"color:rgb(255, 0, 0)")

        self.gridLayoutInput.addWidget(self.lblPassword, 1, 0, 1, 1)

        self.lnePassword = QLineEdit(self.layoutWidget1)
        self.lnePassword.setObjectName(u"lnePassword")
        self.lnePassword.setFont(font2)
        self.lnePassword.setMaxLength(50)
        self.lnePassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayoutInput.addWidget(self.lnePassword, 1, 1, 1, 1)


        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"Form", None))
        self.lblManagerMoney.setText(QCoreApplication.translate("LoginScreen", u"Manager Money", None))
        self.btnLogin.setText(QCoreApplication.translate("LoginScreen", u"Login", None))
        self.btnClose.setText(QCoreApplication.translate("LoginScreen", u"Close", None))
        self.lblUsername.setText(QCoreApplication.translate("LoginScreen", u"Username", None))
        self.lblPassword.setText(QCoreApplication.translate("LoginScreen", u"Password", None))
    # retranslateUi

