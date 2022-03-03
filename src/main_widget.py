from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from session import *
from codes import *
from observation import *
from home_widget import HomeWidget

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setObjectName("main_window")
        self.sessions = ["Queens_LOPUS", "session2"]
        self.codesets = ["LOPUS_student_behavior"]
        self.resize(960, 720)
        self.setCentralWidget(HomeWidget(self))


    def reset_central_widget(self):
        self.setCentralWidget(HomeWidget(self))

class App(QtWidgets.QApplication):
    def __init__(self, arr):
        super().__init__(arr)
        self.main_widget = MainWindow()
        self.main_widget.show()

def main():
    app = App([])
    app.exec_()

if __name__ == '__main__':
    main()