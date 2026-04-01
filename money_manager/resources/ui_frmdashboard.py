# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmdashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QStackedWidget, QStatusBar,
    QVBoxLayout, QWidget)
import Resources_rc

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        if not MainScreen.objectName():
            MainScreen.setObjectName(u"MainScreen")
        MainScreen.setEnabled(True)
        MainScreen.resize(952, 827)
        MainScreen.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks)
        MainScreen.setUnifiedTitleAndToolBarOnMac(False)
        self.actSave = QAction(MainScreen)
        self.actSave.setObjectName(u"actSave")
        self.actExit = QAction(MainScreen)
        self.actExit.setObjectName(u"actExit")
        self.actAbout = QAction(MainScreen)
        self.actAbout.setObjectName(u"actAbout")
        self.actExport = QAction(MainScreen)
        self.actExport.setObjectName(u"actExport")
        self.actGuide = QAction(MainScreen)
        self.actGuide.setObjectName(u"actGuide")
        self.centralwidget = QWidget(MainScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblTitleDashBoard = QLabel(self.centralwidget)
        self.lblTitleDashBoard.setObjectName(u"lblTitleDashBoard")
        self.lblTitleDashBoard.setEnabled(True)
        self.lblTitleDashBoard.setGeometry(QRect(260, 0, 371, 111))
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(58)
        font.setBold(False)
        font.setItalic(False)
        self.lblTitleDashBoard.setFont(font)
        self.lblTitleDashBoard.setStyleSheet(u"color:rgb(85, 0, 255);\n"
"font: 58pt \"MV Boli\";")
        self.stackedWidgetChart = QStackedWidget(self.centralwidget)
        self.stackedWidgetChart.setObjectName(u"stackedWidgetChart")
        self.stackedWidgetChart.setGeometry(QRect(70, 510, 811, 251))
        self.pageSpending_1 = QWidget()
        self.pageSpending_1.setObjectName(u"pageSpending_1")
        self.gvPieChart = QGraphicsView(self.pageSpending_1)
        self.gvPieChart.setObjectName(u"gvPieChart")
        self.gvPieChart.setGeometry(QRect(220, 30, 581, 221))
        self.layoutWidget = QWidget(self.pageSpending_1)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 201, 221))
        self.hlSpendingInfo = QHBoxLayout(self.layoutWidget)
        self.hlSpendingInfo.setObjectName(u"hlSpendingInfo")
        self.hlSpendingInfo.setContentsMargins(0, 0, 0, 0)
        self.vlSpendingInfo = QVBoxLayout()
        self.vlSpendingInfo.setObjectName(u"vlSpendingInfo")
        self.lblSpendingAmount = QLabel(self.layoutWidget)
        self.lblSpendingAmount.setObjectName(u"lblSpendingAmount")
        self.lblSpendingAmount.setStyleSheet(u"font:20px;\n"
"color:rgb(255, 255, 0)")

        self.vlSpendingInfo.addWidget(self.lblSpendingAmount)

        self.lblSpendingSpent = QLabel(self.layoutWidget)
        self.lblSpendingSpent.setObjectName(u"lblSpendingSpent")
        self.lblSpendingSpent.setStyleSheet(u"font:20px;\n"
"color:rgb(255, 255, 0)")

        self.vlSpendingInfo.addWidget(self.lblSpendingSpent)

        self.lblSpendingPeriod = QLabel(self.layoutWidget)
        self.lblSpendingPeriod.setObjectName(u"lblSpendingPeriod")
        self.lblSpendingPeriod.setStyleSheet(u"font:20px;\n"
"color:rgb(255, 255, 0)")

        self.vlSpendingInfo.addWidget(self.lblSpendingPeriod)

        self.lblSpendingBudget = QLabel(self.layoutWidget)
        self.lblSpendingBudget.setObjectName(u"lblSpendingBudget")
        self.lblSpendingBudget.setStyleSheet(u"font:20px;\n"
"color:rgb(255, 255, 0)")

        self.vlSpendingInfo.addWidget(self.lblSpendingBudget)


        self.hlSpendingInfo.addLayout(self.vlSpendingInfo)

        self.vlSpendingCalc = QVBoxLayout()
        self.vlSpendingCalc.setObjectName(u"vlSpendingCalc")
        self.lblAmountTotal = QLabel(self.layoutWidget)
        self.lblAmountTotal.setObjectName(u"lblAmountTotal")
        self.lblAmountTotal.setStyleSheet(u"font:20px;\n"
"color:rgb(255, 255, 0)")

        self.vlSpendingCalc.addWidget(self.lblAmountTotal)

        self.lblSpentTotal = QLabel(self.layoutWidget)
        self.lblSpentTotal.setObjectName(u"lblSpentTotal")
        self.lblSpentTotal.setStyleSheet(u"font:20px;\n"
"color:rgb(255, 255, 0)")

        self.vlSpendingCalc.addWidget(self.lblSpentTotal)

        self.lblPeriodTotal = QLabel(self.layoutWidget)
        self.lblPeriodTotal.setObjectName(u"lblPeriodTotal")
        self.lblPeriodTotal.setStyleSheet(u"font:20px;\n"
"color:rgb(255, 255, 0)")

        self.vlSpendingCalc.addWidget(self.lblPeriodTotal)

        self.lbl_BudgetTotal = QLabel(self.layoutWidget)
        self.lbl_BudgetTotal.setObjectName(u"lbl_BudgetTotal")
        self.lbl_BudgetTotal.setStyleSheet(u"font:20px;\n"
"color:rgb(255, 255, 0)")

        self.vlSpendingCalc.addWidget(self.lbl_BudgetTotal)


        self.hlSpendingInfo.addLayout(self.vlSpendingCalc)

        self.stackedWidgetChart.addWidget(self.pageSpending_1)
        self.pageLineGraph_3 = QWidget()
        self.pageLineGraph_3.setObjectName(u"pageLineGraph_3")
        self.gvLineGraph = QGraphicsView(self.pageLineGraph_3)
        self.gvLineGraph.setObjectName(u"gvLineGraph")
        self.gvLineGraph.setGeometry(QRect(0, 30, 801, 221))
        self.stackedWidgetChart.addWidget(self.pageLineGraph_3)
        self.pageBudget_2 = QWidget()
        self.pageBudget_2.setObjectName(u"pageBudget_2")
        self.gvBarChart = QGraphicsView(self.pageBudget_2)
        self.gvBarChart.setObjectName(u"gvBarChart")
        self.gvBarChart.setGeometry(QRect(0, 30, 801, 221))
        self.stackedWidgetChart.addWidget(self.pageBudget_2)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(70, 460, 811, 44))
        self.hlChart = QHBoxLayout(self.layoutWidget1)
        self.hlChart.setObjectName(u"hlChart")
        self.hlChart.setContentsMargins(0, 0, 0, 0)
        self.btnSpending = QPushButton(self.layoutWidget1)
        self.btnSpending.setObjectName(u"btnSpending")
        self.btnSpending.setTabletTracking(False)
        self.btnSpending.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/piechart_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSpending.setIcon(icon)
        self.btnSpending.setCheckable(True)
        self.btnSpending.setChecked(True)
        self.btnSpending.setAutoRepeat(False)
        self.btnSpending.setAutoExclusive(True)

        self.hlChart.addWidget(self.btnSpending)

        self.btnBudgetProgress = QPushButton(self.layoutWidget1)
        self.btnBudgetProgress.setObjectName(u"btnBudgetProgress")
        icon1 = QIcon()
        icon1.addFile(u":/icons/barchart_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBudgetProgress.setIcon(icon1)
        self.btnBudgetProgress.setCheckable(True)
        self.btnBudgetProgress.setChecked(False)
        self.btnBudgetProgress.setAutoRepeat(False)
        self.btnBudgetProgress.setAutoExclusive(True)

        self.hlChart.addWidget(self.btnBudgetProgress)

        self.btnLineGraphinDate = QPushButton(self.layoutWidget1)
        self.btnLineGraphinDate.setObjectName(u"btnLineGraphinDate")
        self.btnLineGraphinDate.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/linegraph_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLineGraphinDate.setIcon(icon2)
        self.btnLineGraphinDate.setCheckable(True)
        self.btnLineGraphinDate.setChecked(False)
        self.btnLineGraphinDate.setAutoRepeat(False)
        self.btnLineGraphinDate.setAutoExclusive(True)

        self.hlChart.addWidget(self.btnLineGraphinDate)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 130, 321, 52))
        self.hlTotalBlalance = QHBoxLayout(self.layoutWidget_2)
        self.hlTotalBlalance.setObjectName(u"hlTotalBlalance")
        self.hlTotalBlalance.setContentsMargins(0, 0, 0, 0)
        self.lblTotalBalance = QLabel(self.layoutWidget_2)
        self.lblTotalBalance.setObjectName(u"lblTotalBalance")
        self.lblTotalBalance.setEnabled(True)
        font1 = QFont()
        font1.setFamilies([u"Mudir MT"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.lblTotalBalance.setFont(font1)
        self.lblTotalBalance.setStyleSheet(u"color:rgb(85, 255, 255);\n"
"font: 20pt ;")

        self.hlTotalBlalance.addWidget(self.lblTotalBalance)

        self.lblTotalBalanceCalc = QLabel(self.layoutWidget_2)
        self.lblTotalBalanceCalc.setObjectName(u"lblTotalBalanceCalc")
        self.lblTotalBalanceCalc.setEnabled(True)
        font2 = QFont()
        font2.setFamilies([u"Modir MT"])
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setItalic(False)
        self.lblTotalBalanceCalc.setFont(font2)
        self.lblTotalBalanceCalc.setStyleSheet(u"color:rgb(85, 255, 255);\n"
"font: 20pt \"Modir MT\";")

        self.hlTotalBlalance.addWidget(self.lblTotalBalanceCalc)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(650, 130, 251, 261))
        self.vlbtnAdd = QVBoxLayout(self.layoutWidget2)
        self.vlbtnAdd.setObjectName(u"vlbtnAdd")
        self.vlbtnAdd.setContentsMargins(0, 0, 0, 0)
        self.btnAddTransaction = QPushButton(self.layoutWidget2)
        self.btnAddTransaction.setObjectName(u"btnAddTransaction")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        self.btnAddTransaction.setFont(font3)
        self.btnAddTransaction.setStyleSheet(u"font: 20pt \"Segoe UI\";\n"
"color:rgb(0, 255, 0);")

        self.vlbtnAdd.addWidget(self.btnAddTransaction)

        self.btnAddBudget = QPushButton(self.layoutWidget2)
        self.btnAddBudget.setObjectName(u"btnAddBudget")
        self.btnAddBudget.setFont(font3)
        self.btnAddBudget.setStyleSheet(u"color:rgb(0, 255, 0);\n"
"font: 20pt \"Segoe UI\";")

        self.vlbtnAdd.addWidget(self.btnAddBudget)

        self.btnExit = QPushButton(self.layoutWidget2)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setFont(font3)
        self.btnExit.setStyleSheet(u"color:rgb(0, 255, 0);\n"
"font: 20pt \"Segoe UI\";")

        self.vlbtnAdd.addWidget(self.btnExit)

        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(30, 210, 321, 224))
        self.vlThisMonth = QVBoxLayout(self.layoutWidget3)
        self.vlThisMonth.setObjectName(u"vlThisMonth")
        self.vlThisMonth.setContentsMargins(0, 0, 0, 0)
        self.lblThisMonth = QLabel(self.layoutWidget3)
        self.lblThisMonth.setObjectName(u"lblThisMonth")
        self.lblThisMonth.setEnabled(True)
        font4 = QFont()
        font4.setFamilies([u"MV Boli"])
        font4.setPointSize(36)
        font4.setBold(False)
        font4.setItalic(False)
        self.lblThisMonth.setFont(font4)
        self.lblThisMonth.setStyleSheet(u"color:rgb(85, 255, 255);\n"
"font: 36pt \"MV Boli\";")

        self.vlThisMonth.addWidget(self.lblThisMonth)

        self.hlCurrentBlalance = QHBoxLayout()
        self.hlCurrentBlalance.setObjectName(u"hlCurrentBlalance")
        self.lblCurrentBalance = QLabel(self.layoutWidget3)
        self.lblCurrentBalance.setObjectName(u"lblCurrentBalance")
        self.lblCurrentBalance.setEnabled(True)
        self.lblCurrentBalance.setFont(font1)
        self.lblCurrentBalance.setStyleSheet(u"color:rgb(85, 255, 255);\n"
"font: 20pt ;")

        self.hlCurrentBlalance.addWidget(self.lblCurrentBalance)

        self.lblCurrentBalanceCalc = QLabel(self.layoutWidget3)
        self.lblCurrentBalanceCalc.setObjectName(u"lblCurrentBalanceCalc")
        self.lblCurrentBalanceCalc.setEnabled(True)
        self.lblCurrentBalanceCalc.setFont(font2)
        self.lblCurrentBalanceCalc.setStyleSheet(u"color:rgb(85, 255, 255);\n"
"font: 20pt \"Modir MT\";")

        self.hlCurrentBlalance.addWidget(self.lblCurrentBalanceCalc)


        self.vlThisMonth.addLayout(self.hlCurrentBlalance)

        self.vlThisMonthSub = QVBoxLayout()
        self.vlThisMonthSub.setObjectName(u"vlThisMonthSub")
        self.hlExpense = QHBoxLayout()
        self.hlExpense.setObjectName(u"hlExpense")
        self.lblExpense = QLabel(self.layoutWidget3)
        self.lblExpense.setObjectName(u"lblExpense")
        font5 = QFont()
        font5.setPointSize(14)
        self.lblExpense.setFont(font5)

        self.hlExpense.addWidget(self.lblExpense)

        self.pbExpense = QProgressBar(self.layoutWidget3)
        self.pbExpense.setObjectName(u"pbExpense")
        self.pbExpense.setFont(font5)
        self.pbExpense.setValue(24)

        self.hlExpense.addWidget(self.pbExpense)


        self.vlThisMonthSub.addLayout(self.hlExpense)

        self.hlEarn = QHBoxLayout()
        self.hlEarn.setObjectName(u"hlEarn")
        self.lblEarn = QLabel(self.layoutWidget3)
        self.lblEarn.setObjectName(u"lblEarn")
        self.lblEarn.setFont(font5)

        self.hlEarn.addWidget(self.lblEarn)

        self.pbEarn = QProgressBar(self.layoutWidget3)
        self.pbEarn.setObjectName(u"pbEarn")
        self.pbEarn.setFont(font5)
        self.pbEarn.setValue(24)

        self.hlEarn.addWidget(self.pbEarn)


        self.vlThisMonthSub.addLayout(self.hlEarn)


        self.vlThisMonth.addLayout(self.vlThisMonthSub)

        MainScreen.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainScreen)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 952, 33))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuHel = QMenu(self.menubar)
        self.menuHel.setObjectName(u"menuHel")
        MainScreen.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainScreen)
        self.statusbar.setObjectName(u"statusbar")
        MainScreen.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.btnAddTransaction, self.btnExit)
        QWidget.setTabOrder(self.btnExit, self.btnSpending)
        QWidget.setTabOrder(self.btnSpending, self.btnBudgetProgress)
        QWidget.setTabOrder(self.btnBudgetProgress, self.btnLineGraphinDate)
        QWidget.setTabOrder(self.btnLineGraphinDate, self.gvLineGraph)
        QWidget.setTabOrder(self.gvLineGraph, self.gvBarChart)
        QWidget.setTabOrder(self.gvBarChart, self.gvPieChart)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHel.menuAction())
        self.menuFile.addAction(self.actSave)
        self.menuFile.addAction(self.actExit)
        self.menuEdit.addAction(self.actExport)
        self.menuHel.addAction(self.actAbout)
        self.menuHel.addAction(self.actGuide)

        self.retranslateUi(MainScreen)

        self.stackedWidgetChart.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainScreen)
    # setupUi

    def retranslateUi(self, MainScreen):
        MainScreen.setWindowTitle(QCoreApplication.translate("MainScreen", u"MainWindow", None))
        self.actSave.setText(QCoreApplication.translate("MainScreen", u"Save", None))
        self.actExit.setText(QCoreApplication.translate("MainScreen", u"Exit", None))
        self.actAbout.setText(QCoreApplication.translate("MainScreen", u"About", None))
        self.actExport.setText(QCoreApplication.translate("MainScreen", u"Export", None))
        self.actGuide.setText(QCoreApplication.translate("MainScreen", u"Guide", None))
        self.lblTitleDashBoard.setText(QCoreApplication.translate("MainScreen", u"DashBoard", None))
        self.lblSpendingAmount.setText(QCoreApplication.translate("MainScreen", u"Amount", None))
        self.lblSpendingSpent.setText(QCoreApplication.translate("MainScreen", u"spent", None))
        self.lblSpendingPeriod.setText(QCoreApplication.translate("MainScreen", u"period", None))
        self.lblSpendingBudget.setText(QCoreApplication.translate("MainScreen", u"Budget", None))
        self.lblAmountTotal.setText(QCoreApplication.translate("MainScreen", u"???", None))
        self.lblSpentTotal.setText(QCoreApplication.translate("MainScreen", u"???", None))
        self.lblPeriodTotal.setText(QCoreApplication.translate("MainScreen", u"???", None))
        self.lbl_BudgetTotal.setText(QCoreApplication.translate("MainScreen", u"???", None))
        self.btnSpending.setText(QCoreApplication.translate("MainScreen", u"Spending", None))
        self.btnBudgetProgress.setText(QCoreApplication.translate("MainScreen", u"Budget Progress", None))
        self.btnLineGraphinDate.setText(QCoreApplication.translate("MainScreen", u"Line Graph inDate", None))
        self.lblTotalBalance.setText(QCoreApplication.translate("MainScreen", u"Total Balance", None))
        self.lblTotalBalanceCalc.setText(QCoreApplication.translate("MainScreen", u"          ???", None))
        self.btnAddTransaction.setText(QCoreApplication.translate("MainScreen", u"Add Transaction", None))
        self.btnAddBudget.setText(QCoreApplication.translate("MainScreen", u"Add Budget", None))
        self.btnExit.setText(QCoreApplication.translate("MainScreen", u"Logout", None))
        self.lblThisMonth.setText(QCoreApplication.translate("MainScreen", u"This Month", None))
        self.lblCurrentBalance.setText(QCoreApplication.translate("MainScreen", u"Current Balance", None))
        self.lblCurrentBalanceCalc.setText(QCoreApplication.translate("MainScreen", u"       ???", None))
        self.lblExpense.setText(QCoreApplication.translate("MainScreen", u"Expense", None))
        self.lblEarn.setText(QCoreApplication.translate("MainScreen", u"Saving", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainScreen", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainScreen", u"Edit", None))
        self.menuHel.setTitle(QCoreApplication.translate("MainScreen", u"Help", None))
    # retranslateUi

