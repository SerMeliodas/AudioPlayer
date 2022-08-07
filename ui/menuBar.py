from signal import Signals
from typing import Sequence
from PySide6.QtWidgets import QMenuBar, QMenu, QFileDialog, QListWidgetItem
from PySide6.QtGui import QAction
from PySide6.QtCore import QUrl, Signal

from pathlib import Path

class MenuBar(QMenuBar):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setNativeMenuBar(True)
        
        self.actionFolderOpen = QAction(self)
        self.actionFolderOpen.setText(u"Open folder")
        self.actionFolderOpen.setShortcut(u"Ctrl+F")

        self.FileMenu = QMenu(self)
        self.FileMenu.setTitle(u"File")
        

        self.addAction(self.FileMenu.menuAction())
        self.FileMenu.addAction(self.actionFolderOpen)

        self.actionFolderOpen.triggered.connect(self.openFolder)
        
    def openFolder(self):
        if self.parent().playListWidget.count() != 0:
            self.parent().playListWidget.clear()
        folder = QFileDialog.getExistingDirectory()
        self.parent().playListWidget.setFolder(folder)
        for file in Path(folder).iterdir():
            QListWidgetItem(Path(file).name, self.parent().playListWidget)
