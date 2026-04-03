from PySide6 import QtCore, QtGui, QtWidgets, QtCharts
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QIcon
from PySide6.QtWidgets import QVBoxLayout
from datetime import datetime
import random


all_transactions = [
    {"id": 1, "type": "expense", "category": "Food",      "amount": 200, "date": "2026-01-05"},
    {"id": 2, "type": "expense", "category": "Transport", "amount": 150, "date": "2026-02-10"},
    {"id": 3, "type": "expense", "category": "Shopping",  "amount": 300, "date": "2026-03-15"},
    {"id": 4, "type": "expense", "category": "Bills",     "amount": 100, "date": "2026-03-20"},
]


class DashBoardService:
    def show_about(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("About This App")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText("Expense Manager v1.0\n\nA simple tool for managing expenses and tracking your budget.\nDeveloper: Team Student\n\nClick below to visit my GitHub page:")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        btn_link = msg.addButton("Open GitHub", QtWidgets.QMessageBox.ButtonRole.ActionRole)
        msg.exec()
        if msg.clickedButton() == btn_link:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/anasemadanas/Expense_Track"))

    def save_data(self):
        print("Saving… :")

    def open_guide(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Guide")
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText("Click below to visit my GitHub page:")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        btn_link = msg.addButton("Open Guide", QtWidgets.QMessageBox.ButtonRole.ActionRole)
        msg.exec()
        if msg.clickedButton() == btn_link:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://github.com/anasemadanas/Expense_Track/blob/main/docs/project_document.md"))




    def export_data(self):
        file, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Export Data", "Summary_Budget.csv", "CSV Files (*.csv);;All Files (*)")
        if file:
            print("Export to:", file)

    def get_current_month_balance(self):
        income = 1200
        expense = 750
        net = income - expense
        return {"income": income, "expense": expense, "net": net}

    def get_available_months(self, transactions: list):
        months = set()
        for t in transactions:
            dt = datetime.strptime(t['date'], "%Y-%m-%d")
            months.add(dt.month)
        return sorted(list(months))

# --------------------- Main Screen ---------------------
from ui.ui_frmdashboard import Ui_MainScreen  

class MainScreen(QtWidgets.QMainWindow, Ui_MainScreen):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.service = DashBoardService()
        self.setWindowTitle("Dashboard")
        self.setWindowIcon(QIcon("resources\\icons\\logo.png"))

        # Buttons
        self.btnSpending.clicked.connect(lambda: self.stackedWidgetChart.setCurrentIndex(0))
        self.btnBudgetProgress.clicked.connect(lambda: self.stackedWidgetChart.setCurrentIndex(1))
        self.btnLineGraphinDate.clicked.connect(lambda: self.stackedWidgetChart.setCurrentIndex(2))
        self.btnLogout.clicked.connect(self.close)
        self.btnAddBudget.clicked.connect(self.open_add_budget)
        self.btnAddTransaction.clicked.connect(self.open_add_transaction)

        # Menu Actions
        self.actAbout.triggered.connect(self.service.show_about)
        self.actGuide.triggered.connect(self.service.open_guide)
        self.actExit.triggered.connect(self.close)
        self.actSave.triggered.connect(self.service.save_data)
        self.actExport.triggered.connect(self.service.export_data)

        # ComboBox for Months
        self.cmbMonths.currentIndexChanged.connect(self.on_month_changed)
        self.load_months()

        self.load_dashboard()


    def load_months(self):
        self.cmbMonths.clear()
        months = self.service.get_available_months(all_transactions)
        for m in months:
            self.cmbMonths.addItem(datetime(2026, m, 1).strftime("%B"))
        if months:
            self.cmbMonths.setCurrentIndex(0)

    def on_month_changed(self):
        idx = self.cmbMonths.currentIndex()
        if idx < 0: return
        selected_month = idx + 1
        month_transactions = [t for t in all_transactions if datetime.strptime(t['date'], "%Y-%m-%d").month == selected_month]
        self.draw_pie_chart(month_transactions)
        self.draw_bar_chart(month_transactions)
        self.draw_line_chart(month_transactions)

    # ---- Add Forms ----
    def open_add_budget(self):
        from ui.frmAddBudget import AddBudget
        self.add_Bud = AddBudget()
        self.add_Bud.show()

    def open_add_transaction(self):
        from ui.frmAddTransaction import AddTransaction
        self.add_Tran = AddTransaction()
        self.add_Tran.show()

    # ---- Dashboard ----
    def load_dashboard(self):
        self.update_balance_labels()
        self.draw_pie_chart(all_transactions)
        self.draw_bar_chart(all_transactions)
        self.draw_line_chart(all_transactions)
        self.stackedWidgetChart.setCurrentIndex(0)

    # ---- Balance ----
    def update_balance_labels(self):
        data = self.service.get_current_month_balance()
        self.lblTotalBalanceCalc.setText(f"${data['net']:,.2f}")
        self.lblCurrentBalanceCalc.setText(f"${data['net']:,.2f}")
        income = data["income"] or 1
        self.pbExpense.setValue(min(int(data["expense"] / income * 100), 100))
        self.pbSave.setValue(min(int(max(0, data["net"]) / income * 100), 100))

    # ---- Pie Chart ----
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

    # ---- Bar Chart ----
    def draw_bar_chart(self, transactions):
        categories = list(set(t["category"] for t in transactions)) or ["No data"]
        set_budget = QtCharts.QBarSet("Budget")
        set_actual = QtCharts.QBarSet("Actual")
        set_budget.setColor(QColor("#36A2EB"))
        set_actual.setColor(QColor("#FF6384"))

        for cat in categories:
            budget = 400  # قيمة تجريبية
            actual = sum(t["amount"] for t in transactions if t["category"] == cat)
            set_budget.append(budget)
            set_actual.append(actual)

        series = QtCharts.QBarSeries()
        series.append(set_budget)
        series.append(set_actual)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Budget vs Actual")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        # --- تصحيح حساب max_val ---
        budget_values = [set_budget.at(i) for i in range(set_budget.count())]
        actual_values = [set_actual.at(i) for i in range(set_actual.count())]
        max_val = max(budget_values + actual_values, default=100)

        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, max_val * 1.2)
        axis_y.setTitleText("Amount ($)")
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)
        chart.legend().setAlignment(Qt.AlignBottom)
        self._set_chart(self.gvBarChart, chart)

    # ---- Line Chart ----
    def draw_line_chart(self, transactions):
        months_labels = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
        expense_by_month = {i:0 for i in range(1,13)}
        for t in transactions:
            expense_by_month[datetime.strptime(t["date"], "%Y-%m-%d").month] += t["amount"]

        series_exp = QtCharts.QLineSeries()
        series_save = QtCharts.QLineSeries()
        series_exp.setName("Expense")
        series_save.setName("Saving")
        series_exp.setColor(QColor("#FF6384"))
        series_save.setColor(QColor("#4BC0C0"))

        for i in range(1,13):
            series_exp.append(i-1, expense_by_month[i])
            series_save.append(i-1, random.randint(50, 300))  # مثال للادخار

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

        max_val = max(expense_by_month.values()) + 50
        axis_y = QtCharts.QValueAxis()
        axis_y.setRange(0, max_val)
        axis_y.setTitleText("Amount ($)")
        chart.addAxis(axis_y, Qt.AlignLeft)
        series_exp.attachAxis(axis_y)
        series_save.attachAxis(axis_y)
        chart.legend().setAlignment(Qt.AlignBottom)
        self._set_chart(self.gvLineGraph, chart)

    # ---- Helper ----
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