# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmAddBudget.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_AddBudget(object):
    def setupUi(self, AddBudget):
        if not AddBudget.objectName():
            AddBudget.setObjectName(u"AddBudget")
        AddBudget.resize(574, 597)
        self.lblNewBudget = QLabel(AddBudget)
        self.lblNewBudget.setObjectName(u"lblNewBudget")
        self.lblNewBudget.setGeometry(QRect(140, 30, 301, 51))
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        self.lblNewBudget.setFont(font)
        self.lblNewBudget.setStyleSheet(u"\n"
"font: 36pt \"MV Boli\";\n"
"color:rgb(170, 0, 255)\n"
"\n"
"")
        self.layoutWidget = QWidget(AddBudget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 140, 401, 331))
        self.gridLayoutBugdet = QGridLayout(self.layoutWidget)
        self.gridLayoutBugdet.setObjectName(u"gridLayoutBugdet")
        self.gridLayoutBugdet.setContentsMargins(0, 0, 0, 0)
        self.lblYearBugdet = QLabel(self.layoutWidget)
        self.lblYearBugdet.setObjectName(u"lblYearBugdet")
        font1 = QFont()
        font1.setFamilies([u"Myanmar Texti"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.lblYearBugdet.setFont(font1)
        self.lblYearBugdet.setStyleSheet(u"\n"
"font: 20pt \"Myanmar Texti\";")

        self.gridLayoutBugdet.addWidget(self.lblYearBugdet, 0, 0, 1, 1)

        self.lblAmountBugdet = QLabel(self.layoutWidget)
        self.lblAmountBugdet.setObjectName(u"lblAmountBugdet")
        self.lblAmountBugdet.setFont(font1)
        self.lblAmountBugdet.setStyleSheet(u"\n"
"font: 20pt \"Myanmar Texti\";")

        self.gridLayoutBugdet.addWidget(self.lblAmountBugdet, 6, 0, 1, 1)

        self.txtAmountBugdet = QLineEdit(self.layoutWidget)
        self.txtAmountBugdet.setObjectName(u"txtAmountBugdet")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.txtAmountBugdet.setFont(font2)
        self.txtAmountBugdet.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.txtAmountBugdet.setMaxLength(20)

        self.gridLayoutBugdet.addWidget(self.txtAmountBugdet, 6, 1, 1, 1)

        self.dateYear = QDateEdit(self.layoutWidget)
        self.dateYear.setObjectName(u"dateYear")
        self.dateYear.setStyleSheet(u"font: 18pt \"Segoe UI\";")
        self.dateYear.setDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.dateYear.setMinimumDateTime(QDateTime(QDate(2020, 1, 1), QTime(0, 0, 0)))
        self.dateYear.setMaximumDate(QDate(2100, 12, 31))
        self.dateYear.setMinimumDate(QDate(2020, 1, 1))

        self.gridLayoutBugdet.addWidget(self.dateYear, 0, 1, 1, 1)

        self.lblMonthBugdet = QLabel(self.layoutWidget)
        self.lblMonthBugdet.setObjectName(u"lblMonthBugdet")
        self.lblMonthBugdet.setFont(font1)
        self.lblMonthBugdet.setStyleSheet(u"\n"
"font: 20pt \"Myanmar Texti\";")

        self.gridLayoutBugdet.addWidget(self.lblMonthBugdet, 5, 0, 1, 1)

        self.dateMonthBugdet = QDateEdit(self.layoutWidget)
        self.dateMonthBugdet.setObjectName(u"dateMonthBugdet")
        self.dateMonthBugdet.setStyleSheet(u"font: 18pt \"Segoe UI\";")
        self.dateMonthBugdet.setMaximumDate(QDate(2100, 12, 31))
        self.dateMonthBugdet.setMinimumDate(QDate(2020, 1, 1))
        self.dateMonthBugdet.setCalendarPopup(False)

        self.gridLayoutBugdet.addWidget(self.dateMonthBugdet, 5, 1, 1, 1)

        self.btnCloseBudget = QPushButton(AddBudget)
        self.btnCloseBudget.setObjectName(u"btnCloseBudget")
        self.btnCloseBudget.setGeometry(QRect(280, 500, 151, 61))
        font3 = QFont()
        font3.setFamilies([u"Nirmala UI Semilight"])
        font3.setPointSize(14)
        self.btnCloseBudget.setFont(font3)
        self.btnSaveBudget = QPushButton(AddBudget)
        self.btnSaveBudget.setObjectName(u"btnSaveBudget")
        self.btnSaveBudget.setGeometry(QRect(100, 500, 151, 61))
        self.btnSaveBudget.setFont(font3)

        self.retranslateUi(AddBudget)

        QMetaObject.connectSlotsByName(AddBudget)
    # setupUi

    def retranslateUi(self, AddBudget):
        AddBudget.setWindowTitle(QCoreApplication.translate("AddBudget", u"Dialog", None))
        self.lblNewBudget.setText(QCoreApplication.translate("AddBudget", u"New Budget ", None))
        self.lblYearBugdet.setText(QCoreApplication.translate("AddBudget", u"Year", None))
        self.lblAmountBugdet.setText(QCoreApplication.translate("AddBudget", u"Amount", None))
        self.txtAmountBugdet.setText("")
        self.dateYear.setDisplayFormat(QCoreApplication.translate("AddBudget", u"yyyy", None))
        self.lblMonthBugdet.setText(QCoreApplication.translate("AddBudget", u"Month Budget", None))
        self.dateMonthBugdet.setDisplayFormat(QCoreApplication.translate("AddBudget", u"MM", None))
        self.btnCloseBudget.setText(QCoreApplication.translate("AddBudget", u"Close", None))
        self.btnSaveBudget.setText(QCoreApplication.translate("AddBudget", u"Save", None))
    # retranslateUi

