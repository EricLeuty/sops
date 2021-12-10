from PyQt5 import QtCore, QtGui, QtWidgets
from media_viewer import *
from code_widget import *
from session import *

class CodingWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, session_name=None):
        super().__init__(parent)

        self.session = Session.load(session_name)

        self.grid_layout = QtWidgets.QGridLayout(self)

        self.media_viewer = MediaViewer(self, True)
        self.code_widget = CodeWidget(self)

        self.grid_layout.addWidget(self.media_viewer, 0, 0, 1, 1)


    def show_code_widget(self):
        time = self.media_viewer.videoGroup.player.position()
        self.code_widget.update_time(time)
        self.grid_layout.addWidget(self.code_widget, 0, 1, 1, 1)
        self.code_widget.show()

    def hide_code_widget(self):
        self.code_widget.hide()
        self.grid_layout.removeWidget(self.code_widget)


def main():
    app = QtWidgets.QApplication([])
    widget = CodingWidget(session_name="Queens_LOPUS")
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()