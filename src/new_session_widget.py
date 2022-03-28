from PyQt5 import QtCore, QtGui, QtWidgets
import os
from pathlib import Path
from sops_widget import SOPSWidget
from session import *
from codeset import CodeSet

class NewSessionWidget(SOPSWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_layout = QtWidgets.QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        self.name_edit_box = QtWidgets.QTextEdit()
        self.name_label = QtWidgets.QLabel("Session Name: ")
        self.codeset_label = QtWidgets.QLabel("Codeset: ")
        self.studentset_label = QtWidgets.QLabel("Studentset: ")
        self.media_label = QtWidgets.QLabel("Path to Media: ")
        self.codeset = QtWidgets.QComboBox()
        self.studentset = QtWidgets.QComboBox()
        self.media_box = QtWidgets.QTextEdit()
        self.media_path = QtWidgets.QPushButton("Path to File")
        #self.media_path.setIcon(QtWidgets.QFileIconProvider.File)
        self.back = QtWidgets.QPushButton("Back")
        self.create_session = QtWidgets.QPushButton("Create Session")

        self.codeset.addItems(self.mainwindow.codesets)
        self.studentset.addItems(self.mainwindow.studentsets)
        self.grid_layout.addWidget(self.name_label, 0, 0)
        self.grid_layout.addWidget(self.name_edit_box, 0, 1)
        self.grid_layout.addWidget(self.codeset_label, 1, 0)
        self.grid_layout.addWidget(self.codeset, 1, 1)
        self.grid_layout.addWidget(self.studentset_label, 2, 0)
        self.grid_layout.addWidget(self.studentset, 2, 1)
        self.grid_layout.addWidget(self.media_label, 3, 0)
        self.grid_layout.addWidget(self.media_box, 3, 1)
        self.grid_layout.addWidget(self.media_path, 3, 2)
        self.grid_layout.addWidget(self.back)
        self.grid_layout.addWidget(self.create_session)

        self.back.clicked.connect(self.back_clicked)
        self.create_session.clicked.connect(self.create_session_clicked)
        self.media_path.clicked.connect(self.media_path_clicked)

    def back_clicked(self):
        self.close()
        self.mainwindow.reset_central_widget()

    def create_session_clicked(self):
        session_name = self.name_edit_box.toPlainText()
        codeset = CodeSet.load(self.codeset.currentText())
        studentset = StudentSet.load(self.studentset.currentText())
        media_path = self.media_box.toPlainText()
        temp_session = Session(session_name, code_set=codeset, student_set=studentset, path_media=media_path)
        temp_session.save()
        self.close()
        self.mainwindow.reset_central_widget()

    def media_path_clicked(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Open file')
        if filename:
            self.media_box.setText(filename)


