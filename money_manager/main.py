import sys
from PySide6 import QtWidgets
from ui.frmLoginScreen import LoginScreen

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.show_ui = LoginScreen()
        self.show_ui.setupUi(self)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())