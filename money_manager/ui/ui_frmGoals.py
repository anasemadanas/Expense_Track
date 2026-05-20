# -*- coding: utf-8 -*-

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
    QFrame,
)


class Ui_GoalsDialog(object):
    def setupUi(self, GoalsDialog):
        if not GoalsDialog.objectName():
            GoalsDialog.setObjectName(u"GoalsDialog")
        GoalsDialog.resize(520, 580)
        GoalsDialog.setMinimumSize(480, 500)

        self.lblTitleGoals = QLabel(GoalsDialog)
        self.lblTitleGoals.setObjectName(u"lblTitleGoals")
        self.lblTitleGoals.setGeometry(QRect(100, 20, 321, 51))
        title_font = QFont()
        title_font.setPointSize(18)
        title_font.setBold(True)
        self.lblTitleGoals.setFont(title_font)
        self.lblTitleGoals.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.btnAddGoal = QPushButton(GoalsDialog)
        self.btnAddGoal.setObjectName(u"btnAddGoal")
        self.btnAddGoal.setGeometry(QRect(40, 90, 441, 36))
        self.btnAddGoal.setStyleSheet(
            "QPushButton { background-color: rgb(0,200,0); color: black; font-size: 13px; "
            "border-radius: 6px; font-weight: bold; }"
            "QPushButton:hover { background-color: rgb(0,230,0); }"
        )

        self.scrollAreaGoals = QScrollArea(GoalsDialog)
        self.scrollAreaGoals.setObjectName(u"scrollAreaGoals")
        self.scrollAreaGoals.setGeometry(QRect(30, 140, 461, 371))
        self.scrollAreaGoals.setWidgetResizable(True)
        self.scrollAreaGoals.setFrameShape(QFrame.Shape.NoFrame)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 461, 371))

        self.goals_layout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.goals_layout.setObjectName(u"goals_layout")
        self.goals_layout.setSpacing(10)
        self.goals_layout.addStretch()

        self.scrollAreaGoals.setWidget(self.scrollAreaWidgetContents)

        self.btnCloseGoals = QPushButton(GoalsDialog)
        self.btnCloseGoals.setObjectName(u"btnCloseGoals")
        self.btnCloseGoals.setGeometry(QRect(30, 525, 461, 34))

        self.retranslateUi(GoalsDialog)
        QMetaObject.connectSlotsByName(GoalsDialog)

    def retranslateUi(self, GoalsDialog):
        GoalsDialog.setWindowTitle(QCoreApplication.translate("GoalsDialog", u"Dialog", None))
        self.lblTitleGoals.setText(QCoreApplication.translate("GoalsDialog", u"My Savings Goals", None))
        self.btnAddGoal.setText(QCoreApplication.translate("GoalsDialog", u"+ New Goal", None))
        self.btnCloseGoals.setText(QCoreApplication.translate("GoalsDialog", u"Close", None))
