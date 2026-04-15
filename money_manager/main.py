import sys
from PySide6 import QtWidgets
from ui.frmLoginScreen import LoginScreen
from database.database_setup import initialize_database 

if __name__ == "__main__":
    initialize_database()
    app = QtWidgets.QApplication(sys.argv)
    window = LoginScreen()
    window.show()
    sys.exit(app.exec())