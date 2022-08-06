import os
from PySide6.QtWidgets import QListWidget, QListWidgetItem
from PySide6.QtCore import Signal, Qt, QRect

from pathlib import Path

class PlayList(QListWidget):

    fileDropped = Signal(list)

    def __init__(self, parent= None) -> None:
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.folder = str()
        self.fileDropped.connect(self.musicOpen)
    
    def musicOpen(self, files):
        if len(files) == 1 and Path(files[0]).is_dir():
            for file in Path(files[0]).iterdir():
                QListWidgetItem(Path(file).name, self)
        else:        
            for file in files:
                if Path(file).exists():
                    QListWidgetItem(Path(file).name, self)

    def getFolder(self) -> str:
        return self.folder

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
        

