
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Spk_pos(QGroupBox):
    def __init__(self):
        super().__init__()

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.upper_options = options()

        self.bottom_poss = QStackedWidget()
        self.pos1 = spk_pos1()
        self.bottom_poss.addWidget(self.pos1)
        self.pos2 = spk_pos2()
        self.bottom_poss.addWidget(self.pos2)

        self.main_layout.addWidget(self.upper_options)
        self.main_layout.addWidget(self.bottom_poss)
        self.upper_options.poss.currentIndexChanged.connect(self.pos_combo_changed)

    def pos_combo_changed(self):
        if self.upper_options.poss.currentText() == "1":
            self.bottom_poss.setCurrentWidget(self.pos1)
        elif self.upper_options.poss.currentText() == "2":
            self.bottom_poss.setCurrentWidget(self.pos2)

class options(QGroupBox):
    def __init__(self):
        super().__init__()

        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        self.poss = QComboBox()
        self.poss.addItems(["1", "2"])
        self.poss.setFixedHeight(40)

        self.playbtn = QPushButton("Play")
        self.playbtn.setFixedSize(100,40)
        self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.main_layout.addSpacing(800)
        self.main_layout.addWidget(self.poss)
        self.main_layout.addWidget(self.playbtn)


class spk_pos1(QGroupBox):
    def __init__(self):
        super().__init__()

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.spk1 = QLabel("Speaker 1")
        pixmap = QPixmap("./file/speaker1.jpg")
        pixmap = pixmap.scaled(200, 200)
        self.spk1.setPixmap(pixmap)
        self.spk2 = QLabel("Speaker 2")
        pixmap = pixmap.scaled(200, 200)
        self.spk2.setPixmap(pixmap)
        self.spk3 = QLabel("Speaker 3")

        self.main_layout.addWidget(self.spk1, 0, 0)
        self.main_layout.addWidget(self.spk2, 0, 2)
        self.main_layout.addWidget(self.spk3, 2, 0)

class spk_pos2(QGroupBox):
    def __init__(self):
        super().__init__()

        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

        self.spk1 = QLabel("Speaker 1")
        pixmap = QPixmap("./file/speaker1.jpg")
        pixmap = pixmap.scaled(200, 200)
        self.spk1.setPixmap(pixmap)
        self.spk2 = QLabel("Speaker 2")
        pixmap = pixmap.scaled(200, 200)
        self.spk2.setPixmap(pixmap)
        self.spk3 = QLabel("Speaker 3")

        self.main_layout.addWidget(self.spk1, 2, 2)
        self.main_layout.addWidget(self.spk2, 0, 2)
        self.main_layout.addWidget(self.spk3, 2, 0)