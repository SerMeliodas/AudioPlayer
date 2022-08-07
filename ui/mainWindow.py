import os

from pygame import mixer
from pathlib import PurePath
from typing import Container
from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QGridLayout,QMainWindow,QPushButton, QWidget, QHBoxLayout

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

        self.menuBar = MenuBar(self.container)
        self.setMenuBar(self.menuBar)

        self.gridLayoutWidget = QWidget(self.container)
        self.gridLayout = QGridLayout(self.container)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)

        self.container.setLayout(self.gridLayout)

        self.playListWidget = PlayList(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.playListWidget)

        self.controlButtonsWidget = QWidget(self.gridLayoutWidget)
        self.controlButtonsLayout = QHBoxLayout(self.gridLayoutWidget)
        self.controlButtonsWidget.setLayout(self.controlButtonsLayout)
        
        self.pushButtonPlay = QPushButton(self.controlButtonsWidget)
        self.pushButtonPlay.setText(u"play/stop")

        self.pushButtonPrev = QPushButton(self.controlButtonsWidget)
        self.pushButtonPrev.setText(u"<")
        
        self.pushButtonNext = QPushButton(self.controlButtonsWidget)
        self.pushButtonNext.setText(u">")
        
        self.controlButtonsLayout.addWidget(self.pushButtonPrev)      
        self.controlButtonsLayout.addWidget(self.pushButtonPlay)
        self.controlButtonsLayout.addWidget(self.pushButtonNext)

        self.gridLayout.addWidget(self.controlButtonsWidget)