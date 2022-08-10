from PySide6.QtWidgets import QSlider
from PySide6.QtCore import Qt, QTimer

from pygame import mixer


class ProgressBar(QSlider):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setOrientation(Qt.Horizontal)
        self._songLength = 0
        self._songOfset = 0
        self._timer = QTimer()
        self._timer.timeout.connect(self.update)
        
        self.setRange(0,0)

        self.sliderPressed.connect(self.onPressed)
        self.sliderReleased.connect(self.onRelease)

    def getSongLength(self):
        return self._songLength
    
    def setSongLength(self, length):
        self._songLength = length
        self.setMaximum(length)

    def getTimer(self):
        return self._timer

    def update(self):
        self.setValue(mixer.music.get_pos()/1000)
        if self.sliderPosition() == self._songLength:
            mixer.music.stop()
            mixer.music.unload()
   
    def onPressed(self):
        self._timer.stop()
    
    def onRelease(self):
        mixer.music.play(start=self.sliderPosition())
        self._timer.start()