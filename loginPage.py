import sys

from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from MataElangManagement import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        # self.app = QtGui.QFontDatabase.addApplicationFont('/home/taufiq/Documents/DATA/docker-management/assets/fonts/')
        self.window = QtWidgets.QMainWindow()
        
        self.logoPath = "/home/taufiq/Documents/DATA/docker-management/assets/images/boss.png"

        self.stylesheet = """

        QPushButton#loginBtn{
            background-color: #6052FF;
            color: #fafafa; 
            font-size: 15px; 
            border-radius: 10px;
        }

        """

        self.initGui()


        self.window.setWindowTitle("Mata Elang Sensor Management")
        self.window.setGeometry(0, 0, 1440, 1024)

        self.window.show()
        self.app.setStyleSheet(self.stylesheet)
        sys.exit(self.app.exec_())
    
    def initGui(self):
        #Create the labels that holds Mata Elang Logo
        self.label = QtWidgets.QLabel(self.window)
        self.label.setGeometry(583, 120, 200, 200)
        
        #Show Logo
        self.image = QtGui.QImage(self.logoPath)
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)

        self.label.setPixmap(self.pixmapImage)
        self.label.setScaledContents(True)

        #Create Username field
        self.usernameLabel = QtWidgets.QLabel(self.window)
        self.usernameLabel.setText("Username")
        self.usernameLabel.setGeometry(583, 350, 84, 24)

        self.usernameField = QtWidgets.QTextEdit(self.window)
        self.usernameField.setGeometry(583, 380, 220, 25)
        self.usernameField.setObjectName("usernameField")
        self.usernameField.setText("Username")

        #Create Password field
        self.passwordLabel = QtWidgets.QLabel(self.window)
        self.passwordLabel.setText("Password")
        self.passwordLabel.setGeometry(583, 410, 84, 24)

        self.passwordField = QtWidgets.QTextEdit(self.window)
        self.passwordField.setGeometry(583, 440, 220, 25)
        self.passwordField.setText("Password")

        #Create Login Button
        self.loginBtn = QtWidgets.QPushButton(self.window)
        self.loginBtn.setGeometry(583, 480, 220, 40)
        self.loginBtn.setText("Login")
        self.loginBtn.setObjectName("loginBtn")
        self.loginBtn.clicked.connect(self.openLayout)
        
    def openLayout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        


main = MainWindow()