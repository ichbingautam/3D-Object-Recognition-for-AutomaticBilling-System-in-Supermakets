# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SecondMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import store_images
import data_fetch
class Ui_SecondMainWindow(object):

    def setupUi(self, SecondMainWindow):
        SecondMainWindow.setObjectName("SecondMainWindow")
        SecondMainWindow.resize(622, 648)
        self.centralwidget = QtWidgets.QWidget(SecondMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(260, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.detectButton = QtWidgets.QPushButton(self.centralwidget)
        self.detectButton.setGeometry(QtCore.QRect(260, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.detectButton.setFont(font)
        self.detectButton.setObjectName("detectButton")
        self.resultButton = QtWidgets.QPushButton(self.centralwidget)
        self.resultButton.setGeometry(QtCore.QRect(260, 350, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.resultButton.setFont(font)
        self.resultButton.setObjectName("resultButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lb = QtWidgets.QLabel(self.centralwidget)
        self.lb.setGeometry(QtCore.QRect(120, 440, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb.setFont(font)
        self.lb.setObjectName("lb")
        self.lb2 = QtWidgets.QLabel(self.centralwidget)
        self.lb2.setGeometry(QtCore.QRect(250, 440, 271, 16))
        self.lb2.setText("")
        self.lb2.setObjectName("lb2")
        SecondMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 622, 21))
        self.menubar.setObjectName("menubar")
        SecondMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondMainWindow)
        self.statusbar.setObjectName("statusbar")
        SecondMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondMainWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondMainWindow)

    def retranslateUi(self, SecondMainWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondMainWindow.setWindowTitle(_translate("SecondMainWindow", "MainWindow"))
        self.startButton.setText(_translate("SecondMainWindow", "Start"))
        self.detectButton.setText(_translate("SecondMainWindow", "Recognize"))
        self.resultButton.setText(_translate("SecondMainWindow", "Result"))
        self.label.setText(_translate("SecondMainWindow", "Object Detection of Automatic Billing System"))
        self.lb.setText(_translate("SecondMainWindow", "Detected Object:"))
        ######################### Button Event ##################
        self.startButton.clicked.connect(self.run_camera)
        self.resultButton.clicked.connect(self.fetch_data)
      #  self.detectButton.clicked.connect(self.run_model)
        #########################################################


    def run_camera(self):
        store_images.main()
        

    def fetch_data(self):
        data_fetch.main()

    # def run_model(self):
    #     model.main()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondMainWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondMainWindow()
    ui.setupUi(SecondMainWindow)
    SecondMainWindow.show()
    sys.exit(app.exec_())

