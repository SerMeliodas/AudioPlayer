import os
from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtCore import Signal, Qt, QRect
from pygame import mixer
from pathlib import Path

class PlayList(QListWidget):

    fileDropped = Signal(list)

    def __init__(self, parent= None) -> None:
        super().__init__(parent)
        self.setAcceptDrops(True)
        self._currentSong = None
        self._directory = str()
        self.fileDropped.connect(self._musicOpen)
        self.itemDoubleClicked.connect(self.playMusic)
    
    def _musicOpen(self, files):
        # if play list is not empty
        if self.count() != 0:
            self.clear()
        # if was dropped folder instead of files array
        if len(files) == 1 and Path(files[0]).is_dir():
            self._directory = Path(files[0])
            for file in Path(files[0]).iterdir():
                QListWidgetItem(Path(file).name, self)
        # if was dropped files array
        else:        
            self._directory = Path(files[0]).parent
            for file in files:
                if Path(file).exists():
                    QListWidgetItem(Path(file).name, self)

    def playMusic(self, music):
        mixer.music.load(f"{self._directory}\{music.text()}")
        mixer.music.play()
        self._currentSong = music


    def stopMusic(self):
        mixer.music.stop()
        mixer.music.unload()

    def pauseMusic(self):
        mixer.music.pause()

    def unpauseMusic(self):
        mixer.music.unpause()

    def getCurrentSong(self) -> QListWidgetItem:
        return self._currentSong
    
    def getDirectory(self) -> str:
        return self._directory

    def getSongPath(self) -> str:
        return f"{self._directory}\{self._currentSong.text()}"

    def setCurrentSong(self, currentSong):
        self._currentSong = currentSong

    def setFolder(self, folder) -> None:
        self._directory = folder

    def dragEnterEvent(self, event) -> None:
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()
    
    def dragMoveEvent(self, event) -> None:
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()
    
    def dropEvent(self, event) -> None:
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            links = list()
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            self.setFolder(Path(links[0]).parent)
            self.fileDropped.emit(links)
        else:
            event.ignore()
        

