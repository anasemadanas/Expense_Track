from PySide6 import QtCore, QtGui, QtWidgets
import sys

from Services.user_service import UserService
    
class LoginScreen(object):

    def __init__(self):
        self.service = UserService()
    
    
    def setupUi(self, LoginScreen):
        
        LoginScreen.setObjectName("LoginScreen")
        LoginScreen.resize(474, 340)
        LoginScreen.setWindowTitle("Login - Money Manager")

        # ── Title  ──────────────────────────────────────────────────────
        self.lblManagerMoney = QtWidgets.QLabel(LoginScreen)
        self.lblManagerMoney.setGeometry(QtCore.QRect(80, 20, 320, 71))
        font_big = QtGui.QFont()
        font_big.setFamily("Segoe UI")
        font_big.setPointSize(24)
        self.lblManagerMoney.setFont(font_big)
        self.lblManagerMoney.setStyleSheet("color: rgb(85, 0, 255);")
        self.lblManagerMoney.setObjectName("lblManagerMoney")

        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)

        # ── Username ──────────────────────────────────────────────────────────
        self.lblUsername = QtWidgets.QLabel(LoginScreen)
        self.lblUsername.setGeometry(QtCore.QRect(90, 120, 110, 31))
        self.lblUsername.setFont(font)
        self.lblUsername.setObjectName("lblUsername")

        self.lneUsername = QtWidgets.QLineEdit(LoginScreen)
        self.lneUsername.setGeometry(QtCore.QRect(210, 120, 181, 31))
        self.lneUsername.setFont(font)
        self.lneUsername.setObjectName("lneUsername")

        # ── Password ──────────────────────────────────────────────────────────
        self.lblPassword = QtWidgets.QLabel(LoginScreen)
        self.lblPassword.setGeometry(QtCore.QRect(90, 170, 110, 31))
        self.lblPassword.setFont(font)
        self.lblPassword.setStyleSheet("color: rgb(255, 0, 0);")
        self.lblPassword.setObjectName("lblPassword")

        self.lnePassword = QtWidgets.QLineEdit(LoginScreen)
        self.lnePassword.setGeometry(QtCore.QRect(210, 170, 181, 31))
        self.lnePassword.setFont(font)
        self.lnePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lnePassword.setObjectName("lnePassword")

        # ── Buttons ───────────────────────────────────────────────────────────
        self.btnLogin = QtWidgets.QPushButton(LoginScreen)
        self.btnLogin.setGeometry(QtCore.QRect(80, 250, 141, 51))
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")

        self.btnClose = QtWidgets.QPushButton(LoginScreen)
        self.btnClose.setGeometry(QtCore.QRect(260, 250, 141, 51))
        self.btnClose.setFont(font)
        self.btnClose.setObjectName("btnClose")

        # ── Error label  ───────────────────────────────────
        self.lblError = QtWidgets.QLabel(LoginScreen)
        self.lblError.setGeometry(QtCore.QRect(60, 215, 360, 25))
        self.lblError.setStyleSheet("color: red;")
        self.lblError.setText("")
        self.lblError.setObjectName("lblError")


        # ── Call  ───────────────────────────────────────────────────────────
        self.btnLogin.clicked.connect(self.try_login)
        self.btnClose.clicked.connect(LoginScreen.close)

        self.LoginScreen = LoginScreen
        self.retranslateUi(LoginScreen)
        QtCore.QMetaObject.connectSlotsByName(LoginScreen)
        
    # ── Translations ──────────────────────────────────────────────────────────
    def retranslateUi(self, LoginScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginScreen.setWindowTitle(_translate("LoginScreen", "Login"))
        self.btnLogin.setText(_translate("LoginScreen", "Login"))
        self.lblUsername.setText(_translate("LoginScreen", "Username"))
        self.lblPassword.setText(_translate("LoginScreen", "Password"))
        self.btnClose.setText(_translate("LoginScreen", "Close"))
        self.lblManagerMoney.setText(_translate("LoginScreen", "Money Manager"))


    # ── Login  ───────────────────────────────────────────────────────────
    
    def try_login(self):

        username = self.lneUsername.text().strip()
        password = self.lnePassword.text().strip()

        if not username or not password:
            self.lblError.setText("Please enter username and password.")
            return

        try:                
            if self.service.login(username, password):
                self.lblError.setText("")
                self.open_manager()
            else:
                remaining = self.service.max_attempts - self.service.login_attempts
                self.lblError.setText(f"Invalid credentials! {remaining} attempts left.")

        except Exception as e:
            self.lblError.setText("Too many attempts! Access denied.")
            self.btnLogin.setEnabled(False)        
            self.lneUsername.setEnabled(False)
            self.lnePassword.setEnabled(False)
            
            msg_box = QtWidgets.QMessageBox()
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            msg_box.setWindowTitle("Access Denied")
            msg_box.setText("Contact Admin, Too many login attempts!")
            msg_box.setInformativeText("You have exceeded the maximum number of login attempts.")
            msg_box.exec()



    def open_manager(self):
        try:
            from ui.frmdashboard import MainScreen   

            self.main_window = QtWidgets.QMainWindow()
            self.open_Main_ui = MainScreen()
            self.open_Main_ui.setupUi(self.main_window)
            self.main_window.show()
            self.LoginScreen.close()
            
        except Exception as e:
            self.lblError.setText("Error opening main window!")
            print("Open Manager Error:", e)


