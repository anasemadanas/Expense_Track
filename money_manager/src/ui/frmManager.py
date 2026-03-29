import os
import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

CURRENT = os.path.abspath(__file__)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(CURRENT)))
DB_PATH = os.path.join(PROJECT_ROOT, "Database", "money_manager_DB.db")
DB_PATH = os.path.normpath(DB_PATH)


class Ui_MainScreen(object):

    def setupUi(self, MainScreen):
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(717, 523)
        MainScreen.setWindowTitle("Expense Track - Manager")

        self.centralwidget = QtWidgets.QWidget(MainScreen)
        self.centralwidget.setObjectName("centralwidget")
        

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)

        self.lblExpenseTrack = QtWidgets.QLabel(self.centralwidget)
        self.lblExpenseTrack.setGeometry(QtCore.QRect(200, 20, 411, 71))
        font_title = QtGui.QFont()
        font_title.setFamily("MV Boli")
        font_title.setPointSize(36)
        self.lblExpenseTrack.setFont(font_title)
        self.lblExpenseTrack.setStyleSheet("color: rgb(85, 0, 255);")
        self.lblExpenseTrack.setObjectName("lblExpenseTrack")

        self.btnAddBudget = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddBudget.setGeometry(QtCore.QRect(170, 100, 171, 61))
        self.btnAddBudget.setFont(font)
        self.btnAddBudget.setObjectName("btnAddBudget")

        self.btnAddTransaction = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddTransaction.setGeometry(QtCore.QRect(390, 100, 171, 61))
        self.btnAddTransaction.setFont(font)
        self.btnAddTransaction.setObjectName("btnAddTransaction")

        self.lstTransaction = QtWidgets.QTreeView(self.centralwidget)
        self.lstTransaction.setGeometry(QtCore.QRect(40, 180, 641, 192))
        font_tree = QtGui.QFont()
        font_tree.setFamily("Calibri")
        font_tree.setPointSize(12)
        self.lstTransaction.setFont(font_tree)
        self.lstTransaction.setObjectName("lstTransaction")

        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(510, 390, 171, 61))
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")

        MainScreen.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 717, 33))
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        MainScreen.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainScreen)
        MainScreen.setStatusBar(self.statusbar)

        self.actSave   = QtWidgets.QAction(MainScreen)
        self.actExit   = QtWidgets.QAction(MainScreen)
        self.actExport = QtWidgets.QAction(MainScreen)
        self.actAbout  = QtWidgets.QAction(MainScreen)
        self.actGuide  = QtWidgets.QAction(MainScreen)

        self.menuFile.addAction(self.actSave)
        self.menuFile.addAction(self.actExit)
        self.menuEdit.addAction(self.actExport)
        self.menuHelp.addAction(self.actAbout)
        self.menuHelp.addAction(self.actGuide)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.btnAddTransaction.clicked.connect(self.open_transaction)
        self.btnAddBudget.clicked.connect(self.open_budget)
        self.btnExit.clicked.connect(MainScreen.close)
        self.actExit.triggered.connect(MainScreen.close)

        self.MainScreen = MainScreen
        self.retranslateUi(MainScreen)
        QtCore.QMetaObject.connectSlotsByName(MainScreen)

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "Expense Track"))
        self.lblExpenseTrack.setText(_translate("MainScreen", "Expense Track"))
        self.btnAddBudget.setText(_translate("MainScreen", "Add Budget"))
        self.btnAddTransaction.setText(_translate("MainScreen", "Add Transaction"))
        self.btnExit.setText(_translate("MainScreen", "Exit"))
        self.menuFile.setTitle(_translate("MainScreen", "File"))
        self.menuEdit.setTitle(_translate("MainScreen", "Edit"))
        self.menuHelp.setTitle(_translate("MainScreen", "Help"))
        self.actSave.setText(_translate("MainScreen", "Save"))
        self.actExit.setText(_translate("MainScreen", "Exit"))
        self.actExport.setText(_translate("MainScreen", "Export"))
        self.actAbout.setText(_translate("MainScreen", "About"))
        self.actGuide.setText(_translate("MainScreen", "Guide"))

    def open_transaction(self):
        from ...presentation.views.frmTransaction import Ui_AddTransaction
        self.trans_window = QtWidgets.QWidget()
        self.trans_ui = Ui_AddTransaction()
        self.trans_ui.setupUi(self.trans_window)
        self.trans_window.show()

    def open_budget(self):
        from ...presentation.views.budget_view import Ui_AddBudget
        self.budget_window = QtWidgets.QWidget()
        self.budget_ui = Ui_AddBudget()
        self.budget_ui.setupUi(self.budget_window)
        self.budget_window.show()


def save_data(self):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    row_count = self.model.rowCount()

    for row in range(row_count):
        date     = self.model.item(row, 0).text()
        category = self.model.item(row, 1).text()
        amount   = self.model.item(row, 2).text()

        cur.execute("""
            INSERT INTO transactions (t_date, category, amount, note)
            VALUES (?, ?, ?, ?)
        """, (date, category, amount))

    conn.commit()
    conn.close()

    QtWidgets.QMessageBox.information(None, "Saved", "All data saved successfully.")
    
    
def load_transactions(self):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT id, t_date, category, amount FROM transactions")
    rows = cur.fetchall()

    self.model.removeRows(0, self.model.rowCount()) 

    for row in rows:
        items = [
            QtGui.QStandardItem(str(row[0])),
            QtGui.QStandardItem(row[1]),
            QtGui.QStandardItem(row[2]),
            QtGui.QStandardItem(str(row[3]))
        ]
        self.model.appendRow(items)

    conn.close()
    
    
def export_csv(self):
    path, _ = QtWidgets.QFileDialog.getSaveFileName(
        None, 
        "Export CSV", 
        "", 
        "CSV Files (*.csv)"
    )

    if not path:
        return

    row_count = self.model.rowCount()
    col_count = self.model.columnCount()

    with open(path, "w", encoding="utf-8") as file:

        headers = []
        for col in range(col_count):
            headers.append(self.model.headerData(col, QtCore.Qt.Horizontal))
        file.write(",".join(headers) + "\n")


        for row in range(row_count):
            row_data = []
            for col in range(col_count):
                item = self.model.item(row, col)
                row_data.append(item.text() if item else "")
            file.write(",".join(row_data) + "\n")

    QtWidgets.QMessageBox.information(None, "Exported", "CSV exported successfully.")    