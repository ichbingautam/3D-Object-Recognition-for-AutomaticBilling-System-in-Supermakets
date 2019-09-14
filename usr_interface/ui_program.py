from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import os, sys, subprocess, filetoinclude
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))

def :









window.setLayout(layout)
window.show()
app.exec_()