from PySide6 import QtCore, QtGui, QtWidgets

from ui.ui_frmdashboard import Ui_MainScreen
from PySide6 import QtCharts

class MainScreen(QtWidgets.QMainWindow, Ui_MainScreen):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

  
   
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainScreen()
    window.show()
    sys.exit(app.exec_())