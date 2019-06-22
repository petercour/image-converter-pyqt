# image converter in pyqt
# https://pythonbasics.org/pyqt/

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QMessageBox, QDialog, QFileDialog
import sys
import os
import glob

class Example(QtWidgets.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('gui.ui', self)
        self.comboBox.addItem(".png")
        self.comboBox.addItem(".jpg")
        self.comboBox.addItem(".bmp")
        self.pushButtonDir.clicked.connect(self.onClick)
        self.pushButtonConvert.clicked.connect(self.onConvert)
        
    def onClick(self):
        self.thedir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print('select dir ' + self.thedir)

    def onConvert(self):
        images = glob.glob(self.thedir + "/*")
        print(images)
        for image in images:
            # no dot in filename allowed
            newImage = image[:image.index(".")] + self.comboBox.currentText()
            cmd = "convert " + image + " " + newImage
            os.system(cmd)
            
app = QtWidgets.QApplication([])
win = Example()
win.show()
sys.exit(app.exec())
