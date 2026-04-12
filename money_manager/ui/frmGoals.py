from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QFrame, QLabel, QProgressBar

from services.goal_service import GoalService
from ui.ui_frmGoals import Ui_GoalsDialog


class GoalDetailDialog(QtWidgets.QDialog):
    def __init__(self, goal, service: GoalService, parent=None):
        super().__init__(parent)
        self.goal = goal
        self.service = service
        self.setWindowTitle(goal.name)
        self.setWindowIcon(QIcon("resources\\icons\\logo.png"))
        self.setMinimumWidth(400)
        self.resize(420, 320)

        self.layout_ = QtWidgets.QVBoxLayout(self)
        self.layout_.setSpacing(14)
        self.layout_.setContentsMargins(24, 24, 24, 24)

        self.lbl_name = QLabel(goal.name)
        name_font = QFont()
        name_font.setPointSize(16)
        name_font.setBold(True)
        self.lbl_name.setFont(name_font)
        self.lbl_name.setAlignment(Qt.AlignCenter)
        self.layout_.addWidget(self.lbl_name)

        self.lbl_amounts = QLabel()
        self.lbl_amounts.setAlignment(Qt.AlignCenter)
        self.lbl_amounts.setStyleSheet("font-size: 13px;")
        self.layout_.addWidget(self.lbl_amounts)

        self.bar = QProgressBar()
        self.bar.setMinimum(0)
        self.bar.setMaximum(100)
        self.bar.setFixedHeight(32)
        self.bar.setTextVisible(True)
        self.bar.setStyleSheet(
            """
            QProgressBar {
                border: 1px solid #555;
                border-radius: 8px;
                text-align: center;
                font-size: 12px;
                font-weight: bold;
            }
            QProgressBar::chunk {
                border-radius: 8px;
                background-color: #36A2EB;
            }
            """
        )
        self.layout_.addWidget(self.bar)

        self.lbl_remaining = QLabel()
        self.lbl_remaining.setAlignment(Qt.AlignCenter)
        self.lbl_remaining.setStyleSheet("color: grey; font-size: 11px;")
        self.layout_.addWidget(self.lbl_remaining)

        self.btn_save = QtWidgets.QPushButton("+ Add Savings")
        self.btn_save.setFixedHeight(36)
        self.btn_save.setStyleSheet(
            "QPushButton { background-color: #36A2EB; color: white; border-radius: 6px; font-size: 13px; }"
            "QPushButton:hover { background-color: #5BB8FF; }"
        )
        self.btn_save.clicked.connect(self.add_savings)
        self.layout_.addWidget(self.btn_save)

        btn_close = QtWidgets.QPushButton("Close")
        btn_close.setFixedHeight(34)
        btn_close.clicked.connect(self.close)
        self.layout_.addWidget(btn_close)

        self.refresh()

    def refresh(self):
        goals = self.service.get_all_goals()
        updated = next((g for g in goals if g.id == self.goal.id), None)
        if updated:
            self.goal = updated

        pct = self.goal.progress_percent
        self.bar.setValue(pct)

        if self.goal.is_complete:
            self.lbl_amounts.setText(
                f"<b style='color:#4BC0C0'>Goal Complete!</b>  ${self.goal.saved_amount:,.2f} saved"
            )
            self.lbl_remaining.setText("You reached your goal!")
            self.bar.setStyleSheet(self.bar.styleSheet().replace("#36A2EB", "#4BC0C0"))
            self.btn_save.setVisible(False)
        else:
            remaining = self.goal.target_amount - self.goal.saved_amount
            self.lbl_amounts.setText(
                f"Saved: <b>${self.goal.saved_amount:,.2f}</b> &nbsp;/&nbsp; Target: <b>${self.goal.target_amount:,.2f}</b>"
            )
            self.lbl_remaining.setText(f"${remaining:,.2f} remaining")
            self.btn_save.setVisible(True)

    def add_savings(self):
        remaining = self.goal.target_amount - self.goal.saved_amount
        amount, ok = QtWidgets.QInputDialog.getDouble(
            self,
            "Add Savings",
            f"How much are you adding toward '{self.goal.name}'?\n(Remaining: ${remaining:,.2f})",
            0.01,
            0.01,
            max(remaining, 0.01),
            2,
        )
        if not ok:
            return

        try:
            self.service.add_savings(self.goal.id, amount)
            self.refresh()
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))


class GoalCard(QFrame):
    def __init__(self, goal, service: GoalService, on_delete, parent_dialog):
        super().__init__()
        self.goal = goal
        self.service = service
        self.parent_dialog = parent_dialog
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setStyleSheet("QFrame { background-color: #1e1e2e; border-radius: 8px; padding: 4px; }")
        self.setCursor(Qt.PointingHandCursor)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(6)

        top = QtWidgets.QHBoxLayout()
        name_label = QLabel(goal.name)
        name_font = QFont()
        name_font.setPointSize(12)
        name_font.setBold(True)
        name_label.setFont(name_font)
        name_label.setStyleSheet("color: white;")
        top.addWidget(name_label)
        top.addStretch()

        btn_delete = QtWidgets.QPushButton("x")
        btn_delete.setFixedSize(24, 24)
        btn_delete.setStyleSheet("color: #ff5457; background: transparent; border: none; font-size: 14px;")
        btn_delete.clicked.connect(lambda: on_delete(goal.id))
        top.addWidget(btn_delete)
        layout.addLayout(top)

        status_color = "#4BC0C0" if goal.is_complete else "white"
        status_text = "COMPLETE!" if goal.is_complete else f"${goal.saved_amount:,.2f} of ${goal.target_amount:,.2f}"
        amounts_label = QLabel(status_text)
        amounts_label.setStyleSheet(f"color: {status_color}; font-size: 11px;")
        layout.addWidget(amounts_label)

        bar = QProgressBar()
        bar.setMinimum(0)
        bar.setMaximum(100)
        bar.setValue(goal.progress_percent)
        bar.setTextVisible(True)
        bar.setFixedHeight(20)
        chunk_color = "#4BC0C0" if goal.is_complete else "#36A2EB"
        bar.setStyleSheet(f"QProgressBar::chunk {{ background-color: {chunk_color}; }}")
        layout.addWidget(bar)

        hint = QLabel("Click to view details")
        hint.setStyleSheet("color: #555; font-size: 10px;")
        hint.setAlignment(Qt.AlignRight)
        layout.addWidget(hint)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            detail = GoalDetailDialog(self.goal, self.service, self.parent_dialog)
            detail.exec()
            self.parent_dialog.load_goals()
        super().mousePressEvent(event)


class GoalsDialog(QtWidgets.QDialog, Ui_GoalsDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.service = GoalService()

        self.setWindowTitle("Savings Goals")
        self.setWindowIcon(QIcon("resources\\icons\\logo.png"))

        self.btnAddGoal.clicked.connect(self.add_goal)
        self.btnCloseGoals.clicked.connect(self.close)

        self.load_goals()

    def load_goals(self):
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
            card = GoalCard(goal, self.service, self.on_delete, self)
            self.goals_layout.insertWidget(i, card)

    def add_goal(self):
        name, ok = QtWidgets.QInputDialog.getText(self, "New Goal", "What are you saving for?")
        if not ok or not name.strip():
            return

        target, ok = QtWidgets.QInputDialog.getDouble(
            self,
            "Target Amount",
            f"How much do you want to save for '{name.strip()}'?",
            0.0,
            0.01,
            1_000_000,
            2,
        )
        if not ok:
            return

        initial, ok = QtWidgets.QInputDialog.getDouble(
            self,
            "Initial Savings",
            f"How much are you putting in now toward '{name.strip()}'?\n(You can add more later)",
            0.0,
            0.0,
            target,
            2,
        )
        if not ok:
            return

        try:
            self.service.add_goal(name, target, initial)
            self.load_goals()
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def on_delete(self, goal_id: int):
        confirm = QtWidgets.QMessageBox.question(
            self,
            "Delete Goal",
            "Are you sure you want to delete this goal?",
            QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No,
            QtWidgets.QMessageBox.StandardButton.No,
        )
        if confirm == QtWidgets.QMessageBox.StandardButton.Yes:
            self.service.delete_goal(goal_id)
            self.load_goals()
