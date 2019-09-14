import os, sys, subprocess
from PyQt5 import *
from PyQt5.QtCore import * 
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui

class QButton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        # create objects
        self.name='me'
        label = QLabel(self.tr("Enter command and press Return"))
        self.le = QLineEdit()
        self.te = QTextEdit()
        self.button = QtGui.QPushButton('Button', self)
        # layout
        layout = QVBoxLayout(self)
        layout.addWidget(label)
        layout.addWidget(self.le)
        layout.addWidget(self.button)
        layout.addWidget(self.te)
        self.setLayout(layout) 
        # create connection
        self.button.clicked.connect(self.calluser)
        self.connect(self.le, SIGNAL("returnPressed(void)"), self.run_command)
    def calluser(self):
        print(self.name)
        filetoinclude.dadada()

    def run_command(self):
        cmd = str(self.le.text())
        result = self.system_call(cmd)
        self.te.setText(result)

    def system_call(self, command):
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        return p.stdout.read()

def demo_QButton():
    app = QtGui.QApplication(sys.argv)
    tb = QButton()
    tb.show()
    app.exec_()

if __name__=='__main__':
    demo_QButton()