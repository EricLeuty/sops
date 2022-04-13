# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/mediaViewer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from sops_widget import SOPSWidget
from timeline_controller import *
from video_widget import *

class MediaViewer(SOPSWidget):
    def __init__(self, parent=None, show_coding_buttons=False, session=None):
        super().__init__(parent)

        if session:
            self.session = session



        self.resize(1200, 800)
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.videoGroup = VideoWidget(self)
        self.videoGroup.setObjectName("videoGroup")
        self.verticalLayout.addWidget(self.videoGroup, stretch=10)
        self.timelineController = TimelineController(self, show_coding_buttons)
        self.timelineController.setObjectName("timelineController")
        self.timelineController.setMinimumHeight(50)
        self.verticalLayout.addWidget(self.timelineController, stretch=2)


        self.duration = self.videoGroup.player.duration()
        self.playmode = 1
        self.playback_speed = 1

        self.update_media_state()

        self.videoGroup.player.durationChanged.connect(lambda x: self.set_duration(x))
        self.videoGroup.player.positionChanged.connect(lambda x: self.timelineController.update_timeline_position(x))
        self.timelineController.timelineSlider.sliderMoved.connect(lambda x: self.update_position(x))
        self.timelineController.playPause.clicked.connect(lambda x: self.update_playmode())
        self.timelineController.toStart.clicked.connect(lambda x: self.update_position(0))
        self.timelineController.toEnd.clicked.connect(lambda x: self.update_position(self.duration))
        self.timelineController.fastBackward.clicked.connect(self.fast_backward)
        self.timelineController.fastForward.clicked.connect(self.fast_forward)




    def update_playmode(self):
        if self.playmode == 1:
            self.playmode = 0
        elif self.playmode == 0 and self.playback_speed == 1.0:
            self.playmode = 1
        elif self.playmode == 0 and self.playback_speed != 1.0:
            self.playback_speed = 1.0
        self.update_media_state()

    def update_position(self, position):
        self.videoGroup.player.setPosition(position)
        self.timelineController.update_timeline_position(position)


    def fast_backward(self):
        if self.playback_speed == 1.0:
            self.playback_speed *= -1.0
        elif self.playback_speed < 0.0:
            self.playback_speed *= 2.0
        elif self.playback_speed > 1.0:
            self.playback_speed /= 2.0
        self.update_media_state()

    def fast_forward(self):
        if self.playback_speed >= 1.0:
            self.playback_speed *= 2.0
        elif self.playback_speed < -1.0:
            self.playback_speed /= 2.0
        elif self.playback_speed == -1.0:
            self.playback_speed = 1.0
        self.update_media_state()

    def set_duration(self, duration):
        self.duration = duration
        self.timelineController.set_timeline_max(self.duration)

    def update_media_state(self):
        self.videoGroup.set_playmode(self.playmode)
        self.videoGroup.set_playback_speed(self.playback_speed)





def main():
    app = QtWidgets.QApplication([])
    widget = MediaViewer()
    widget.show()

    app.exec_()

if __name__ == '__main__':
    main()
