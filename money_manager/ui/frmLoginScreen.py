from PySide6 import QtCore, QtGui, QtWidgets
from Services.user_service import UserService
from PySide6.QtGui import Qt, QIcon
from ui.ui_frmLogin import Ui_LoginScreen

class LoginScreen(QtWidgets.QWidget, Ui_LoginScreen):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.user_service = UserService()
        
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon("resources\\icons\\login.png"))
        
        # Error label
        self.lblError = QtWidgets.QLabel(self)   
        self.lblError.setGeometry(QtCore.QRect(60, 215, 360, 25))
        self.lblError.setStyleSheet("color: red;")
        self.lblError.setObjectName("lblError")
        self.lblError.setText("")
        
        self.ui.btnLogin.clicked.connect(self.try_login)
        self.ui.btnClose.clicked.connect(self.close)
    # ---- ------------------------------------------------------------- ----
            
    def try_login(self):

        username = self.ui.lneUsername.text().strip()
        password = self.ui.lnePassword.text().strip()
        
        if not username or not password:
            self.lblError.setText("Please enter username and password.")
            return

        try:
            if self.user_service.login(username, password):
                self.lblError.setText("")
                
                import data.app_state as app_state
                user = self.user_service.login2(username, password)
                app_state.current_user = user
                
                self.open_Dashboard()
            else:
                remaining = self.user_service.max_attempts - self.user_service.login_attempts
                self.lblError.setText(f"Invalid credentials! {remaining} attempts left.")

        except Exception as e:
                print("Login error:", e)
                self.lock_account()

                
    def lock_account(self):
        self.ui.btnLogin.setEnabled(False)
        self.ui.lneUsername.setEnabled(False)
        self.ui.lnePassword.setEnabled(False)
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg.setWindowTitle("Account Locked")
        msg.setText("You have exceeded the maximum login attempts!")
        msg.setInformativeText("Please contact the administrator.")
        msg.exec()
        
    def open_Dashboard(self):
            from ui.frmdashboard import MainScreen
            self.dashboard = MainScreen()
            self.dashboard.show()
            self.close()
            
            
    def try_login2(self):
        username = self.ui.lneUsername.text().strip()
        password = self.ui.lnePassword.text().strip()
        
        if not username or not password:
            self.lblError.setText("Please enter username and password.")
            return

        try:
            current_user = self.user_service.login2(username, password)
            if current_user:
                self.lblError.setText("")
                self.user_perm = current_user["permissions"]
                self.current_user = current_user
                self.open_Dashboard()
            else:
                remaining = self.user_service.max_attempts - self.user_service.login_attempts
                self.lblError.setText(f"Invalid credentials! {remaining} attempts left.")
        except Exception as e:
            print("Login error:", e)
            self.lock_account()
        