from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("Mata-Elang-Management.ui", self)

        #Dashboard Page
        self.dashboardPage = self.findChild(QStackedWidget.stackedWidget, "dashboardPage")
        self.dahboardButton = self.findChild(QPushButton, "dashboardButton")
        self.dashboardButton.clicked.connect(self.dashboardPage)


        self.show()



app = QApplication(sys.argv)
window = UI()
app.exec_()