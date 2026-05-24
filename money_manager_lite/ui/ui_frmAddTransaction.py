# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_frmAddTransaction.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_AddTransaction(object):
    def setupUi(self, AddTransaction):
        if not AddTransaction.objectName():
            AddTransaction.setObjectName(u"AddTransaction")
        AddTransaction.resize(543, 737)
        self.btnCloseTransaction = QPushButton(AddTransaction)
        self.btnCloseTransaction.setObjectName(u"btnCloseTransaction")
        self.btnCloseTransaction.setGeometry(QRect(280, 640, 151, 61))
        font = QFont()
        font.setFamilies([u"Nirmala UI Semilight"])
        font.setPointSize(14)
        self.btnCloseTransaction.setFont(font)
        self.layoutWidget = QWidget(AddTransaction)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 120, 441, 401))
        self.gridLayoutTransaction = QGridLayout(self.layoutWidget)
        self.gridLayoutTransaction.setObjectName(u"gridLayoutTransaction")
        self.gridLayoutTransaction.setContentsMargins(0, 0, 0, 0)
        self.txtAmountTransaction = QLineEdit(self.layoutWidget)
        self.txtAmountTransaction.setObjectName(u"txtAmountTransaction")
        font1 = QFont()
        font1.setPointSize(18)
        self.txtAmountTransaction.setFont(font1)
        self.txtAmountTransaction.setMaxLength(20)

        self.gridLayoutTransaction.addWidget(self.txtAmountTransaction, 0, 1, 1, 1)

        self.cmbboxCatagory = QComboBox(self.layoutWidget)
        self.cmbboxCatagory.addItem("")
        self.cmbboxCatagory.addItem("")
        self.cmbboxCatagory.addItem("")
        self.cmbboxCatagory.addItem("")
        self.cmbboxCatagory.addItem("")
        self.cmbboxCatagory.addItem("")
        self.cmbboxCatagory.addItem("")
        self.cmbboxCatagory.setObjectName(u"cmbboxCatagory")
        self.cmbboxCatagory.setFont(font1)
        self.cmbboxCatagory.setMaxCount(50)

        self.gridLayoutTransaction.addWidget(self.cmbboxCatagory, 1, 1, 1, 1)

        self.dateYearTransaction = QDateEdit(self.layoutWidget)
        self.dateYearTransaction.setObjectName(u"dateYearTransaction")
        self.dateYearTransaction.setStyleSheet(u"font: 18pt \"Segoe UI\";")
        self.dateYearTransaction.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.dateYearTransaction.setMinimumDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.dateYearTransaction.setMaximumDate(QDate(2100, 12, 31))
        self.dateYearTransaction.setMinimumDate(QDate(2020, 1, 1))

        self.gridLayoutTransaction.addWidget(self.dateYearTransaction, 3, 1, 1, 1)

        self.dateMonthTransaction = QDateEdit(self.layoutWidget)
        self.dateMonthTransaction.setObjectName(u"dateMonthTransaction")
        self.dateMonthTransaction.setStyleSheet(u"font: 18pt \"Segoe UI\";")
        self.dateMonthTransaction.setMaximumDate(QDate(2100, 12, 31))
        self.dateMonthTransaction.setMinimumDate(QDate(2020, 1, 1))
        self.dateMonthTransaction.setCalendarPopup(False)

        self.gridLayoutTransaction.addWidget(self.dateMonthTransaction, 2, 1, 1, 1)

        self.lblYear = QLabel(self.layoutWidget)
        self.lblYear.setObjectName(u"lblYear")
        self.lblYear.setFont(font1)

        self.gridLayoutTransaction.addWidget(self.lblYear, 3, 0, 1, 1)

        self.lblAmountTransaction = QLabel(self.layoutWidget)
        self.lblAmountTransaction.setObjectName(u"lblAmountTransaction")
        self.lblAmountTransaction.setFont(font1)

        self.gridLayoutTransaction.addWidget(self.lblAmountTransaction, 0, 0, 1, 1)

        self.lblCatagory = QLabel(self.layoutWidget)
        self.lblCatagory.setObjectName(u"lblCatagory")
        self.lblCatagory.setFont(font1)

        self.gridLayoutTransaction.addWidget(self.lblCatagory, 1, 0, 1, 1)

        self.lblMonth = QLabel(self.layoutWidget)
        self.lblMonth.setObjectName(u"lblMonth")
        self.lblMonth.setFont(font1)

        self.gridLayoutTransaction.addWidget(self.lblMonth, 2, 0, 1, 1)

        self.lblNewTransaction = QLabel(AddTransaction)
        self.lblNewTransaction.setObjectName(u"lblNewTransaction")
        self.lblNewTransaction.setGeometry(QRect(70, 40, 401, 81))
        font2 = QFont()
        font2.setFamilies([u"MV Boli"])
        font2.setPointSize(36)
        font2.setBold(False)
        font2.setItalic(False)
        self.lblNewTransaction.setFont(font2)
        self.lblNewTransaction.setStyleSheet(u"\n"
"font: 36pt \"MV Boli\";\n"
"color:rgb(170, 0, 255)\n"
"\n"
"")
        self.btnSaveTransaction = QPushButton(AddTransaction)
        self.btnSaveTransaction.setObjectName(u"btnSaveTransaction")
        self.btnSaveTransaction.setGeometry(QRect(100, 640, 151, 61))
        self.btnSaveTransaction.setFont(font)
        self.layoutWidget1 = QWidget(AddTransaction)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(50, 550, 441, 61))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lblTotalAmountBudgetHave = QLabel(self.layoutWidget1)
        self.lblTotalAmountBudgetHave.setObjectName(u"lblTotalAmountBudgetHave")
        self.lblTotalAmountBudgetHave.setFont(font1)

        self.gridLayout.addWidget(self.lblTotalAmountBudgetHave, 0, 0, 1, 1)

        self.lblTotalAmountBudget = QLabel(self.layoutWidget1)
        self.lblTotalAmountBudget.setObjectName(u"lblTotalAmountBudget")
        self.lblTotalAmountBudget.setFont(font1)

        self.gridLayout.addWidget(self.lblTotalAmountBudget, 0, 1, 1, 1)


        self.retranslateUi(AddTransaction)

        QMetaObject.connectSlotsByName(AddTransaction)
    # setupUi

    def retranslateUi(self, AddTransaction):
        AddTransaction.setWindowTitle(QCoreApplication.translate("AddTransaction", u"Dialog", None))
        self.btnCloseTransaction.setText(QCoreApplication.translate("AddTransaction", u"Close", None))
        self.cmbboxCatagory.setItemText(0, QCoreApplication.translate("AddTransaction", u"Food", None))
        self.cmbboxCatagory.setItemText(1, QCoreApplication.translate("AddTransaction", u"Transport", None))
        self.cmbboxCatagory.setItemText(2, QCoreApplication.translate("AddTransaction", u"Entertainment", None))
        self.cmbboxCatagory.setItemText(3, QCoreApplication.translate("AddTransaction", u"Shopping", None))
        self.cmbboxCatagory.setItemText(4, QCoreApplication.translate("AddTransaction", u"Education", None))
        self.cmbboxCatagory.setItemText(5, QCoreApplication.translate("AddTransaction", u"Health", None))
        self.cmbboxCatagory.setItemText(6, QCoreApplication.translate("AddTransaction", u"Other", None))

        self.dateYearTransaction.setDisplayFormat(QCoreApplication.translate("AddTransaction", u"yyyy", None))
        self.dateMonthTransaction.setDisplayFormat(QCoreApplication.translate("AddTransaction", u"MM", None))
        self.lblYear.setText(QCoreApplication.translate("AddTransaction", u"Year", None))
        self.lblAmountTransaction.setText(QCoreApplication.translate("AddTransaction", u"Amount", None))
        self.lblCatagory.setText(QCoreApplication.translate("AddTransaction", u"Catagory", None))
        self.lblMonth.setText(QCoreApplication.translate("AddTransaction", u"Month", None))
        self.lblNewTransaction.setText(QCoreApplication.translate("AddTransaction", u"New Transaction ", None))
        self.btnSaveTransaction.setText(QCoreApplication.translate("AddTransaction", u"Save", None))
        self.lblTotalAmountBudgetHave.setText(QCoreApplication.translate("AddTransaction", u"Available Balance", None))
        self.lblTotalAmountBudget.setText(QCoreApplication.translate("AddTransaction", u"???", None))
    # retranslateUi

