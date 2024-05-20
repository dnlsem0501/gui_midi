
import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from page_btns import PageBtns
from spk_pos import Spk_pos

class Main(QGroupBox):
    def __init__(self):
        super().__init__()

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.left_btns = PageBtns()
        
        self.right_pages = QStackedWidget()
        self.spk_pos_page = Spk_pos()
        self.play_page = QWidget()

        self.right_pages.addWidget(self.spk_pos_page)
        self.right_pages.addWidget(self.play_page)

        self.main_layout.addWidget(self.left_btns)
        self.main_layout.addWidget(self.right_pages)

        self.left_btns.spk_pos_btn.clicked.connect(self.spk_pos_btn_clicked)
        self.left_btns.play_btn.clicked.connect(self.play_btn_clicked)

    def spk_pos_btn_clicked(self):
        self.right_pages.setCurrentWidget(self.spk_pos_page)
    
    def play_btn_clicked(self):
        self.right_pages.setCurrentWidget(self.play_page)
