from PyQt5 import QtCore, QtGui, QtWidgets
from sessions_widget import *
from code_settings_widget import *


class HomeWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.grid_layout = QtWidgets.QGridLayout(self)

        self.button_sessions = QtWidgets.QPushButton(text="Sessions")
        self.button_codes = QtWidgets.QPushButton(text="Codes")
        self.button_settings = QtWidgets.QPushButton(text="Settings")
        self.active_widget = SessionsWidget(self)

        self.grid_layout.addWidget(self.button_sessions, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.button_codes, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.button_settings, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.active_widget, 0, 1, 5, 1)

        self.button_sessions.clicked.connect(lambda state: self.open_sessions())
        self.button_codes.clicked.connect(lambda state: self.open_codesets())


    def open_codesets(self):
        self.grid_layout.removeWidget(self.active_widget)
        self.active_widget.deleteLater()
        self.active_widget = CodeSettingsWidget(self)
        self.grid_layout.addWidget(self.active_widget, 0, 1, 5, 1)

    def open_sessions(self):
        self.grid_layout.removeWidget(self.active_widget)
        self.active_widget.deleteLater()
        self.active_widget = SessionsWidget(self)
        self.grid_layout.addWidget(self.active_widget, 0, 1, 5, 1)


