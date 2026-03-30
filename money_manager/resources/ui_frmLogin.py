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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        if not LoginScreen.objectName():
            LoginScreen.setObjectName(u"LoginScreen")
        LoginScreen.resize(474, 340)
        LoginScreen.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.btnLogin = QPushButton(LoginScreen)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(100, 240, 151, 61))
        font = QFont()
        font.setFamilies([u"Nirmala UI Semilight"])
        font.setPointSize(14)
        self.btnLogin.setFont(font)
        self.lblUsername = QLabel(LoginScreen)
        self.lblUsername.setObjectName(u"lblUsername")
        self.lblUsername.setEnabled(True)
        self.lblUsername.setGeometry(QRect(90, 120, 91, 21))
        self.lblUsername.setFont(font)
        self.lblPassword = QLabel(LoginScreen)
        self.lblPassword.setObjectName(u"lblPassword")
        self.lblPassword.setGeometry(QRect(90, 170, 91, 21))
        self.lblPassword.setFont(font)
        self.lblPassword.setStyleSheet(u"color:rgb(255, 0, 0)")
        self.lneUsername = QLineEdit(LoginScreen)
        self.lneUsername.setObjectName(u"lneUsername")
        self.lneUsername.setGeometry(QRect(210, 120, 161, 31))
        self.lnePassword = QLineEdit(LoginScreen)
        self.lnePassword.setObjectName(u"lnePassword")
        self.lnePassword.setGeometry(QRect(210, 170, 161, 31))
        self.lnePassword.setEchoMode(QLineEdit.EchoMode.Password)
        self.btnClose = QPushButton(LoginScreen)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(270, 240, 151, 61))
        self.btnClose.setFont(font)
        self.lblManagerMoney = QLabel(LoginScreen)
        self.lblManagerMoney.setObjectName(u"lblManagerMoney")
        self.lblManagerMoney.setEnabled(True)
        self.lblManagerMoney.setGeometry(QRect(130, 20, 301, 71))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(28)
        font1.setBold(False)
        font1.setItalic(False)
        self.lblManagerMoney.setFont(font1)
        self.lblManagerMoney.setStyleSheet(u"color:rgb(85, 0, 255);\n"
"font: 28pt \"Segoe UI\";")

        self.retranslateUi(LoginScreen)

        QMetaObject.connectSlotsByName(LoginScreen)
# ── Error Label ───────────────────────────────────────────
        self.lblError = QLabel(LoginScreen)
        self.lblError.setGeometry(QRect(60, 215, 360, 25))
        self.lblError.setStyleSheet("color: red;")
        self.lblError.setObjectName("lblError")
        self.lblError.setText("")
    # setupUi

    def retranslateUi(self, LoginScreen):
        LoginScreen.setWindowTitle(QCoreApplication.translate("LoginScreen", u"Form", None))
        self.btnLogin.setText(QCoreApplication.translate("LoginScreen", u"Login", None))
        self.lblUsername.setText(QCoreApplication.translate("LoginScreen", u"Username", None))
        self.lblPassword.setText(QCoreApplication.translate("LoginScreen", u"Password", None))
        self.btnClose.setText(QCoreApplication.translate("LoginScreen", u"Close", None))
        self.lblManagerMoney.setText(QCoreApplication.translate("LoginScreen", u"Manager Money", None))
    # retranslateUi

