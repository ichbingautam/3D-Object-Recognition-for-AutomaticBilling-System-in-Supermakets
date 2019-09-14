from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
import store_images
import model
import sys

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def run_gui(self):
    	self.startButton.clicked.connect(self.run_camera)
    	self.detectButton.clicked.connect(self.run_model)
        #self.resultButton.clicked.connect(self.get_result)

    def run_camera(self):
        store_images()

    def run_model(self):
   	    model()

#def get_result(self):


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()