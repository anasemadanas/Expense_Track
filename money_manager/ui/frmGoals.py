from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QProgressBar, QScrollArea, QWidget, QFrame, QInputDialog,
    QMessageBox, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
from Services.goal_service import GoalService


class GoalCard(QFrame):
    def __init__(self, goal, on_add_savings, on_delete):
        super().__init__()
        self.goal = goal
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setStyleSheet("QFrame { background-color: #1e1e2e; border-radius: 8px; padding: 4px; }")

        layout = QVBoxLayout(self)
        layout.setSpacing(6)

        # ---- Top row: name + delete button ----
        top = QHBoxLayout()
        name_label = QLabel(goal.name)
        name_font = QFont()
        name_font.setPointSize(12)
        name_font.setBold(True)
        name_label.setFont(name_font)
        name_label.setStyleSheet("color: white;")
        top.addWidget(name_label)
        top.addStretch()

        btn_delete = QPushButton("✕")
        btn_delete.setFixedSize(24, 24)
        btn_delete.setStyleSheet("color: #ff5457; background: transparent; border: none; font-size: 14px;")
        btn_delete.clicked.connect(lambda: on_delete(goal.id))
        top.addWidget(btn_delete)
        layout.addLayout(top)

        # ---- Amounts ----
        status_color = "#4BC0C0" if goal.is_complete else "white"
        status_text = "COMPLETE!" if goal.is_complete else f"${goal.saved_amount:,.2f} of ${goal.target_amount:,.2f}"
        amounts_label = QLabel(status_text)
        amounts_label.setStyleSheet(f"color: {status_color}; font-size: 11px;")
        layout.addWidget(amounts_label)

        # ---- Progress bar ----
        bar = QProgressBar()
        bar.setMinimum(0)
        bar.setMaximum(100)
        bar.setValue(goal.progress_percent)
        bar.setTextVisible(True)
        bar.setFixedHeight(20)
        if goal.is_complete:
            bar.setStyleSheet("QProgressBar::chunk { background-color: #4BC0C0; }")
        else:
            bar.setStyleSheet("QProgressBar::chunk { background-color: #36A2EB; }")
        layout.addWidget(bar)

        # ---- Add savings button ----
        if not goal.is_complete:
            btn_save = QPushButton("+ Add Savings")
            btn_save.setStyleSheet(
                "QPushButton { background-color: #36A2EB; color: white; border-radius: 4px; padding: 4px 10px; }"
                "QPushButton:hover { background-color: #5BB8FF; }"
            )
            btn_save.clicked.connect(lambda: on_add_savings(goal.id, goal.name, goal.target_amount - goal.saved_amount))
            layout.addWidget(btn_save, alignment=Qt.AlignRight)


class GoalsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.service = GoalService()
        self.setWindowTitle("Savings Goals")
        self.setWindowIcon(QIcon("resources\\icons\\logo.png"))
        self.setMinimumSize(480, 500)
        self.resize(520, 580)

        root = QVBoxLayout(self)
        root.setSpacing(10)

        # ---- Header ----
        title = QLabel("My Savings Goals")
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        root.addWidget(title)

        # ---- Add goal button ----
        btn_add = QPushButton("+ New Goal")
        btn_add.setFixedHeight(36)
        btn_add.setStyleSheet(
            "QPushButton { background-color: rgb(0,200,0); color: black; font-size: 13px; "
            "border-radius: 6px; font-weight: bold; }"
            "QPushButton:hover { background-color: rgb(0,230,0); }"
        )
        btn_add.clicked.connect(self.add_goal)
        root.addWidget(btn_add)

        # ---- Scrollable goal list ----
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        self.goals_container = QWidget()
        self.goals_layout = QVBoxLayout(self.goals_container)
        self.goals_layout.setSpacing(10)
        self.goals_layout.addStretch()

        self.scroll_area.setWidget(self.goals_container)
        root.addWidget(self.scroll_area)

        # ---- Close button ----
        btn_close = QPushButton("Close")
        btn_close.setFixedHeight(34)
        btn_close.clicked.connect(self.close)
        root.addWidget(btn_close)

        self.load_goals()

    def load_goals(self):
        # Clear existing cards (everything except the trailing stretch)
        while self.goals_layout.count() > 1:
            item = self.goals_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        goals = self.service.get_all_goals()

        if not goals:
            empty = QLabel("No goals yet. Add one to get started!")
            empty.setAlignment(Qt.AlignCenter)
            empty.setStyleSheet("color: grey; font-size: 12px;")
            self.goals_layout.insertWidget(0, empty)
            return

        for i, goal in enumerate(goals):
            card = GoalCard(goal, self.on_add_savings, self.on_delete)
            self.goals_layout.insertWidget(i, card)

    def add_goal(self):
        name, ok = QInputDialog.getText(self, "New Goal", "What are you saving for?")
        if not ok or not name.strip():
            return

        amount, ok = QInputDialog.getDouble(
            self, "Target Amount", f"How much do you want to save for '{name.strip()}'?",
            min=0.01, max=1_000_000, decimals=2
        )
        if not ok:
            return

        try:
            self.service.add_goal(name, amount)
            self.load_goals()
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def on_add_savings(self, goal_id: int, goal_name: str, remaining: float):
        amount, ok = QInputDialog.getDouble(
            self, "Add Savings", f"How much are you adding toward '{goal_name}'?\n(Remaining: ${remaining:,.2f})",
            min=0.01, max=max(remaining, 0.01), decimals=2
        )
        if not ok:
            return

        try:
            self.service.add_savings(goal_id, amount)
            self.load_goals()
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def on_delete(self, goal_id: int):
        confirm = QMessageBox.question(
            self, "Delete Goal",
            "Are you sure you want to delete this goal?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            self.service.delete_goal(goal_id)
            self.load_goals()
