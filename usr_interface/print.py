import sys
import os
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication


class MyStream(QtCore.QObject):
    message = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        super(MyStream, self).__init__(parent)

    def write(self, message):
        self.message.emit(str(message))

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.pushButtonPrint = QtWidgets.QPushButton(self)
        self.pushButtonPrint.setText("Click Me!")
        self.pushButtonPrint.clicked.connect(self.on_pushButtonPrint_clicked)
        self.textEdit = QtWidgets.QTextEdit(self)
        self.layoutVertical = QtWidgets.QVBoxLayout(self)
        self.layoutVertical.addWidget(self.pushButtonPrint)
        self.layoutVertical.addWidget(self.textEdit)

    @QtCore.pyqtSlot()
    def on_pushButtonPrint_clicked(self):
        cmd = 'python D:/Object Recognition/usr_interface/test.py'
        # execute script
        output = subprocess.check_output(cmd, shell=True)
        #print(output.decode('utf-8'))
        print(output)

    @QtCore.pyqtSlot(str)
    def on_myStream_message(self, message):
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.textEdit.insertPlainText(message)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()

    myStream = MyStream()
    myStream.message.connect(main.on_myStream_message)

    sys.stdout = myStream
    sys.exit(app.exec_())