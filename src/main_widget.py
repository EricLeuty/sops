from PyQt5 import QtCore, QtGui, QtWidgets
from session import *
from code import *
from observation import *
from home_window import *

class MainWidget(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.sessions = ["Queens_LOPUS", "session2"]
        self.codesets = ["LOPUS_student_behavior"]
        self.resize(960, 720)
        self.setCentralWidget(HomeWidget(self))


def main():
    app = QtWidgets.QApplication([])
    main_widget = MainWidget()
    main_widget.show()

    app.exec_()

if __name__ == '__main__':
    main()