

from PySide6 import QtCore, QtGui, QtWidgets

class DashBoardService() :
    def __init__(self):
        pass
           
    def show_about(self):
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("About This App")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)

            msg.setText(
                "Expense Manager v1.0\n"
                "\n"
                "A simple tool for managing expenses and tracking your budget.\n"
                "Developer: Team Student\n\n"
                "Click below to visit my GitHub page:"
            )

            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            btn_link = msg.addButton("Open GitHub", QtWidgets.QMessageBox.ButtonRole.ActionRole)
            msg.exec()

            if msg.clickedButton() == btn_link:
                QtGui.QDesktopServices.openUrl(
                    QtCore.QUrl("https://github.com/anasemadanas/Expense_Track")
                )
        
    def save_data(self):
        print("Saving…")
       
    def open_guide(self):
        pdf_path = "https://github.com/anasemadanas/Expense_Track"  

        url = QtCore.QUrl.fromLocalFile(pdf_path)
        QtGui.QDesktopServices.openUrl(url)      
        
    def export_data(self):
        file, _ = QtWidgets.QFileDialog.getSaveFileName(
            None,
            "Export Data",
             "Summary_Budget.csv",
            "CSV Files (*.csv);;All Files (*)"
        )
        if file:
            print("Export to:", file)   