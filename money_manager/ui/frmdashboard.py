

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
        self.stackedWidgetChart.setCurrentIndex(0)

    def Switch_to_BarChart(self):
        self.stackedWidgetChart.setCurrentIndex(1)

    def Switch_to_LineGraph(self):
        self.stackedWidgetChart.setCurrentIndex(2)
        

        
    def update_piechart (self):
        self.gvPieChart = QtCharts.QChart()

        self.gvPieChart = QtCharts.QPieSeries()
        self.gvPieChart.setLabelsVisible(True)
        self.gvPieChart.setLabelsPosition(QtCharts.QPieSeries.LabelOutside)
        
        self.slice_food = QtCharts.QPieSlice("Food", 30)
        self.slice_transport = QtCharts.QPieSlice("Transport", 20)
        self.slice_entertainment = QtCharts.QPieSlice("Entertainment", 10)
        self.slice_other = QtCharts.QPieSlice("Other", 40)

        self.gvPieChart.append(self.slice_food)
        self.gvPieChart.append(self.slice_transport)
        self.gvPieChart.append(self.slice_entertainment)
        self.gvPieChart.append(self.slice_other)
        
        self.gvPieChart.addSeries(self.gvPieChart)
        self.gvPieChart.setTitle("Spending by Category")
        self.gvPieChart.legend().setAlignment(Qt.AlignBottom)
        self.gvPieChart.legend().setVisible(True)

        self.stackedWidgetChart.setChart(self.gvPieChart)
        
    def open_AddBudget(self):
            from ui.frmAddBudget import AddBudget
            self.Add = AddBudget()
            self.Add.show()
     
            
    def open_AddTransaction(self):
            from ui.frmAddTransaction import AddTransaction
            self.Add = AddTransaction()
            self.Add.show()
   