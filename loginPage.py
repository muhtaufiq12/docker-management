import sys

from PyQt5 import QtWidgets, QtCore, QtGui, Qt

class MainWindow:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        # self.app = QtGui.QFontDatabase.addApplicationFont('/home/taufiq/Documents/DATA/docker-management/assets/fonts/')
        self.window = QtWidgets.QMainWindow()
        
        self.logoPath = "/home/taufiq/Documents/DATA/docker-management/assets/images/boss.png"

        self.initGui()


        self.window.setWindowTitle("Mata Elang Sensor Management")
        self.window.setGeometry(0, 0, 1440, 1024)

        self.window.show()
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
        self.loginBtn.setStyleSheet("background-color: #4e4e4e; color: #fafafa; font-size: 15px; border: 1px solid #4e4e4e")

        


main = MainWindow()