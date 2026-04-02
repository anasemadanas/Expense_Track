from PySide6 import QtCharts, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QVBoxLayout

from Services.dashboard_service import DashBoardService
from ui.ui_frmdashboard import Ui_MainScreen

class MainScreen(QtWidgets.QMainWindow, Ui_MainScreen):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.service = DashBoardService()

        self.setWindowTitle("Dashboard")
        self.setWindowIcon(QIcon("resources\\icons\\logo.png"))


        self.btnSpending.clicked.connect(self.switch_to_pie)
        self.btnBudgetProgress.clicked.connect(self.switch_to_bar)
        self.btnLineGraphinDate.clicked.connect(self.switch_to_line)
        self.btnLogout.clicked.connect(self.close)
        self.btnAddBudget.clicked.connect(self.open_add_budget)
        self.btnAddTransaction.clicked.connect(self.open_add_transaction)

        self.actAbout.triggered.connect(self.service.show_about)
        self.actGuide.triggered.connect(self.service.open_guide)
        self.actExit.triggered.connect(self.close)
        self.actSave.triggered.connect(self.service.save_data)
        self.actExport.triggered.connect(self.service.export_data)
        
        self.load_dashboard()


    def switch_to_pie(self):  self.stackedWidgetChart.setCurrentIndex(0)
    def switch_to_line(self): self.stackedWidgetChart.setCurrentIndex(1)
    def switch_to_bar(self):  self.stackedWidgetChart.setCurrentIndex(2)
    
    
    def open_add_budget(self):
        from ui.frmAddBudget import AddBudget
        self.add_Bud = AddBudget()
        self.add_Bud.show()

    def open_add_transaction(self):
        from ui.frmAddTransaction import AddTransaction
        self.add_Tran = AddTransaction()
        self.add_Tran.show()



    def load_dashboard(self):
        self.update_balance_labels()
        self.init_pie_chart()
        self.init_bar_chart()
        self.init_line_graph()
        self.stackedWidgetChart.setCurrentIndex(0)
        
    def update_balance_labels(self):
        data = self.service.get_current_month_balance()

        self.lblTotalBalanceCalc.setText(f"${data['net']:,.2f}")

        self.lblCurrentBalanceCalc.setText(f"${data['net']:,.2f}")

        
        income = data["income"] or 1  
        expense_pct = min(int(data["expense"] / income * 100), 100)
        saving_pct  = min(int(max(0, data["net"]) / income * 100), 100)

        self.pbExpense.setValue(expense_pct)
        self.pbSave.setValue(saving_pct)


        
    def init_pie_chart(self):
        rows = self.service.get_spending_by_category()

        if not rows:
            rows = [{"category": "No data", "total": 1}]

        series = QtCharts.QPieSeries()
        series.setLabelsVisible(True)
        series.setPieSize(0.7)

        total = sum(r["total"] for r in rows)
        colors = ["#FF6384","#36A2EB","#FFCE56","#4BC0C0",
                  "#9966FF","#FF9F40","#C9CBCF","#7CFC00"]

        for i, row in enumerate(rows):
            pct   = round(row["total"] / total * 100) if total else 0
            label = f"{row['category']}  {pct}%"
            sl    = series.append(label, row["total"])
            sl.setColor(QColor(colors[i % len(colors)]))
            sl.setLabelVisible(True)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Spending by Category — This Month")
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        self._set_chart(self.gvPieChart, chart)
        

    def init_bar_chart(self):
        rows = self.service.get_budget_vs_actual()
        if not rows:
            rows = [{"category": "No data", "budget": 0, "actual": 0}]

        categories = [r["category"] for r in rows]
        set_budget = QtCharts.QBarSet("Budget")
        set_actual = QtCharts.QBarSet("Actual")
        set_budget.setColor(QColor("#36A2EB"))
        set_actual.setColor(QColor("#FF6384"))

        for r in rows:
            set_budget.append(r["budget"])
            set_actual.append(r["actual"])

        series = QtCharts.QBarSeries()
        series.append(set_budget)
        series.append(set_actual)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Budget vs Actual — This Month")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        max_val = max((max(r["budget"], r["actual"]) for r in rows), default=100)
        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, max_val * 1.2)
        axis_y.setTitleText("Amount ($)")
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        chart.legend().setAlignment(Qt.AlignBottom)
        self._set_chart(self.gvBarChart, chart)



    def init_line_graph(self):
        rows = self.service.get_monthly_spending_saving()

        series_exp  = QtCharts.QLineSeries()
        series_save = QtCharts.QLineSeries()
        series_exp.setName("Expense")
        series_save.setName("Saving")
        series_exp.setColor(QColor("#FF6384"))
        series_save.setColor(QColor("#4BC0C0"))

        pen_exp = series_exp.pen();   pen_exp.setWidth(2);  series_exp.setPen(pen_exp)
        pen_sav = series_save.pen();  pen_sav.setWidth(2);  series_save.setPen(pen_sav)

        months      = []
        max_val     = 0
        for i, row in enumerate(rows):
            series_exp.append(i, row["expense"])
            series_save.append(i, row["saving"])
            months.append(row["month"])
            max_val = max(max_val, row["expense"], row["saving"])

        chart = QtCharts.QChart()
        chart.addSeries(series_exp)
        chart.addSeries(series_save)
        chart.setTitle("Monthly Expense vs Saving — This Year")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(months)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series_exp.attachAxis(axis_x)
        series_save.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, (max_val or 100) * 1.2)
        axis_y.setTitleText("Amount ($)")
        chart.addAxis(axis_y, Qt.AlignLeft)
        series_exp.attachAxis(axis_y)
        series_save.attachAxis(axis_y)

        chart.legend().setAlignment(Qt.AlignBottom)
        self._set_chart(self.gvLineGraph, chart)
        

    def _set_chart(self, graphics_view, chart: QtCharts.QChart):

        chart_view = QtCharts.QChartView(chart)
        chart_view.setRenderHint(QtGui.QPainter.Antialiasing)


        old_layout = graphics_view.layout()
        if old_layout:
            while old_layout.count():
                item = old_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
        else:
            layout = QVBoxLayout(graphics_view)
            layout.setContentsMargins(0, 0, 0, 0)
            graphics_view.setLayout(layout)

        graphics_view.layout().addWidget(chart_view)
