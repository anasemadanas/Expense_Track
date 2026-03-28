from PyQt5.QtGui import QStandardItemModel, QStandardItem

self.model = QStandardItemModel()
self.model.setHorizontalHeaderLabels(["Date", "Category", "Amount", "Note"])

self.lstTransaction.setModel(self.model)