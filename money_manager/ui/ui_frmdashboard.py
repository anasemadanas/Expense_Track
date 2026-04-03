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
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainScreen(object):
    def setupUi(self, MainScreen):
        if not MainScreen.objectName():
            MainScreen.setObjectName(u"MainScreen")
        MainScreen.setEnabled(True)
        MainScreen.resize(917, 829)
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
        self.lblTitleDashBoard.setGeometry(QRect(260, 10, 371, 91))
        font = QFont()
        font.setFamilies([u"MV Boli"])
        font.setPointSize(58)
        font.setBold(False)
        font.setItalic(False)
        self.lblTitleDashBoard.setFont(font)
        self.lblTitleDashBoard.setStyleSheet(u"\n"
"font: 58pt \"MV Boli\";")
        self.stackedWidgetChart = QStackedWidget(self.centralwidget)
        self.stackedWidgetChart.setObjectName(u"stackedWidgetChart")
        self.stackedWidgetChart.setGeometry(QRect(50, 510, 831, 251))
        self.pageSpending_1 = QWidget()
        self.pageSpending_1.setObjectName(u"pageSpending_1")
        self.gvPieChart = QGraphicsView(self.pageSpending_1)
        self.gvPieChart.setObjectName(u"gvPieChart")
        self.gvPieChart.setGeometry(QRect(-10, 30, 811, 221))
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
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 460, 831, 44))
        self.hlCharts = QHBoxLayout(self.layoutWidget)
        self.hlCharts.setObjectName(u"hlCharts")
        self.hlCharts.setContentsMargins(0, 0, 0, 0)
        self.btnSpending = QPushButton(self.layoutWidget)
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

        self.hlCharts.addWidget(self.btnSpending)

        self.btnBudgetProgress = QPushButton(self.layoutWidget)
        self.btnBudgetProgress.setObjectName(u"btnBudgetProgress")
        icon1 = QIcon()
        icon1.addFile(u":/icons/barchart_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBudgetProgress.setIcon(icon1)
        self.btnBudgetProgress.setCheckable(True)
        self.btnBudgetProgress.setChecked(False)
        self.btnBudgetProgress.setAutoRepeat(False)
        self.btnBudgetProgress.setAutoExclusive(True)

        self.hlCharts.addWidget(self.btnBudgetProgress)

        self.btnLineGraphinDate = QPushButton(self.layoutWidget)
        self.btnLineGraphinDate.setObjectName(u"btnLineGraphinDate")
        self.btnLineGraphinDate.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/linegraph_black.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnLineGraphinDate.setIcon(icon2)
        self.btnLineGraphinDate.setCheckable(True)
        self.btnLineGraphinDate.setChecked(False)
        self.btnLineGraphinDate.setAutoRepeat(False)
        self.btnLineGraphinDate.setAutoExclusive(True)

        self.hlCharts.addWidget(self.btnLineGraphinDate)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(630, 130, 251, 301))
        self.vlbtnAdd = QVBoxLayout(self.layoutWidget1)
        self.vlbtnAdd.setObjectName(u"vlbtnAdd")
        self.vlbtnAdd.setContentsMargins(0, 0, 0, 0)
        self.btnAddTransaction = QPushButton(self.layoutWidget1)
        self.btnAddTransaction.setObjectName(u"btnAddTransaction")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(False)
        self.btnAddTransaction.setFont(font1)
        self.btnAddTransaction.setStyleSheet(u"font: 20pt \"Segoe UI\";\n"
"color:rgb(0, 255, 0);")

        self.vlbtnAdd.addWidget(self.btnAddTransaction)

        self.btnAddBudget = QPushButton(self.layoutWidget1)
        self.btnAddBudget.setObjectName(u"btnAddBudget")
        self.btnAddBudget.setFont(font1)
        self.btnAddBudget.setStyleSheet(u"color:rgb(0, 255, 0);\n"
"font: 20pt \"Segoe UI\";")

        self.vlbtnAdd.addWidget(self.btnAddBudget)

        self.btnLogout = QPushButton(self.layoutWidget1)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setFont(font1)
        self.btnLogout.setStyleSheet(u"color:rgb(0, 255, 0);\n"
"font: 20pt \"Segoe UI\";")

        self.vlbtnAdd.addWidget(self.btnLogout)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(50, 130, 361, 304))
        self.gridLayoutThisMonth = QGridLayout(self.layoutWidget2)
        self.gridLayoutThisMonth.setObjectName(u"gridLayoutThisMonth")
        self.gridLayoutThisMonth.setContentsMargins(0, 0, 0, 0)
        self.pbSave = QProgressBar(self.layoutWidget2)
        self.pbSave.setObjectName(u"pbSave")
        font2 = QFont()
        font2.setPointSize(14)
        self.pbSave.setFont(font2)
        self.pbSave.setValue(24)

        self.gridLayoutThisMonth.addWidget(self.pbSave, 4, 1, 1, 4)

        self.pbExpense = QProgressBar(self.layoutWidget2)
        self.pbExpense.setObjectName(u"pbExpense")
        self.pbExpense.setFont(font2)
        self.pbExpense.setValue(24)

        self.gridLayoutThisMonth.addWidget(self.pbExpense, 3, 1, 1, 4)

        self.lblTotalBalanceCalc = QLabel(self.layoutWidget2)
        self.lblTotalBalanceCalc.setObjectName(u"lblTotalBalanceCalc")
        self.lblTotalBalanceCalc.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"Modir MT"])
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setItalic(False)
        self.lblTotalBalanceCalc.setFont(font3)
        self.lblTotalBalanceCalc.setStyleSheet(u"\n"
"font: 20pt \"Modir MT\";")

        self.gridLayoutThisMonth.addWidget(self.lblTotalBalanceCalc, 1, 3, 1, 2)

        self.lblSave = QLabel(self.layoutWidget2)
        self.lblSave.setObjectName(u"lblSave")
        self.lblSave.setFont(font2)

        self.gridLayoutThisMonth.addWidget(self.lblSave, 4, 0, 1, 1)

        self.lblCurrentBalanceCalc = QLabel(self.layoutWidget2)
        self.lblCurrentBalanceCalc.setObjectName(u"lblCurrentBalanceCalc")
        self.lblCurrentBalanceCalc.setEnabled(True)
        self.lblCurrentBalanceCalc.setFont(font3)
        self.lblCurrentBalanceCalc.setStyleSheet(u"\n"
"font: 20pt \"Modir MT\";")

        self.gridLayoutThisMonth.addWidget(self.lblCurrentBalanceCalc, 2, 3, 1, 2)

        self.lblTotalBalance = QLabel(self.layoutWidget2)
        self.lblTotalBalance.setObjectName(u"lblTotalBalance")
        self.lblTotalBalance.setEnabled(True)
        font4 = QFont()
        font4.setFamilies([u"Mudir MT"])
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        self.lblTotalBalance.setFont(font4)
        self.lblTotalBalance.setStyleSheet(u"color:rgb(255, 84, 87);\n"
"font: 20pt ;")

        self.gridLayoutThisMonth.addWidget(self.lblTotalBalance, 1, 0, 1, 3)

        self.lblCurrentBalance = QLabel(self.layoutWidget2)
        self.lblCurrentBalance.setObjectName(u"lblCurrentBalance")
        self.lblCurrentBalance.setEnabled(True)
        self.lblCurrentBalance.setFont(font4)
        self.lblCurrentBalance.setStyleSheet(u"color:rgb(255, 84, 87);\n"
"font: 20pt ;")

        self.gridLayoutThisMonth.addWidget(self.lblCurrentBalance, 2, 0, 1, 3)

        self.lblExpense = QLabel(self.layoutWidget2)
        self.lblExpense.setObjectName(u"lblExpense")
        self.lblExpense.setFont(font2)

        self.gridLayoutThisMonth.addWidget(self.lblExpense, 3, 0, 1, 1)

        self.lblThisMonth = QLabel(self.layoutWidget2)
        self.lblThisMonth.setObjectName(u"lblThisMonth")
        self.lblThisMonth.setEnabled(True)
        font5 = QFont()
        font5.setFamilies([u"MV Boli"])
        font5.setPointSize(36)
        font5.setBold(False)
        font5.setItalic(False)
        self.lblThisMonth.setFont(font5)
        self.lblThisMonth.setStyleSheet(u"color:rgb(255, 84, 87);\n"
"font: 36pt \"MV Boli\";")

        self.gridLayoutThisMonth.addWidget(self.lblThisMonth, 0, 0, 1, 4)

        self.cmbMonths = QComboBox(self.layoutWidget2)
        self.cmbMonths.setObjectName(u"cmbMonths")

        self.gridLayoutThisMonth.addWidget(self.cmbMonths, 0, 4, 1, 1)

        MainScreen.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainScreen)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 917, 33))
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
        QWidget.setTabOrder(self.btnAddTransaction, self.btnLogout)
        QWidget.setTabOrder(self.btnLogout, self.btnSpending)
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

        self.stackedWidgetChart.setCurrentIndex(2)


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
        self.btnSpending.setText(QCoreApplication.translate("MainScreen", u"Spending", None))
        self.btnBudgetProgress.setText(QCoreApplication.translate("MainScreen", u"Budget Progress", None))
        self.btnLineGraphinDate.setText(QCoreApplication.translate("MainScreen", u"Line Graph inDate", None))
        self.btnAddTransaction.setText(QCoreApplication.translate("MainScreen", u"Add Transaction", None))
        self.btnAddBudget.setText(QCoreApplication.translate("MainScreen", u"Add Budget", None))
        self.btnLogout.setText(QCoreApplication.translate("MainScreen", u"Logout", None))
        self.lblTotalBalanceCalc.setText(QCoreApplication.translate("MainScreen", u"???", None))
        self.lblSave.setText(QCoreApplication.translate("MainScreen", u"Saving", None))
        self.lblCurrentBalanceCalc.setText(QCoreApplication.translate("MainScreen", u"???", None))
        self.lblTotalBalance.setText(QCoreApplication.translate("MainScreen", u"Total Balance", None))
        self.lblCurrentBalance.setText(QCoreApplication.translate("MainScreen", u"Current Balance", None))
        self.lblExpense.setText(QCoreApplication.translate("MainScreen", u"Expense", None))
        self.lblThisMonth.setText(QCoreApplication.translate("MainScreen", u"This Month", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainScreen", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainScreen", u"Edit", None))
        self.menuHel.setTitle(QCoreApplication.translate("MainScreen", u"Help", None))
    # retranslateUi

