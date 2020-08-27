import sys
import os
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from dockerManagement import *

db_connection = sqlite3.connect("db_sensor.db")

class Ui_MainWindow(object):
    def setup(self, MainWindow):

        # MainWindow Settings
        MainWindow.setObjectName("LoginWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Central Widgets Settings
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Login Frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(460, 190, 421, 431))
        self.frame.setStyleSheet("background-color: rgb(71, 206, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Login Frame - Mata Elang Logo
        self.mataelangLogo = QtWidgets.QLabel(self.frame)
        self.mataelangLogo.setGeometry(QtCore.QRect(160, 40, 121, 111))
        self.mataelangLogo.setText("")
        self.mataelangLogo.setPixmap(QtGui.QPixmap("assets/icon/mata elang 52-02.png"))
        self.mataelangLogo.setScaledContents(True)
        self.mataelangLogo.setObjectName("mataelangLogo")

        # Login Frame - Username Field
        self.usernameLabel = QtWidgets.QLabel(self.frame)
        self.usernameLabel.setGeometry(QtCore.QRect(20, 170, 71, 21))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernamelineEdit = QtWidgets.QLineEdit(self.frame)
        self.usernamelineEdit.setGeometry(QtCore.QRect(20, 190, 381, 41))
        self.usernamelineEdit.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.usernamelineEdit.setObjectName("usernamelineEdit")

        # Login Frame - Password Field
        self.passwordLabel = QtWidgets.QLabel(self.frame)
        self.passwordLabel.setGeometry(QtCore.QRect(20, 260, 71, 21))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordlineEdit = QtWidgets.QLineEdit(self.frame)
        self.passwordlineEdit.setGeometry(QtCore.QRect(20, 280, 381, 41))
        self.passwordlineEdit.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.passwordlineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.passwordlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordlineEdit.setObjectName("passwordlineEdit")

        # Login Frame - Login Button
        self.loginButton = QtWidgets.QPushButton(self.frame)
        self.loginButton.setGeometry(QtCore.QRect(20, 350, 381, 51))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.loginButton.setFont(font)
        self.loginButton.setStyleSheet("background-color: #6052FF;\n"
"color: rgb(255, 255, 255);")
        self.loginButton.clicked.connect(self.login)
        self.loginButton.setObjectName("loginButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Docker Management"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.passwordLabel.setText(_translate("MainWindow", "Password"))
        self.loginButton.setText(_translate("MainWindow", "Login"))
    
    def login(self):
        username = self.usernamelineEdit.text()
        password = self.passwordlineEdit.text()

        db = db_connection.cursor()
        db.execute("SELECT * FROM tb_user")
        data_admin = db.fetchall()
        for x in data_admin:
            usernameAdmin = x[1]
            passwordAdmin = x[2]
        
        if username == usernameAdmin and password == passwordAdmin:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow1()
            self.ui.setup(self.window)
            self.window.show()
            MainWindow.hide()
            
        else:
            QMessageBox.warning(QMessageBox(), 'Error', 'Invalid Username or Password')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
