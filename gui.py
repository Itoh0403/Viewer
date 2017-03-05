# coding:utf-8

import sys
import gribDraw
from PyQt5.QtWidgets import *

class Button01(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 =QPushButton("表示する", self)
        btn2 =QPushButton("閉じる", self)
        btn2.move(0,20)
        btn1.clicked.connect(self.button01Clicked)
        btn2.clicked.connect(self.button02Clicked)

        self.statusBar()

        self.resize(400, 300)
        self.setWindowTitle('Button01')
        self.show()

    def button01Clicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' Push Button01')
        grbs = gribDraw.openGrib('Z__C_RJTD_20170211000000_GSM_GPV_Rgl_FD0000_grib2.bin')
        gribDraw.displayContour(grbs, 3, 35, 40, 137, 142)

    def button02Clicked(self):
        gribDraw.closeWindow()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Button01()
    sys.exit(app.exec_())
