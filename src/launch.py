import sys
import os

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from mediaViewer import *








def main():
    app = QApplication([])
    widget = MediaViewer()
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()


