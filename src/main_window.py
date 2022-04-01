from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from os.path import join, isfile
from session import *
from codeset import *
from dataset import *
from home_widget import HomeWidget

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setObjectName("main_window")
        self.load_data()
        self.resize(960, 720)
        self.setCentralWidget(HomeWidget(self))

    def load_data(self):
        self.load_sessions()
        self.load_codesets()
        self.load_studentsets()

    def load_codesets(self):
        path = Path(os.getcwd()).parent / "Codesets"
        self.codesets = [f for f in os.listdir(path) if isfile(join(path, f))]

    def load_studentsets(self):
        path = Path(os.getcwd()).parent / "Studentsets"
        self.studentsets = [f for f in os.listdir(path) if isfile(join(path, f))]

    def load_sessions(self):
        path = Path(os.getcwd()).parent / "Sessions"
        self.sessions = [f for f in os.listdir(path) if isfile(join(path, f))]


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