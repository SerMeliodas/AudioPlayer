import os

from pygame import mixer
from PySide6.QtCore import QCoreApplication, QDate, QDateTime, QLocale, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QGridLayout,QMainWindow,QPushButton, QWidget, QHBoxLayout

from mutagen.mp3 import MP3

from auidoPlayer.playList import PlayList
from auidoPlayer.menuBar import MenuBar
from auidoPlayer.seekBar import SeekBar 

class MainWindow(QMainWindow):
    def __init__(self, parent= None) -> None:
        super().__init__(parent)
        self.setWindowTitle("MainWindow")
        self.setWindowIcon(QIcon("./icons/windowIcon.svg"))
        self.resize(1000,600)

        self.container = QWidget(self)
        self.setCentralWidget(self.container)
        self.container.setObjectName(u"container")

        # menu bar
        self.menuBar = MenuBar(self.container)
        self.setMenuBar(self.menuBar)

        # main layout
        self.gridLayoutWidget = QWidget(self.container)
        self.gridLayout = QGridLayout(self.container)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)

        self.container.setLayout(self.gridLayout)
        
        # play list
        self.playListWidget = PlayList(self.gridLayoutWidget)
        self.gridLayout.addWidget(self.playListWidget)
        
        # control buttons
        self.controlButtonsWidget = QWidget(self.gridLayoutWidget)
        self.controlButtonsLayout = QHBoxLayout(self.gridLayoutWidget)
        self.controlButtonsWidget.setLayout(self.controlButtonsLayout)
        
        self.pushButtonPlay = QPushButton(self.controlButtonsWidget)
        self.pushButtonPlay.setText(u"play/stop")
        self.pushButtonPlay.clicked.connect(self.togglePlay)

        self.pushButtonPrev = QPushButton(self.controlButtonsWidget)
        self.pushButtonPrev.setText(u"<")
        
        self.pushButtonNext = QPushButton(self.controlButtonsWidget)
        self.pushButtonNext.setText(u">")
        
        self.controlButtonsLayout.addWidget(self.pushButtonPrev)      
        self.controlButtonsLayout.addWidget(self.pushButtonPlay)
        self.controlButtonsLayout.addWidget(self.pushButtonNext)

        # seek bar
        self.seekBar = SeekBar(self.container)       
        self.gridLayout.addWidget(self.seekBar)
    
        self.gridLayout.addWidget(self.controlButtonsWidget)

    def togglePlay(self):
        # if selected another song
        if self.playListWidget.getCurrentSong() != self.playListWidget.currentItem():
            self.playListWidget.playMusic(self.playListWidget.currentItem())
            self.seekBar.setSongLength(MP3(self.playListWidget.getSongPath()).info.length)
        # if nothing else selected just pause
        elif self.playListWidget.getCurrentSong() == self.playListWidget.currentItem() and mixer.music.get_busy():
            self.playListWidget.pauseMusic()
        # else unpause
        else:
            self.playListWidget.unpauseMusic()
