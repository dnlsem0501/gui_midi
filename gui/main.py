import sys
sys.setrecursionlimit(100000)

from PySide6.QtWidgets import QWidget
from PySide6.QtCore import *
from PySide6.QtGui import *

from mainwidget import * 

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    # self.setWindowTitle("LG Portable version 1.0 (LG Electronics and VizWave Inc.)")
    self.setFixedSize(QSize(1280, 720)) # removable  
    # self.setWindowIcon(QIcon("./file/LGlogo.jpg"))
    self.widget = Main()
    self.setCentralWidget(self.widget)
    self.show()

app = QApplication(sys.argv)
# app.setStyle(QStyleFactory.create("fusion"))
# customFont = QFont("Time New Roman", 9)
# # customFont.setBold(True)
# app.setFont(customFont)

window = MainWindow()  
window.show()
sys.exit(app.exec())
