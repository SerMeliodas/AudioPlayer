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
        self.folder = str()
        self.fileDropped.connect(self.musicOpen)
        self.itemDoubleClicked.connect(self.playMusicOnItemDoubleclick)
    
    def musicOpen(self, files):
        #if play list is not empty
        if self.count() != 0:
            self.clear()
        #if was dropped folder instead of array of files
        if len(files) == 1 and Path(files[0]).is_dir():
            self.folder = Path(files[0])
            for file in Path(files[0]).iterdir():
                QListWidgetItem(Path(file).name, self)
        #if was dropped array of files
        else:        
            self.folder = Path(files[0]).parent
            for file in files:
                if Path(file).exists():
                    QListWidgetItem(Path(file).name, self)

    def playMusicOnItemDoubleclick(self, music):
        mixer.music.load(f"{self.folder}\{music.text()}")
        mixer.music.play()

    def getFolder(self) -> str:
        return self.folder
    
    def setFolder(self, folder) -> None:
        self.folder = folder

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
            self.folder = Path(links[0]).parent
            self.fileDropped.emit(links)
        else:
            event.ignore()
        

