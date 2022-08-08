from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt, QTimer

class SeekBar(QSlider):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setOrientation(Qt.Horizontal)
        self._songLength = 0
        self._timer = QTimer()
        self._timer.timeout.connect(self.update)

    def getSongLength(self):
        return self._songLength
    
    def setSongLength(self, length):
        self._songLength = length

    def update(self):
        pass