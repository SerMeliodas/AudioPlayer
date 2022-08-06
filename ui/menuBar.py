from PySide6.QtWidgets import QMenuBar, QMenu
from PySide6.QtGui import QAction


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
        