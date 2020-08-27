import sys
import os
import subprocess
import shutil
import sqlite3
import json
import shlex

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from loginPage import *


db_connection = sqlite3.connect("db_sensor.db")

class Ui_MainWindow1(object):

    def setup(self, MainWindow):
        
        # MainWindow Settings
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        # Central Widgets Settings
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Stack Widgets Settings
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(150, 0, 1211, 701))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.stackedWidget.setObjectName("stackedWidget")
        
        # Dashboard Page
        self.dashboardPage = QtWidgets.QWidget()
        self.dashboardPage.setObjectName("dashboardPage")
        
        # Dashboard Page - Dashboard Label
        self.headerDashboardLabel = QtWidgets.QLabel(self.dashboardPage)
        self.headerDashboardLabel.setGeometry(QtCore.QRect(20, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(24)
        self.headerDashboardLabel.setFont(font)
        self.headerDashboardLabel.setObjectName("headerDashboardLabel")
        
        # Dashboard Page - Add Sensor Button
        self.toolButton_6 = QtWidgets.QToolButton(self.dashboardPage)
        self.toolButton_6.setGeometry(QtCore.QRect(20, 80, 91, 81))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.toolButton_6.setFont(font)
        self.toolButton_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.toolButton_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icon/add-32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_6.setIcon(icon)
        self.toolButton_6.setIconSize(QtCore.QSize(52, 52))
        self.toolButton_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_6.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(3))
        self.toolButton_6.setObjectName("toolButton_6")

        
        #Dashboard Page - refresh Button
        self.refreshButtonDashboard = QtWidgets.QToolButton(self.dashboardPage)
        self.refreshButtonDashboard.setGeometry(QtCore.QRect(120, 71, 91, 81))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.refreshButtonDashboard.setFont(font)
        self.refreshButtonDashboard.setFocusPolicy(QtCore.Qt.NoFocus)
        self.refreshButtonDashboard.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/icon/refresh-52.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshButtonDashboard.setIcon(icon)
        self.refreshButtonDashboard.setIconSize(QtCore.QSize(52, 52))
        self.refreshButtonDashboard.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.refreshButtonDashboard.clicked.connect(self.loadData)
        self.refreshButtonDashboard.setObjectName("refreshButtonDashboard")

        # Dashboard Page - Sensor List Table
        self.sensorListTable = QtWidgets.QTableWidget(self.dashboardPage)
        self.sensorListTable.setGeometry(QtCore.QRect(20, 180, 731, 400))
        self.sensorListTable.setObjectName("sensorListTable")
        self.sensorListTable.setColumnCount(5)
        self.sensorListTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.sensorListTable.setHorizontalHeaderLabels(("Device ID","Device Name", "Protected Subnet", "IP Address", "Company"))

        
        self.loadData()
        
        # # Dashboard Page - Sensor List Table
        # self.sensorListTable = QtWidgets.QTableWidget(self.dashboardPage)
        # self.sensorListTable.setGeometry(QtCore.QRect(20, 180, 731, 400))
        # self.sensorListTable.setObjectName("sensorListTable")
        # self.sensorListTable.setColumnCount(5)
        # self.sensorListTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # self.sensorListTable.setHorizontalHeaderLabels(("Device ID","Device Name", "Protected Subnet", "IP Address", "Company"))

        # # Dashboard Page - Sensor List Table - Query untuk menampilkan data sensor
        # db = db_connection.cursor()
        # db.execute("SELECT deviceID, deviceName, protectedSubnet, mqttIP, company FROM tb_sensor_env")
        # data_sensor = db.fetchall()
        # self.sensorListTable.setRowCount(0)
        # for row_number, row_data in enumerate(data_sensor):
        #     self.sensorListTable.insertRow(row_number)
        #     for colum_number, data in enumerate(row_data):
        #         self.sensorListTable.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
        
        
        self.stackedWidget.addWidget(self.dashboardPage)

        # Container Page
        self.containerPage = QtWidgets.QWidget()
        self.containerPage.setObjectName("containerPage")

        # Container Page - List Container 
        self.listContainer1 = QtWidgets.QListWidget(self.containerPage)
        self.listContainer1.setGeometry(QtCore.QRect(10, 10, 201, 691))
        self.listContainer1.setObjectName("listContainer1")
        
       
        self.loadDataContainerPage()
        # query_data = db_connection.cursor()
        # query_data.execute("SELECT deviceName FROM tb_sensor_env")
        # data_sensor = query_data.fetchall()
        # for data in data_sensor: 
        #         self.listContainer1.setFont(font)
        #         self.listContainer1.addItem(''.join(data))
        
        self.listContainer1.itemActivated.connect(self.selectedItem)

        # Container Page - Log Field
        self.logs = QtWidgets.QTextEdit(self.containerPage)
        self.logs.setGeometry(QtCore.QRect(220, 90, 991, 611))
        self.logs.setFontPointSize(14)
        self.logs.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.logs.setObjectName("logs")
        

        # Container Page - Start Button
        self.startButton = QtWidgets.QToolButton(self.containerPage)
        self.startButton.setGeometry(QtCore.QRect(220, 10, 91, 71))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setText("Start")
        self.startButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0;")
        self.startButton.setStyleSheet("QToolButton:hover"
                                        "{"
                                        "background-color : lightblue;"
                                        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/icon/play-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startButton.setIcon(icon1)
        self.startButton.setIconSize(QtCore.QSize(32, 32))
        self.startButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.startButton.clicked.connect(self.startSensor)
        self.startButton.setObjectName("startButton")

        # Container Page - Stop Button
        self.stopButton = QtWidgets.QToolButton(self.containerPage)
        self.stopButton.setGeometry(QtCore.QRect(320, 10, 91, 71))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.stopButton.setFont(font)
        self.stopButton.setText("Stop")
        self.stopButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0;")
        self.stopButton.setStyleSheet("QToolButton:hover"
                                        "{"
                                        "background-color : lightblue;"
                                        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("assets/icon/stop-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon2)
        self.stopButton.setIconSize(QtCore.QSize(32, 32))
        self.stopButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.stopButton.clicked.connect(self.stopSensor)
        self.stopButton.setObjectName("stopButton")

        # Container Page - Delete Button
        self.deleteButton = QtWidgets.QToolButton(self.containerPage)
        self.deleteButton.setGeometry(QtCore.QRect(420, 10, 91, 71))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.deleteButton.setFont(font)
        self.deleteButton.setText("Delete")
        self.deleteButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0;")
        self.deleteButton.setStyleSheet("QToolButton:hover"
                                        "{"
                                        "background-color : lightblue;"
                                        "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("assets/icon/trash-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon3)
        self.deleteButton.setIconSize(QtCore.QSize(32, 32))
        self.deleteButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.deleteButton.clicked.connect(self.deleteSensor)
        self.deleteButton.setObjectName("deleteButton")

        # Container Page - Info Button
        self.infoButton = QtWidgets.QToolButton(self.containerPage)
        self.infoButton.setGeometry(QtCore.QRect(520, 10, 91, 71))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.infoButton.setFont(font)
        self.infoButton.setText("Info")
        self.infoButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0;")
        self.infoButton.setStyleSheet("QToolButton:hover"
                                        "{"
                                        "background-color : lightblue; "
                                        "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/icon/info-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoButton.setIcon(icon4)
        self.infoButton.setIconSize(QtCore.QSize(32, 32))
        self.infoButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.infoButton.setObjectName("infoButton")
        self.infoButton.clicked.connect(self.getInfoSensor)
        self.stackedWidget.addWidget(self.containerPage)

        # Container Page - Refresh Button
        self.refreshButton = QtWidgets.QToolButton(self.containerPage)
        self.refreshButton.setGeometry(QtCore.QRect(620, 10, 91, 71))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.refreshButton.setFont(font)
        self.refreshButton.setText("Refresh")
        self.refreshButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 0;")
        self.refreshButton.setStyleSheet("QToolButton:hover"
                                        "{"
                                        "background-color : lightblue; "
                                        "}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("assets/icon/refresh-52.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshButton.setIcon(icon4)
        self.refreshButton.setIconSize(QtCore.QSize(32, 32))
        self.refreshButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.clicked.connect(self.refreshPage)
        self.stackedWidget.addWidget(self.containerPage)


        # Monitoring Page 
        self.monitorinPage = QtWidgets.QWidget()
        self.monitorinPage.setObjectName("monitorinPage")

        # Monitoring Page - List Container
        self.listWidget_2 = QtWidgets.QListWidget(self.monitorinPage)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 20, 201, 681))
        self.listWidget_2.setObjectName("listWidget_2")
        self.loadDataMonitoringPage()
        # font = QtGui.QFont()
        # font.setFamily("FontAwesome")
        # font.setPointSize(16)

        # query_data = db_connection.cursor()
        # query_data.execute("SELECT deviceName FROM tb_sensor_env")
        # data_sensor = query_data.fetchall()
        # for data in data_sensor: 
        #         self.listWidget_2.setFont(font)
        #         self.listWidget_2.addItem(''.join(data))
        
        self.listWidget_2.itemActivated.connect(self.getLogsDocker)

        # Monitoring Page - Monitoring Label
        self.monitoringLabel = QtWidgets.QLabel(self.monitorinPage)
        self.monitoringLabel.setGeometry(QtCore.QRect(220, 10, 131, 61))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(48)
        self.monitoringLabel.setFont(font)
        self.monitoringLabel.setText("Logs")
        self.monitoringLabel.setObjectName("monitoringLabel")

        # Monitoring Page - Log Sensor
        self.logsSensor = QtWidgets.QTextEdit(self.monitorinPage)
        self.logsSensor.setGeometry(QtCore.QRect(220, 80, 991, 621))
        self.logsSensor.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.logsSensor.setObjectName("logsSensor")
        self.stackedWidget.addWidget(self.monitorinPage)

        # Add Sensor Page
        self.addSensorPage = QtWidgets.QWidget()
        self.addSensorPage.setObjectName("addSensorPage")

        # Add Sensor Page - Form Frame
        self.frame = QtWidgets.QFrame(self.addSensorPage)
        self.frame.setGeometry(QtCore.QRect(360, 10, 451, 681))
        self.frame.setStyleSheet("background-color: rgb(71, 206, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Add Sensor Page - Form Frame - Device ID Field
        self.deviceIDLabel = QtWidgets.QLabel(self.frame)
        self.deviceIDLabel.setGeometry(QtCore.QRect(40, 90, 61, 16))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.deviceIDLabel.setFont(font)
        self.deviceIDLabel.setObjectName("deviceIDLabel")
        self.deviceIDLineEdit = QtWidgets.QLineEdit(self.frame)
        self.deviceIDLineEdit.setGeometry(QtCore.QRect(40, 110, 371, 31))
        self.deviceIDLineEdit.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.deviceIDLineEdit.setObjectName("deviceIDLineEdit")

        # Add Sensor Page - Form Frame - Device Name Field
        self.deviceNameLabel = QtWidgets.QLabel(self.frame)
        self.deviceNameLabel.setGeometry(QtCore.QRect(40, 150, 91, 16))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.deviceNameLabel.setFont(font)
        self.deviceNameLabel.setObjectName("deviceNameLabel")
        self.deviceNameLideEdit = QtWidgets.QLineEdit(self.frame)
        self.deviceNameLideEdit.setGeometry(QtCore.QRect(40, 170, 371, 31))
        self.deviceNameLideEdit.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.deviceNameLideEdit.setObjectName("deviceNameLideEdit")

        # Add Sensor Page - Form Frame - Company Field
        self.companyLabel = QtWidgets.QLabel(self.frame)
        self.companyLabel.setGeometry(QtCore.QRect(40, 210, 61, 16))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.companyLabel.setFont(font)
        self.companyLabel.setObjectName("companyLabel")
        self.companyLineEdit = QtWidgets.QLineEdit(self.frame)
        self.companyLineEdit.setGeometry(QtCore.QRect(40, 230, 371, 31))
        self.companyLineEdit.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.companyLineEdit.setObjectName("companyLineEdit")

        # Add Sensor Page - Form Frame - Network Interface
        self.networkInterfaceLabel = QtWidgets.QLabel(self.frame)
        self.networkInterfaceLabel.setGeometry(QtCore.QRect(40, 270, 121, 16))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.networkInterfaceLabel.setFont(font)
        self.networkInterfaceLabel.setObjectName("networkInterfaceLabel")
        self.networkInterfaceComboBox = QtWidgets.QComboBox(self.frame)
        self.networkInterfaceComboBox.setGeometry(QtCore.QRect(40, 290, 371, 31))
        self.networkInterfaceComboBox.setStyleSheet("background-color: rgb(227, 227, 227); color: rgb(0, 0, 0);")
        self.networkInterfaceComboBox.setFont(font)
        self.networkInterfaceComboBox.addItem("enp0s3")
        self.networkInterfaceComboBox.addItem("eth0")
        self.networkInterfaceComboBox.setObjectName("networkInterfaceComboBox")

        # Add Sensor Page - Form Frame - Protected Subnet
        self.protectedSubnetLabel = QtWidgets.QLabel(self.frame)
        self.protectedSubnetLabel.setGeometry(QtCore.QRect(40, 330, 121, 16))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.protectedSubnetLabel.setFont(font)
        self.protectedSubnetLabel.setObjectName("protectedSubnetLabel")
        self.protectedSubnetLineEdit = QtWidgets.QLineEdit(self.frame)
        self.protectedSubnetLineEdit.setGeometry(QtCore.QRect(40, 350, 371, 31))
        self.protectedSubnetLineEdit.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.protectedSubnetLineEdit.setObjectName("protectedSubnetLineEdit")

        # Add Sensor Page - Form Frame - External Subnet
        self.externalSubnetLabel = QtWidgets.QLabel(self.frame)
        self.externalSubnetLabel.setGeometry(QtCore.QRect(40, 390, 121, 16))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.externalSubnetLabel.setFont(font)
        self.externalSubnetLabel.setObjectName("externalSubnetLabel")
        self.externalSubnetLineEdit = QtWidgets.QLineEdit(self.frame)
        self.externalSubnetLineEdit.setGeometry(QtCore.QRect(40, 410, 371, 31))
        self.externalSubnetLineEdit.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.externalSubnetLineEdit.setObjectName("externalSubnetLineEdit")

        # Add Sensor Page - Form Frame - MQTT Topic
        self.mqttTopicLabel = QtWidgets.QLabel(self.frame)
        self.mqttTopicLabel.setGeometry(QtCore.QRect(40, 450, 121, 16))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.mqttTopicLabel.setFont(font)
        self.mqttTopicLabel.setObjectName("mqttTopicLabel")
        self.mqttTopicLineEdit = QtWidgets.QLineEdit(self.frame)
        self.mqttTopicLineEdit.setGeometry(QtCore.QRect(40, 470, 371, 31))
        self.mqttTopicLineEdit.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.mqttTopicLineEdit.setObjectName("mqttTopicLineEdit")

        # Add Sensor Page - Form Frame - MQTT IP
        self.mqttIPLabel = QtWidgets.QLabel(self.frame)
        self.mqttIPLabel.setGeometry(QtCore.QRect(40, 510, 151, 16))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.mqttIPLabel.setFont(font)
        self.mqttIPLabel.setObjectName("mqttIPLabel")
        self.mqttIPLineEdit = QtWidgets.QLineEdit(self.frame)
        self.mqttIPLineEdit.setGeometry(QtCore.QRect(40, 530, 371, 31))
        self.mqttIPLineEdit.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.mqttIPLineEdit.setObjectName("mqttIPLineEdit")

        # Add Sensor Page - Form Frame - MQTT Port
        self.mqttPortLabel = QtWidgets.QLabel(self.frame)
        self.mqttPortLabel.setGeometry(QtCore.QRect(40, 570, 171, 16))
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.mqttPortLabel.setFont(font)
        self.mqttPortLabel.setObjectName("mqttPortLabel")
        self.mqttPortLineEdit = QtWidgets.QLineEdit(self.frame)
        self.mqttPortLineEdit.setGeometry(QtCore.QRect(40, 590, 371, 31))
        self.mqttPortLineEdit.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.mqttPortLineEdit.setObjectName("mqttPortLineEdit")

        # Add Sensor Page - Form Frame - Create Sensor Button
        self.createSensorButton = QtWidgets.QPushButton(self.frame)
        self.createSensorButton.setGeometry(QtCore.QRect(40, 640, 84, 30))
        self.createSensorButton.setStyleSheet("background-color: rgb(227, 227 227);")
        self.createSensorButton.setObjectName("createSensorButton")
        self.createSensorButton.clicked.connect(self.createDataSensor)

        # Add Sensor Page - Form Frame - Mata Elang Logo
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(200, 20, 51, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("assets/icon/mata elang 52-02.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.addSensorPage)

        # Toolbar Frame
        self.toolbarFrame = QtWidgets.QFrame(self.centralwidget)
        self.toolbarFrame.setGeometry(QtCore.QRect(0, 0, 151, 701))
        self.toolbarFrame.setStyleSheet("background-color: rgb(71, 206, 255);\n"
"\n"
"")
        self.toolbarFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toolbarFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.toolbarFrame.setObjectName("toolbarFrame")

        # Toolbar Frame - Layout Button
        self.verticalLayoutWidget = QtWidgets.QWidget(self.toolbarFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 151, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.buttonGroupMenu = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.buttonGroupMenu.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.buttonGroupMenu.setContentsMargins(0, 0, 0, 0)
        self.buttonGroupMenu.setSpacing(0)
        self.buttonGroupMenu.setObjectName("buttonGroupMenu")

        # Toolbar Frame - Dashboard Button
        self.dashboardButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.dashboardButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dashboardButton.sizePolicy().hasHeightForWidth())
        self.dashboardButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.dashboardButton.setFont(font)
        self.dashboardButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.dashboardButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.dashboardButton.setStyleSheet("background-color: rgb(71, 206, 255);\n"
"border: 0;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("assets/icon/dashboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dashboardButton.setIcon(icon5)
        self.dashboardButton.setIconSize(QtCore.QSize(52, 52))
        self.dashboardButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.dashboardButton.setAutoRaise(False)
        self.dashboardButton.setObjectName("dashboardButton")
        self.dashboardButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.buttonGroupMenu.addWidget(self.dashboardButton)

        # Toobar Frame - Containers Button
        self.containersButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.containersButton.sizePolicy().hasHeightForWidth())
        self.containersButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.containersButton.setFont(font)
        self.containersButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.containersButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.containersButton.setStyleSheet("background-color: rgb(71, 206, 255);\n"
"border: 0;\n"
"")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("assets/icon/list.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.containersButton.setIcon(icon6)
        self.containersButton.setIconSize(QtCore.QSize(52, 52))
        self.containersButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.containersButton.setObjectName("containersButton")
        self.containersButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.buttonGroupMenu.addWidget(self.containersButton)

        

        # Toolbar Frame - Monitoring Button
        self.monitoringButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.monitoringButton.sizePolicy().hasHeightForWidth())
        self.monitoringButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.monitoringButton.setFont(font)
        self.monitoringButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.monitoringButton.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.monitoringButton.setStyleSheet("background-color: rgb(71, 206, 255);\n"
"border: 0;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("assets/icon/computer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.monitoringButton.setIcon(icon7)
        self.monitoringButton.setIconSize(QtCore.QSize(52, 52))
        self.monitoringButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.monitoringButton.setObjectName("monitoringButton")
        self.monitoringButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(2))
        self.buttonGroupMenu.addWidget(self.monitoringButton)

        # Toolbar Frame - Logout Button
        self.logoutButton = QtWidgets.QToolButton(self.toolbarFrame)
        self.logoutButton.setGeometry(QtCore.QRect(1, 630, 151, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoutButton.sizePolicy().hasHeightForWidth())
        self.logoutButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(12)
        self.logoutButton.setFont(font)
        self.logoutButton.setStyleSheet("background-color: rgb(71, 206, 255);\n"
"border: 0;")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("assets/icon/icons8-logout-rounded-left-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutButton.setIcon(icon8)
        self.logoutButton.setIconSize(QtCore.QSize(32, 32))
        self.logoutButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.logoutButton.clicked.connect(self.logout)
        self.logoutButton.setObjectName("logoutButton")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Docker Management"))
        self.headerDashboardLabel.setText(_translate("MainWindow", "Sensor List"))
        self.toolButton_6.setText(_translate("MainWindow", "Add Sensor"))
        self.refreshButtonDashboard.setText(_translate("MainWindow", "Refresh"))
        self.deviceIDLabel.setText(_translate("MainWindow", "Device ID"))
        self.deviceNameLabel.setText(_translate("MainWindow", "Device Name"))
        self.companyLabel.setText(_translate("MainWindow", "Company"))
        self.networkInterfaceLabel.setText(_translate("MainWindow", "Network Interface"))
        self.protectedSubnetLabel.setText(_translate("MainWindow", "Protected Subnet"))
        self.externalSubnetLabel.setText(_translate("MainWindow", "External Subnet"))
        self.mqttTopicLabel.setText(_translate("MainWindow", "MQTT Topic"))
        self.mqttIPLabel.setText(_translate("MainWindow", "MQTT (MQTT Broker) IP"))
        self.mqttPortLabel.setText(_translate("MainWindow", "MQTT (MQTT Broker) Port"))
        self.createSensorButton.setText(_translate("MainWindow", "Create Sensor"))
        self.dashboardButton.setText(_translate("MainWindow", "Dashboard"))
        self.containersButton.setText(_translate("MainWindow", "Containers"))
        self.monitoringButton.setText(_translate("MainWindow", "Monitoring")) 
        self.logoutButton.setText(_translate("MainWindow", "Logout"))


    def selectedItem(self, item):
        global selectedIP
        global nameDevice
        
        nameDevice = item.text()

        query_data = db_connection.cursor()
        sql_statement = '''SELECT mqttIP FROM tb_sensor_env WHERE deviceName='{0}' '''.format(nameDevice)
        data = query_data.execute(sql_statement)
        result = query_data.fetchall()
        for x in result:
                selectedIP = x[0]
        try:
                hosts_file = open("/home/taufiq/Documents/DATA/docker-management/ansible/hosts.ini","w+")
                hosts_file.write(selectedIP)
                hosts_file.close()
                QMessageBox.information(QMessageBox(),'Successful','Sensor Selected')
                self.logs.setText("")
                print(selectedIP)
        except Exception as e:
                QMessageBox.warning(QMessageBox(), 'Error', 'Sensor Could Not Selected')
                print(str(e))
        
    
    def getInfoSensor(self):
        os.chdir("/home/taufiq/Documents/DATA/docker-management/ansible")

        cmd = "ansible-playbook playbook-container-info.yml -i hosts.ini"
        proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE).communicate()
        info_container = open("/home/taufiq/Documents/DATA/docker-management/output/info-sensor/"+selectedIP)
        data = json.loads(info_container.read())

        IDContainer = data['container']['Id']
        statusContainer = data['container']['State']['Status']
        sensorName = data['container']['Name']
        baseImage = data['container']['Config']['Image']
        startedContainer = data['container']['State']['StartedAt']
        networkMode = data['container']['HostConfig']['NetworkMode']

        self.logs.setText("")
        self.logs.append("Device Name : "+nameDevice)
        self.logs.append("IP Address : "+selectedIP)
        self.logs.append("\n")

        self.logs.append("ID Container : "+IDContainer)
        self.logs.append("Container Status : "+statusContainer)
        self.logs.append("Name Sensor : "+sensorName)
        self.logs.append("Base Image : "+baseImage)
        self.logs.append("Started At : "+startedContainer)
        self.logs.append("Network Mode : "+networkMode)
        os.chdir("/home/taufiq/Documents/DATA/docker-management")
        

    def getLogsDocker(self, item):
        nameDevice = item.text()
        self.logsSensor.setText("")

        query_data = db_connection.cursor()
        sql_statement = '''SELECT mqttIP FROM tb_sensor_env WHERE deviceName='{0}' '''.format(nameDevice)
        data = query_data.execute(sql_statement)
        result = query_data.fetchall()
        for x in result:
                selectedIP = x[0]

        try:
                hosts_file = open("./ansible/hosts.ini","w+")
                hosts_file.write(selectedIP)
                hosts_file.close()
                os.chdir("/home/taufiq/Documents/DATA/docker-management/ansible")
                self.logsSensor.setText("")
                cmd = "/usr/bin/ansible-playbook playbook-logs-container.yml -i hosts.ini"
                proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE).communicate()
                log_container = open("/home/taufiq/Documents/DATA/docker-management/output/log-sensor/"+selectedIP)
                data = json.loads(log_container.read())
                self.logsSensor.append(data['stderr']+data['stdout'])
        except Exception as e:
                QMessageBox.warning(QMessageBox(), 'Error', 'Sensor Could Not Selected')
                print(str(e))

        os.chdir("/home/taufiq/Documents/DATA/docker-management")

    def startSensor(self):
        os.chdir("/home/taufiq/Documents/DATA/docker-management")
        os.chdir("/home/taufiq/Documents/DATA/docker-management/ansible") 

        cmd = "/usr/bin/ansible-playbook playbook-community-installer.yml --tags 'Running container' -i hosts.ini"
        process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
        self.logs.setText("")
        while True:
                output = process.stdout.readline()
                if process.poll() is not None:
                        break
                if output:
                        self.logs.append(output.strip().decode('utf-8'))
        rc = process.poll()

        os.chdir("/home/taufiq/Documents/DATA/docker-management")
        self.logs.append("Sensor Successfully Started")
        self.loadData()

    def stopSensor(self):
        os.chdir("/home/taufiq/Documents/DATA/docker-management")
        os.chdir("/home/taufiq/Documents/DATA/docker-management/ansible")

        cmd = "/usr/bin/ansible-playbook playbook-manage-container.yml --tags 'Stop Container' -i hosts.ini"
        process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
        self.logs.setText("")
        while True:
                output = process.stdout.readline()
                if process.poll() is not None:
                        break
                if output:
                        self.logs.append(output.strip().decode('utf-8'))
        rc = process.poll()

        self.logs.append("Sensor Successfully Stopped")
        self.loadData()

    def deleteSensor(self):
        os.chdir("/home/taufiq/Documents/DATA/docker-management")
        os.chdir("/home/taufiq/Documents/DATA/docker-management/ansible")

        cmd = "/usr/bin/ansible-playbook playbook-manage-container.yml -i hosts.ini"
        process = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
        self.logs.setText("")
        while True:
                output = process.stdout.readline()
                if process.poll() is not None:
                        break
                if output:
                        self.logs.append(output.strip().decode('utf-8'))
        rc = process.poll()
        query_data = db_connection.cursor()
        query_data.execute(
                '''DELETE FROM tb_sensor_env WHERE mqttIP='{0}' '''.format(selectedIP)
        )
        db_connection.commit()

        self.logs.append("Sensor Successfully Deleted")
        self.loadData()
        self.loadDataContainerPage()
        self.loadDataMonitoringPage()

    def createDataSensor(self):
        #Pilih IP
        list_host = []
        with open("list-host.txt") as f:    
            for line in f:
                line = line.strip()
                list_host.append(line)
        
        self.host = QtWidgets.QLineEdit(self.addSensorPage)
        self.host.move(130,22)

        host, ok = QInputDialog.getItem(self.addSensorPage, "Select Available IP", "List of IP", list_host, 0, False)
	
        if ok and host:
            self.host.setText(str(host))
        
        # Input IP kedalam variable hosts
        host = self.host.text()

        # Buat Inventory File untuk Hosts
        hosts_file = open("./ansible/hosts.ini","w+")
        hosts_file.write(host)
        hosts_file.close()

        deviceID = self.deviceIDLineEdit.text()
        deviceName = self.deviceNameLideEdit.text()
        company = self.companyLineEdit.text()
        networkInterface = str(self.networkInterfaceComboBox.currentText())
        protectedSubnet = self.protectedSubnetLineEdit.text()
        externalSubnet = self.externalSubnetLineEdit.text()
        mqttTopic = self.mqttTopicLineEdit.text()
        mqttIP = self.mqttIPLineEdit.text()
        mqttPort = self.mqttPortLineEdit.text()
        
        
        #Tambahkan data ke dalam database 
        db = db_connection.cursor()
        db.execute("INSERT INTO tb_sensor_env (protectedSubnet, externalSubnet, mqttTopic, mqttIP, mqttPort, deviceID, deviceName, networkInterface, company) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (protectedSubnet, externalSubnet, mqttTopic, mqttIP, mqttPort, deviceID, deviceName, networkInterface, company))

        db_connection.commit()
        
        #Tambah file .env ke /var/tmp/sensor_environment untuk di copy ke remote host
        path_env_checking = os.path.isdir("/var/tmp/sensor_environment")
        output_env_path = str(path_env_checking)
        if output_env_path == "False":
            os.makedirs("/var/tmp/sensor_environment")
        else:
            print("/var/tmp/sensor_environment folder exists")
                
        env_sensor_file = open("/var/tmp/sensor_environment/sensor.env","w+")
        env_sensor_file.write(
            'PROTECTED_SUBNET={0}\nEXTERNAL_SUBNET={1}\nALERT_MQTT_TOPIC={2}\nALERT_MQTT_SERVER={3}\nALERT_MQTT_PORT={4}\nDEVICE_ID={5}\nNETINT={6}\nCOMPANY={7}\n'
            .format(protectedSubnet, externalSubnet, mqttTopic, mqttIP, mqttPort, deviceID, networkInterface, company)
        )
        env_sensor_file.close()

        try:
                self.installSensor()
        except Exception:
                print(e)

    def installSensor(self):
        os.chdir("/home/taufiq/Documents/DATA/docker-management/ansible")
        os.system("/usr/bin/ansible-playbook playbook-install-mqtt.yml -i hosts.ini ")
        os.system("/usr/bin/ansible-playbook playbook-install-docker.yml playbook-community-installer.yml -i hosts.ini ")
        os.chdir("/home/taufiq/Documents/DATA/docker-management")
        self.loadData()
        self.loadDataContainerPage()
        self.loadDataMonitoringPage()

    def refreshPage(self):
        self.logs.setText("")
    
    def loadData(self):
        # Dashboard Page - Sensor List Table - Query untuk menampilkan data sensor
        db = db_connection.cursor()
        db.execute("SELECT deviceID, deviceName, protectedSubnet, mqttIP, company FROM tb_sensor_env")
        data_sensor = db.fetchall()
        self.sensorListTable.setRowCount(0)
        for row_number, row_data in enumerate(data_sensor):
            self.sensorListTable.insertRow(row_number)
            for colum_number, data in enumerate(row_data):
                self.sensorListTable.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

    def loadDataContainerPage(self):
        self.listContainer1.clear()
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(16)
        
        query_data = db_connection.cursor()
        query_data.execute("SELECT deviceName FROM tb_sensor_env")
        data_sensor = query_data.fetchall()
        for data in data_sensor: 
                self.listContainer1.setFont(font)
                self.listContainer1.addItem(''.join(data))    

    def loadDataMonitoringPage(self):
        self.listWidget_2.clear()
        font = QtGui.QFont()
        font.setFamily("FontAwesome")
        font.setPointSize(16)

        query_data = db_connection.cursor()
        query_data.execute("SELECT deviceName FROM tb_sensor_env")
        data_sensor = query_data.fetchall()
        for data in data_sensor: 
                self.listWidget_2.setFont(font)
                self.listWidget_2.addItem(''.join(data))   

    def logout(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setup(self.window)
        self.window.show()
        MainWindow.hide()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
