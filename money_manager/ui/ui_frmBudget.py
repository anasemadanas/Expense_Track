# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmBudget.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialogButtonBox, QLabel,
    QLineEdit, QSizePolicy, QTextEdit, QWidget)

class Ui_AddBudget(object):
    def setupUi(self, AddBudget):
        if not AddBudget.objectName():
            AddBudget.setObjectName(u"AddBudget")
        AddBudget.resize(520, 604)
        self.btnOkCnacel = QDialogButtonBox(AddBudget)
        self.btnOkCnacel.setObjectName(u"btnOkCnacel")
        self.btnOkCnacel.setGeometry(QRect(150, 520, 211, 51))
        font = QFont()
        font.setPointSize(14)
        self.btnOkCnacel.setFont(font)
        self.btnOkCnacel.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.txtNote = QTextEdit(AddBudget)
        self.txtNote.setObjectName(u"txtNote")
        self.txtNote.setGeometry(QRect(140, 390, 361, 101))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.txtNote.setFont(font1)
        self.txtNote.setStyleSheet(u"\n"
"font: 12pt \"Segoe UI\";")
        self.lblBudget = QLabel(AddBudget)
        self.lblBudget.setObjectName(u"lblBudget")
        self.lblBudget.setGeometry(QRect(90, 100, 60, 26))
        self.lblBudget.setFont(font)
        self.lblBudget.setStyleSheet(u"Color:rgb(0, 255, 0)")
        self.lblNote = QLabel(AddBudget)
        self.lblNote.setObjectName(u"lblNote")
        self.lblNote.setGeometry(QRect(60, 410, 111, 51))
        self.lblNote.setFont(font)
        self.lblNote.setStyleSheet(u"Color:rgb(0, 255, 0)")
        self.lblAmount = QLabel(AddBudget)
        self.lblAmount.setObjectName(u"lblAmount")
        self.lblAmount.setGeometry(QRect(90, 170, 67, 26))
        self.lblAmount.setFont(font)
        self.lblAmount.setStyleSheet(u"color:rgb(85, 255, 0)")
        self.lblSpent = QLabel(AddBudget)
        self.lblSpent.setObjectName(u"lblSpent")
        self.lblSpent.setGeometry(QRect(90, 240, 48, 26))
        self.lblSpent.setFont(font)
        self.lblSpent.setStyleSheet(u"Color:rgb(0, 255, 0)")
        self.lblPeriod = QLabel(AddBudget)
        self.lblPeriod.setObjectName(u"lblPeriod")
        self.lblPeriod.setGeometry(QRect(90, 310, 54, 26))
        self.lblPeriod.setFont(font)
        self.lblPeriod.setStyleSheet(u"Color:rgb(0, 255, 0)")
        self.txtAmount = QLineEdit(AddBudget)
        self.txtAmount.setObjectName(u"txtAmount")
        self.txtAmount.setGeometry(QRect(200, 170, 161, 36))
        self.txtAmount.setFont(font1)
        self.txtAmount.setStyleSheet(u"font: 12pt \"Arial\";\n"
"font: 12pt \"Segoe UI\";")
        self.txtSpent = QLineEdit(AddBudget)
        self.txtSpent.setObjectName(u"txtSpent")
        self.txtSpent.setGeometry(QRect(200, 240, 161, 36))
        self.txtSpent.setFont(font1)
        self.txtSpent.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.lblNewBudget = QLabel(AddBudget)
        self.lblNewBudget.setObjectName(u"lblNewBudget")
        self.lblNewBudget.setGeometry(QRect(170, 30, 201, 51))
        font2 = QFont()
        font2.setFamilies([u"MV Boli"])
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        self.lblNewBudget.setFont(font2)
        self.lblNewBudget.setStyleSheet(u"\n"
"font: 20pt \"MV Boli\";\n"
"color:rgb(170, 0, 255)\n"
"\n"
"")
        self.txtPeriod = QLineEdit(AddBudget)
        self.txtPeriod.setObjectName(u"txtPeriod")
        self.txtPeriod.setGeometry(QRect(200, 310, 161, 36))
        self.txtPeriod.setFont(font1)
        self.txtPeriod.setStyleSheet(u"font: 12pt \"Segoe UI\";")
        self.txtBudget = QLineEdit(AddBudget)
        self.txtBudget.setObjectName(u"txtBudget")
        self.txtBudget.setGeometry(QRect(200, 100, 161, 36))
        self.txtBudget.setFont(font1)
        self.txtBudget.setStyleSheet(u"font: 12pt \"Segoe UI\";")

        self.retranslateUi(AddBudget)

        QMetaObject.connectSlotsByName(AddBudget)
    # setupUi

    def retranslateUi(self, AddBudget):
        AddBudget.setWindowTitle(QCoreApplication.translate("AddBudget", u"Form", None))
        self.lblBudget.setText(QCoreApplication.translate("AddBudget", u"Budget", None))
        self.lblNote.setText(QCoreApplication.translate("AddBudget", u"Note", None))
        self.lblAmount.setText(QCoreApplication.translate("AddBudget", u"Amount", None))
        self.lblSpent.setText(QCoreApplication.translate("AddBudget", u"Spent", None))
        self.lblPeriod.setText(QCoreApplication.translate("AddBudget", u"Period", None))
        self.txtSpent.setText("")
        self.lblNewBudget.setText(QCoreApplication.translate("AddBudget", u"New Budget ", None))
    # retranslateUi

