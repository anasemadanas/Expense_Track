# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmListTransaction.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_ListTransaction(object):
    def setupUi(self, ListTransaction):
        if not ListTransaction.objectName():
            ListTransaction.setObjectName(u"ListTransaction")
        ListTransaction.resize(900, 618)
        self.tableWidgetTransaction = QTableWidget(ListTransaction)
        self.tableWidgetTransaction.setObjectName(u"tableWidgetTransaction")
        self.tableWidgetTransaction.setGeometry(QRect(20, 150, 861, 361))
        self.tableWidgetTransaction.setMinimumSize(QSize(621, 0))
        self.tableWidgetTransaction.setStyleSheet(u"\n"
"font: 14pt \"Segoe UI\";")
        self.layoutWidget = QWidget(ListTransaction)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(200, 530, 431, 81))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnSaveList = QPushButton(self.layoutWidget)
        self.btnSaveList.setObjectName(u"btnSaveList")
        font = QFont()
        font.setFamilies([u"Nirmala UI Semilight"])
        font.setPointSize(14)
        self.btnSaveList.setFont(font)

        self.horizontalLayout.addWidget(self.btnSaveList)

        self.btnCloseList = QPushButton(self.layoutWidget)
        self.btnCloseList.setObjectName(u"btnCloseList")
        self.btnCloseList.setFont(font)

        self.horizontalLayout.addWidget(self.btnCloseList)

        self.lblTitleListTransaction = QLabel(ListTransaction)
        self.lblTitleListTransaction.setObjectName(u"lblTitleListTransaction")
        self.lblTitleListTransaction.setEnabled(True)
        self.lblTitleListTransaction.setGeometry(QRect(180, 60, 501, 61))
        font1 = QFont()
        font1.setFamilies([u"MV Boli"])
        font1.setPointSize(40)
        font1.setBold(False)
        font1.setItalic(False)
        self.lblTitleListTransaction.setFont(font1)
        self.lblTitleListTransaction.setStyleSheet(u"\n"
"font: 40pt \"MV Boli\";")

        self.retranslateUi(ListTransaction)

        QMetaObject.connectSlotsByName(ListTransaction)
    # setupUi

    def retranslateUi(self, ListTransaction):
        ListTransaction.setWindowTitle(QCoreApplication.translate("ListTransaction", u"Dialog", None))
        self.btnSaveList.setText(QCoreApplication.translate("ListTransaction", u"Save", None))
        self.btnCloseList.setText(QCoreApplication.translate("ListTransaction", u"Close", None))
        self.lblTitleListTransaction.setText(QCoreApplication.translate("ListTransaction", u"List All Transaction", None))
    # retranslateUi

