import sys
import os
from mutagen.mp3 import MP3
from pygame import mixer

from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QTimer
from PySide6.QtGui import QAction

from ui import MainWindow