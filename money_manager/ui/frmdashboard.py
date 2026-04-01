

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6 import QtCharts
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import Qt, QIcon

from Services.dashboard_service import DashBoardService
from ui.ui_frmdashboard import Ui_MainScreen

class MainScreen(QtWidgets.QMainWindow, Ui_MainScreen):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.service = DashBoardService()
        self.btnExit.clicked.connect(self.close)
        self.setWindowTitle("Dashboard")
        self.setWindowIcon(QIcon("resources\\icons\\logo.png"))

        self.btnSpending.clicked.connect(self.Switch_to_PieChart)
        self.btnBudgetProgress.clicked.connect(self.Switch_to_BarChart)
        self.btnLineGraphinDate.clicked.connect(self.Switch_to_LineGraph)
        

        self.actAbout.triggered.connect(self.service.show_about)
        self.actGuide.triggered.connect(self.service.open_guide)
        self.actExit.triggered.connect(self.close)       
        self.actSave.triggered.connect(self.service.save_data)  
        self.actExport.triggered.connect(self.service.export_data)
        self.btnAddBudget.clicked.connect(self.open_AddBudget)
        self.btnAddTransaction.clicked.connect(self.open_AddTransaction)
         
         
    def Switch_to_PieChart(self):
        self.stackedWidgetChart.setCurrentWidget(self.pageSpending_1)

    def Switch_to_BarChart(self):
        self.stackedWidgetChart.setCurrentWidget(self.pageBudget_2)

    def Switch_to_LineGraph(self):
        self.stackedWidgetChart.setCurrentWidget(self.pageLineGraph_3)
        

        
    def update_piechart (self):
        self.gvPieChart = QtCharts.QChart
        
    
    def open_AddBudget(self):
            from ui.frmAddBudget import AddBudget
            self.Add = AddBudget()
            self.Add.show()
     
            
    def open_AddTransaction(self):
            from ui.frmAddTransaction import AddTransaction
            self.Add = AddTransaction()
            self.Add.show()
   