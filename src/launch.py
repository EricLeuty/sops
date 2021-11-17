import sys
import os

from PyQt5.QtCore import QUrl
import PyQt5.QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from mediaViewer import *








def main():
    app = QtWidgets.QApplication([])
    widget = QtWidgets.QMainWindow()
    widget.showFullScreen()
    app.exec_()

if __name__ == '__main__':
    main()


