import os
from pathlib import PurePath
from typing import Container
from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QGridLayout,QMainWindow,QPushButton, QWidget

from ui.playList import PlayList
from ui.menuBar import MenuBar

class MainWindow(QMainWindow):
    def __init__(self, parent= None) -> None:
        super().__init__(parent)
        self.setWindowTitle("MainWindow")
        self.setWindowIcon(QIcon("./icons/windowIcon.svg"))
        self.resize(1000,600)

        self.container = QWidget(self)
        self.setCentralWidget(self.container)
        self.container.setObjectName(u"container")

        self.menuBar = MenuBar()
        self.setMenuBar(self.menuBar)

        self.gridLayoutWidget = QWidget(self.container)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayout = QGridLayout(self.container)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        
        self.container.setLayout(self.gridLayout)
        
        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setText(u"play/stop")
        self.gridLayout.addWidget(self.pushButton)

        self.playListWidget = PlayList(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.playListWidget)

