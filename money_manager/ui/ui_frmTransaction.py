# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmTransaction.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_AddTransaction(object):
    def setupUi(self, AddTransaction):
        if not AddTransaction.objectName():
            AddTransaction.setObjectName(u"AddTransaction")
        AddTransaction.resize(566, 680)
        self.txtAmount = QLineEdit(AddTransaction)
        self.txtAmount.setObjectName(u"txtAmount")
        self.txtAmount.setGeometry(QRect(210, 190, 161, 36))
        font = QFont()
        font.setPointSize(14)
        self.txtAmount.setFont(font)
        self.lblTransaction = QLabel(AddTransaction)
        self.lblTransaction.setObjectName(u"lblTransaction")
        self.lblTransaction.setGeometry(QRect(69, 120, 131, 51))
        self.lblTransaction.setFont(font)
        self.lblBudgetTransaction = QLabel(AddTransaction)
        self.lblBudgetTransaction.setObjectName(u"lblBudgetTransaction")
        self.lblBudgetTransaction.setGeometry(QRect(69, 67, 131, 51))
        self.lblBudgetTransaction.setFont(font)
        self.lblBudget_ = QLabel(AddTransaction)
        self.lblBudget_.setObjectName(u"lblBudget_")
        self.lblBudget_.setGeometry(QRect(210, 80, 49, 16))
        self.lblBudget_.setFont(font)
        self.txtCatagory = QLineEdit(AddTransaction)
        self.txtCatagory.setObjectName(u"txtCatagory")
        self.txtCatagory.setGeometry(QRect(210, 248, 161, 36))
        self.txtCatagory.setFont(font)
        self.lblAmount = QLabel(AddTransaction)
        self.lblAmount.setObjectName(u"lblAmount")
        self.lblAmount.setGeometry(QRect(70, 180, 131, 51))
        self.lblAmount.setFont(font)
        self.lblCatagory = QLabel(AddTransaction)
        self.lblCatagory.setObjectName(u"lblCatagory")
        self.lblCatagory.setGeometry(QRect(70, 240, 131, 51))
        self.lblCatagory.setFont(font)
        self.lblDate = QLabel(AddTransaction)
        self.lblDate.setObjectName(u"lblDate")
        self.lblDate.setGeometry(QRect(80, 300, 81, 51))
        self.lblDate.setFont(font)
        self.txtType = QLineEdit(AddTransaction)
        self.txtType.setObjectName(u"txtType")
        self.txtType.setGeometry(QRect(210, 370, 161, 36))
        self.txtType.setFont(font)
        self.lblType = QLabel(AddTransaction)
        self.lblType.setObjectName(u"lblType")
        self.lblType.setGeometry(QRect(80, 360, 81, 51))
        self.lblType.setFont(font)
        self.lblCurrency = QLabel(AddTransaction)
        self.lblCurrency.setObjectName(u"lblCurrency")
        self.lblCurrency.setGeometry(QRect(70, 420, 81, 51))
        self.lblCurrency.setFont(font)
        self.lblCurrency_ = QLabel(AddTransaction)
        self.lblCurrency_.setObjectName(u"lblCurrency_")
        self.lblCurrency_.setGeometry(QRect(209, 420, 81, 51))
        self.lblCurrency_.setFont(font)
        self.btnSave = QPushButton(AddTransaction)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setGeometry(QRect(120, 600, 151, 61))
        font1 = QFont()
        font1.setFamilies([u"Nirmala UI Semilight"])
        font1.setPointSize(14)
        self.btnSave.setFont(font1)
        self.btnClose = QPushButton(AddTransaction)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(310, 600, 151, 61))
        self.btnClose.setFont(font1)
        self.txtTransaction = QLineEdit(AddTransaction)
        self.txtTransaction.setObjectName(u"txtTransaction")
        self.txtTransaction.setGeometry(QRect(210, 128, 161, 36))
        self.txtTransaction.setFont(font)
        self.txtNote = QTextEdit(AddTransaction)
        self.txtNote.setObjectName(u"txtNote")
        self.txtNote.setGeometry(QRect(120, 490, 361, 101))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.txtNote.setFont(font2)
        self.txtNote.setStyleSheet(u"\n"
"font: 12pt \"Segoe UI\";")
        self.lblNoteTransaction = QLabel(AddTransaction)
        self.lblNoteTransaction.setObjectName(u"lblNoteTransaction")
        self.lblNoteTransaction.setGeometry(QRect(40, 510, 111, 51))
        self.lblNoteTransaction.setFont(font)
        self.lblNoteTransaction.setStyleSheet(u"Color:rgb(0, 255, 0)")
        self.lblNewTransaction = QLabel(AddTransaction)
        self.lblNewTransaction.setObjectName(u"lblNewTransaction")
        self.lblNewTransaction.setGeometry(QRect(150, 20, 231, 51))
        font3 = QFont()
        font3.setFamilies([u"MV Boli"])
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        self.lblNewTransaction.setFont(font3)
        self.lblNewTransaction.setStyleSheet(u"\n"
"font: 20pt \"MV Boli\";\n"
"color:rgb(170, 0, 255)\n"
"\n"
"")
        self.DateTransaction = QDateEdit(AddTransaction)
        self.DateTransaction.setObjectName(u"DateTransaction")
        self.DateTransaction.setGeometry(QRect(210, 310, 171, 41))
        font4 = QFont()
        font4.setPointSize(12)
        self.DateTransaction.setFont(font4)
        self.DateTransaction.setDateTime(QDateTime(QDate(2010, 9, 13), QTime(0, 0, 0)))
        self.DateTransaction.setMaximumDateTime(QDateTime(QDate(2100, 11, 30), QTime(23, 59, 59)))
        self.DateTransaction.setMinimumDateTime(QDateTime(QDate(2009, 12, 31), QTime(0, 0, 0)))
        self.DateTransaction.setMaximumDate(QDate(2100, 11, 30))

        self.retranslateUi(AddTransaction)

        QMetaObject.connectSlotsByName(AddTransaction)
    # setupUi

    def retranslateUi(self, AddTransaction):
        AddTransaction.setWindowTitle(QCoreApplication.translate("AddTransaction", u"Form", None))
        self.lblTransaction.setText(QCoreApplication.translate("AddTransaction", u"Transaction", None))
        self.lblBudgetTransaction.setText(QCoreApplication.translate("AddTransaction", u"Budget", None))
        self.lblBudget_.setText(QCoreApplication.translate("AddTransaction", u"???", None))
        self.lblAmount.setText(QCoreApplication.translate("AddTransaction", u"Amount", None))
        self.lblCatagory.setText(QCoreApplication.translate("AddTransaction", u"Catagory", None))
        self.lblDate.setText(QCoreApplication.translate("AddTransaction", u"Date", None))
        self.lblType.setText(QCoreApplication.translate("AddTransaction", u"Type", None))
        self.lblCurrency.setText(QCoreApplication.translate("AddTransaction", u"Currency", None))
        self.lblCurrency_.setText(QCoreApplication.translate("AddTransaction", u"Currency", None))
        self.btnSave.setText(QCoreApplication.translate("AddTransaction", u"Save", None))
        self.btnClose.setText(QCoreApplication.translate("AddTransaction", u"Close", None))
        self.lblNoteTransaction.setText(QCoreApplication.translate("AddTransaction", u"Note", None))
        self.lblNewTransaction.setText(QCoreApplication.translate("AddTransaction", u"New Transaction ", None))
        self.DateTransaction.setDisplayFormat(QCoreApplication.translate("AddTransaction", u"DD-MMM-yyyy", None))
    # retranslateUi

