import sys
from PySide6 import QtWidgets
import PySide6
from ui.frmLoginScreen import LoginScreen

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = LoginScreen()
    window.show()

    sys.exit(app.exec())