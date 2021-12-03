# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/timelineController.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget


class VideoWidget(QVideoWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent
        self.duration = 0
        self.path = QtCore.QUrl.fromLocalFile('/home/eric/PycharmProjects/sops/Sessions/LOPUS.mp4')
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self)
        self.player.setMedia(QMediaContent(self.path))
        self.player.durationChanged.connect(lambda x: self.setDuration(x))

    def setDuration(self, duration):
        self.duration = duration

    def setPosition(self, time):
        if time <= self.duration:
            self.player.setPosition(time)

    def setPlaymode(self, state):
        if state == 0:
            self.player.play()
        elif state == 1:
            self.player.pause()

    def setPlaybackSpeed(self, speed):
        self.player.setPlaybackRate(speed)


def main():
    app = QtWidgets.QApplication([])
    widget = VideoWidget()
    widget.player.play()
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()