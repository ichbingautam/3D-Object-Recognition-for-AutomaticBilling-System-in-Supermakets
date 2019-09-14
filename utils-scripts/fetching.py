from PySide import QtGui, QtCore
import sys
class MyGui(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.initMenu()
        self.table = QtGui.QTableWidget(1,3)
        self.columnLabels = ["Make","Model","Price"]
        self.table.setHorizontalHeaderLabels(self.columnLabels)
        self.setCentralWidget(self.table)
        self.setGeometry(50,50,700,400)
        self.setWindowTitle("My GUI Program")
        self.show()
        
    def initMenu(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("File")
        open = QtGui.QAction("Open",self)
        open.triggered.connect(self.openFile)
        fileMenu.addAction(open)
        quit = QtGui.QAction("Quit",self)
        quit.triggered.connect(self.close)
        fileMenu.addAction(quit)
        
    def openFile(self):
        filename, _ = QtGui.QFileDialog.getOpenFileName(self,
            "Open File",".")
        if (filename != ""):
            infile = open(filename,"r")
            lines = infile.readlines()
            infile.close()

app = QtGui.QApplication(sys.argv)
mygui = MyGui()
sys.exit(app.exec_())