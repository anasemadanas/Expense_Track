import sys
from PySide6 import QtWidgets
from ui.frmLoginScreen import LoginScreen
from database.database_setup import initialize_database 
from common.theme_manager import ThemeManager

if __name__ == "__main__":
    initialize_database()
    app = QtWidgets.QApplication(sys.argv)
    
    window = LoginScreen()
    theme = ThemeManager(app)
    
    theme.apply_theme()
    window.btnTheme.clicked.connect(theme.choose_color)
    window.btnDefault.clicked.connect(theme.reset_theme)

    window.show()
    sys.exit(app.exec())
    