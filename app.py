import sys
import os

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction

from ui import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())