from PySide6 import QtCore, QtGui, QtWidgets, QtCharts
from PySide6.QtGui import QIcon, QColor
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QVBoxLayout
from datetime import datetime
import random
from PySide6.QtWidgets import QMessageBox
from Services.dashboard_service import DashBoardService
from ui.ui_frmDashBoard import Ui_MainScreen

from Services.models.permissions import has_permission, UserPermissions


class MainScreen(QtWidgets.QMainWindow, Ui_MainScreen):
    def __init__(self, current_user=None, transactions=None):
        super().__init__()
        self.setupUi(self)
        self.transactions = transactions or []
        self.service = DashBoardService()
        self.setWindowTitle("Dashboard")
        self.setWindowIcon(QIcon("resources\\icons\\logo.png"))
        
        self.current_user = current_user
        self.permissions = current_user["permissions"] if current_user else 0
        
    # ------------------ Connect buttons and actions ------------------------------------------
        self.btnSpending.clicked.connect(lambda: self.stackedWidgetChart.setCurrentIndex(0))
        self.btnLineGraphinDate.clicked.connect(lambda: self.stackedWidgetChart.setCurrentIndex(1))
        self.btnBudgetProgress.clicked.connect(lambda: self.stackedWidgetChart.setCurrentIndex(2))

        self.btnAddBudget.clicked.connect(self.open_add_budget)
        self.btnAddTransaction.clicked.connect(self.open_add_transaction)
        self.btnListTransaction.clicked.connect(self.open_list_transaction)
        self.btnLogout.clicked.connect(self.close)

        self.actAbout.triggered.connect(self.service.show_about)
        self.actGuide.triggered.connect(self.service.open_guide)
        self.actSave.triggered.connect(self.service.save_data)
        self.actExport.triggered.connect(self.service.export_data)
        self.actExit.triggered.connect(self.close)
        
        self.cmbMonths.currentIndexChanged.connect(self.on_month_changed)
        self.cmbYears.currentIndexChanged.connect(self.on_month_changed)

        self.load_dashboard()
    # ---- ------------------------------------------------------------- ----
        
    def load_dashboard(self):
        self.transactions = self.service.get_all_transactions()
        self.update_balance_labels()
        self.draw_charts(self.transactions)
        
    def update_balance_labels(self):
        data = self.service.get_current_month_balance()
        self.lblTotalBalanceCalc.setText(f"${data['net']:,.2f}")
        self.lblCurrentBalanceCalc.setText(f"${data['net']:,.2f}")
        income = data["income"] or 1
        self.pbExpense.setValue(min(int(data["expense"] / income * 100), 100))
        self.pbSave.setValue(min(int(max(0, data["net"]) / income * 100), 100))

    # ----------------------------------------------------------------- ----    
    def on_month_changed(self):
        
        idx = self.cmbMonths.currentIndex()
        month_index = datetime.now().month - 1
        year_text = str(datetime.now().year)

        if self.cmbYears.count() == 0 or self.cmbYears.findText(year_text) == -1:
            self.cmbYears.addItem(year_text)
            self.cmbYears.setCurrentIndex(0)
        else:
            self.cmbYears.setCurrentIndex(self.cmbYears.findText(year_text))

        if self.cmbMonths.count() == 0:
            for m in range(1, 13):
                self.cmbMonths.addItem(datetime(2026, m, 1).strftime("%B"))

        self.cmbMonths.setCurrentIndex(month_index)

    # ---- Add Forms ----------------------------------------------------------
    def message_error_permissions(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Permission Denied")
        msg.setText(text)
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.exec()
        
    def open_add_budget(self):
        if not has_permission(self.permissions, UserPermissions.ADD_BUDGET):
            self.message_error_permissions("You do not have permission to add budgets.")
            return
        from ui.frmAddBudget import AddBudget
        open = AddBudget()
        open.exec()
        self.load_dashboard()

    def open_add_transaction(self):
        if not has_permission(self.permissions, UserPermissions.ADD_TRANSACTION):
            self.message_error_permissions("You do not have permission to add transactions.")
            return
        from ui.frmAddTransaction import AddTransaction
        open = AddTransaction()
        open.exec()
        self.load_dashboard()

    def open_list_transaction(self):
        if not has_permission(self.permissions, UserPermissions.LIST_TRANSACTION):
            self.message_error_permissions("You do not have permission to view transactions.")
            return
        from ui.frmListTransaction import ListTransaction
        open = ListTransaction()
        open.exec()
        self.load_dashboard()

    # ---- Draw Charts ----------------------------------------------------------
    def draw_charts(self, transactions):
        self.draw_pie_chart(transactions)
        self.draw_bar_chart(transactions)
        self.draw_line_chart(transactions)
        self.stackedWidgetChart.setCurrentIndex(0)
        
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
            layout.setContentsMargins(0,0,0,0)
            graphics_view.setLayout(layout)
        graphics_view.layout().addWidget(chart_view)

    def draw_pie_chart(self, transactions):
        cat_totals = {}
        for t in transactions:
            cat_totals[t["category"]] = cat_totals.get(t["category"], 0) + t["amount"]
        if not cat_totals: cat_totals = {"No data": 1}

        series = QtCharts.QPieSeries()
        series.setLabelsVisible(True)
        series.setPieSize(0.7)
        colors = ["#FF6384","#36A2EB","#FFCE56","#4BC0C0","#9966FF","#FF9F40","#C9CBCF","#7CFC00"]
        total = sum(cat_totals.values())
        for i, (cat, val) in enumerate(cat_totals.items()):
            pct = round(val / total * 100) if total else 0
            sl = series.append(f"{cat} {pct}%", val)
            sl.setColor(QColor(colors[i % len(colors)]))


        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Spending by Category")
        chart.legend().setAlignment(Qt.AlignBottom)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        self._set_chart(self.gvPieChart, chart)

    def draw_bar_chart(self, transactions):
        if not transactions:
            transactions = [{"category": "No data", "amount": 0}]

        categories = list(set(t["category"] for t in transactions))

        set_budget = QtCharts.QBarSet("Budget")
        set_actual = QtCharts.QBarSet("Actual")

        totals = {}
        for t in transactions:
            cat = t["category"]
            amt = t["amount"] or 0
            totals[cat] = totals.get(cat, 0) + amt

  
        for cat in categories:
            value = float(totals.get(cat, 0))
            set_actual.append(value)
            set_budget.append(0) 

        series = QtCharts.QBarSeries()
        series.append(set_budget)
        series.append(set_actual)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Budget vs Actual")

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, max([sum(totals.values()), 100]))
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        self._set_chart(self.gvBarChart, chart)

    def draw_line_chart(self, transactions):
        months_labels = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        expense_by_month = {i:0 for i in range(1,13)}

        for t in transactions:
            expense_by_month[t["month"]] += t["amount"]

        series_exp = QtCharts.QLineSeries()
        series_save = QtCharts.QLineSeries()
        series_exp.setName("Expense")
        series_save.setName("Saving")
        series_exp.setColor(QColor("#FF6384"))
        series_save.setColor(QColor("#4BC0C0"))

        for i in range(1,13):
            series_exp.append(i-1, expense_by_month[i])
            series_save.append(i-1, random.randint(50, 300))

        chart = QtCharts.QChart()
        chart.addSeries(series_exp)
        chart.addSeries(series_save)
        chart.setTitle("Monthly Expense vs Saving")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(months_labels)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series_exp.attachAxis(axis_x)
        series_save.attachAxis(axis_x)

        axis_y = QtCharts.QValueAxis()
        max_val = max(expense_by_month.values()) + 50
        axis_y.setRange(0, max_val)
        axis_y.setTitleText("Amount ($)")
        chart.addAxis(axis_y, Qt.AlignLeft)
        series_exp.attachAxis(axis_y)
        series_save.attachAxis(axis_y)

        chart.legend().setAlignment(Qt.AlignBottom)
        self._set_chart(self.gvLineGraph, chart)
    # ---- ------------------------------------------------------------- ----   