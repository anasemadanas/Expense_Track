from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import Qt, QIcon
from common.activity_logger import ActivityLogger
from services.user_service import UserService
from ui.ui_frmLogin import Ui_LoginScreen
from common.utils import resource_path


class AccountDialog(QtWidgets.QDialog):
    def __init__(self, title, action_text, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setModal(True)
        self.resize(360, 220)

        layout = QtWidgets.QFormLayout(self)
        self.username = QtWidgets.QLineEdit()
        self.recovery_key = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.confirm_password = QtWidgets.QLineEdit()
        self.recovery_key.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirm_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        layout.addRow("Username", self.username)
        layout.addRow("Recovery code", self.recovery_key)
        layout.addRow("New password", self.password)
        layout.addRow("Confirm password", self.confirm_password)

        buttons = QtWidgets.QDialogButtonBox()
        action_button = buttons.addButton(action_text, QtWidgets.QDialogButtonBox.ButtonRole.AcceptRole)
        buttons.addButton(QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        action_button.clicked.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

    def values(self):
        return (
            self.username.text(),
            self.recovery_key.text(),
            self.password.text(),
            self.confirm_password.text(),
        )


class RecoverySetupDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Set recovery code")
        layout = QtWidgets.QFormLayout(self)
        notice = QtWidgets.QLabel(
            "Create a recovery code for password resets.\n"
            "Keep it private; it cannot be shown later."
        )
        self.recovery_key = QtWidgets.QLineEdit()
        self.confirm_recovery_key = QtWidgets.QLineEdit()
        self.recovery_key.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.confirm_recovery_key.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        layout.addRow(notice)
        layout.addRow("Recovery code", self.recovery_key)
        layout.addRow("Confirm code", self.confirm_recovery_key)

        buttons = QtWidgets.QDialogButtonBox()
        save_button = buttons.addButton("Save", QtWidgets.QDialogButtonBox.ButtonRole.AcceptRole)
        save_button.clicked.connect(self.accept)
        layout.addRow(buttons)

    def values(self):
        return self.recovery_key.text(), self.confirm_recovery_key.text()


class LoginScreen(QtWidgets.QWidget, Ui_LoginScreen):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.user_service = UserService()
        self.resize(474, 400)
        
        self.setWindowTitle("Login")

        self.setWindowIcon(QIcon(resource_path("resources/icons/login.png")))
        self.lblError = QtWidgets.QLabel(self)   
        self.lblError.setGeometry(QtCore.QRect(60, 215, 360, 25))
        self.lblError.setStyleSheet("color: red;")
        self.lblError.setObjectName("lblError")
        self.lblError.setText("")
        
        self.ui.btnLogin.clicked.connect(self.try_login)
        self.ui.btnClose.clicked.connect(self.close)

        self.btnCreateAccount = QtWidgets.QPushButton("Create account", self)
        self.btnCreateAccount.setGeometry(70, 320, 151, 36)
        self.btnCreateAccount.clicked.connect(self.create_account)

        self.btnForgotPassword = QtWidgets.QPushButton("Forgot password?", self)
        self.btnForgotPassword.setGeometry(240, 320, 151, 36)
        self.btnForgotPassword.clicked.connect(self.reset_password)
        
        self.btnTheme = QtWidgets.QPushButton("Theme", self)
        self.btnTheme.setGeometry(10, 10, 80, 30)

        self.btnDefault = QtWidgets.QPushButton("Default", self)
        self.btnDefault.setGeometry(10, 50, 80, 30)

        self.ui.lblManagerMoney.setMinimumWidth(300)
        
        self.setTabOrder(self.ui.lneUsername, self.ui.lnePassword)
        self.setTabOrder(self.ui.lnePassword, self.ui.btnLogin)
        self.setTabOrder(self.ui.btnLogin, self.ui.btnClose)
        self.setTabOrder(self.ui.btnClose, self.btnCreateAccount)
        self.setTabOrder(self.btnCreateAccount, self.btnForgotPassword)
        self.setTabOrder(self.btnForgotPassword, self.btnTheme)
        self.setTabOrder(self.btnTheme, self.btnDefault)
        
    # ---- ------------------------------------------------------------- ----
            
    def try_login(self):
        username = self.ui.lneUsername.text().strip()
        password = self.ui.lnePassword.text()
        self.lblError.setStyleSheet("color: red;")
        
        if not username or not password:
            self.lblError.setText("Please enter username and password.")
            return

        try:
            user = self.user_service.login(username, password)
            if user:
                if not user.get("has_recovery_key") and not self.setup_recovery_key(user):
                    return
                self.lblError.setText("")
                import common.global_user as global_user
                global_user.current_user = user  
                self.current_user = user
                ActivityLogger.log_login(user["username"])
                
                self.open_Dashboard()
            else:
                remaining = self.user_service.max_attempts - self.user_service.login_attempts
                self.lblError.setText(f"Invalid credentials! {remaining} attempts left.")
        except Exception as e:
            self.lblError.setText(str(e))
            self.lock_account()

    def setup_recovery_key(self, user):
        while True:
            dialog = RecoverySetupDialog(self)
            if dialog.exec() != QtWidgets.QDialog.DialogCode.Accepted:
                self.lblError.setText("Set a recovery code to continue.")
                return False
            try:
                recovery_key, confirm_recovery_key = dialog.values()
                self.user_service.set_recovery_key(user["id"], recovery_key, confirm_recovery_key)
                user["has_recovery_key"] = True
                return True
            except ValueError as exc:
                QtWidgets.QMessageBox.warning(self, "Recovery Code", str(exc))
        
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

    def create_account(self):
        dialog = AccountDialog("Create account", "Create", self)
        if dialog.exec() != QtWidgets.QDialog.DialogCode.Accepted:
            return

        try:
            username, recovery_key, password, confirm_password = dialog.values()
            self.user_service.register(username, password, confirm_password, recovery_key)
            self.ui.lneUsername.setText(username.strip().lower())
            self.ui.lnePassword.clear()
            self.lblError.setStyleSheet("color: green;")
            self.lblError.setText("Account created. Please log in.")
        except ValueError as exc:
            QtWidgets.QMessageBox.warning(self, "Create Account", str(exc))

    def reset_password(self):
        dialog = AccountDialog("Reset password", "Reset", self)
        if dialog.exec() != QtWidgets.QDialog.DialogCode.Accepted:
            return

        try:
            username, recovery_key, password, confirm_password = dialog.values()
            self.user_service.reset_password(username, recovery_key, password, confirm_password)
            self.ui.btnLogin.setEnabled(True)
            self.ui.lneUsername.setEnabled(True)
            self.ui.lnePassword.setEnabled(True)
            self.ui.lneUsername.setText(username.strip().lower())
            self.ui.lnePassword.clear()
            self.lblError.setStyleSheet("color: green;")
            self.lblError.setText("Password reset. Please log in.")
        except ValueError as exc:
            QtWidgets.QMessageBox.warning(self, "Reset Password", str(exc))
         
    def open_Dashboard(self):        
        from ui.frmdashboard import MainScreen
        self.dashboard = MainScreen(self.current_user) 
        self.dashboard.show()
        self.close()
