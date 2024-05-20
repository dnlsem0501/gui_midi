
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class PageBtns(QGroupBox):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.btns = QButtonGroup()
        self.btns.setExclusive(True)
        
        self.spk_pos_btn = QPushButton("Speaker Position")
        self.spk_pos_btn.setFixedSize(150,100)
        self.play_btn = QPushButton("Play")
        self.play_btn.setFixedSize(150,100)
        self.btns.addButton(self.spk_pos_btn)
        self.btns.addButton(self.play_btn)
        
        self.main_layout.addWidget(self.spk_pos_btn)
        self.main_layout.addWidget(self.play_btn)
        self.main_layout.addSpacing(500)