from PyQt5 import QtCore, QtGui, QtWidgets
from sops_widget import SOPSWidget
from session import *

class NewSessionWidget(SOPSWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_layout = QtWidgets.QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        self.name_edit_box = QtWidgets.QTextEdit()
        self.codeset = QtWidgets.QComboBox()
        self.studentset = QtWidgets.QComboBox()
        self.media = QtWidgets.QComboBox()
        self.back = QtWidgets.QPushButton("Back")
        self.create_session = QtWidgets.QPushButton("Create Session")

        self.grid_layout.addWidget(self.back)

        self.back.clicked.connect(self.back_clicked)

    def back_clicked(self):
        self.close()
        self.mainwindow.reset_central_widget()
