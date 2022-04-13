from PyQt5 import QtCore, QtGui, QtWidgets
from sops_widget import SOPSWidget
from sessions_widget import SessionsWidget
from code_settings_widget import CodeSettingsWidget
from settings_widget import SettingsWidget
from students_widget import StudentsWidget


class HomeWidget(SOPSWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("home_widget")
        self.mainwindow.load_data()
        self.grid_layout = QtWidgets.QGridLayout(self)

        self.button_sessions = QtWidgets.QPushButton(text="Sessions")
        self.button_codes = QtWidgets.QPushButton(text="Codesets")
        self.button_students = QtWidgets.QPushButton(text="Students")
        self.button_settings = QtWidgets.QPushButton(text="Settings")
        self.active_widget = SessionsWidget(self)

        width = 62

        self.button_sessions.setMaximumWidth(width)
        self.button_codes.setMaximumWidth(width)
        self.button_students.setMaximumWidth(width)
        self.button_settings.setMaximumWidth(width)

        self.grid_layout.addWidget(self.button_sessions, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.button_codes, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.button_students, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.button_settings, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.active_widget, 0, 1, 5, 1)

        self.button_sessions.clicked.connect(self.open_sessions)
        self.button_codes.clicked.connect(self.open_codesets)
        self.button_students.clicked.connect(self.open_students)
        self.button_settings.clicked.connect(self.open_settings)



    def open_codesets(self):
        self.grid_layout.removeWidget(self.active_widget)
        self.active_widget.deleteLater()
        self.active_widget = CodeSettingsWidget(self)
        self.grid_layout.addWidget(self.active_widget, 0, 1, 5, 1)
        print(self.button_settings.width())

    def open_sessions(self):
        self.grid_layout.removeWidget(self.active_widget)
        self.active_widget.deleteLater()
        self.active_widget = SessionsWidget(self)
        self.grid_layout.addWidget(self.active_widget, 0, 1, 5, 1)

    def open_students(self):
        self.grid_layout.removeWidget(self.active_widget)
        self.active_widget.deleteLater()
        self.active_widget = StudentsWidget(self)
        self.grid_layout.addWidget(self.active_widget, 0, 1, 5, 1)

    def open_settings(self):
        self.grid_layout.removeWidget(self.active_widget)
        self.active_widget.deleteLater()
        self.active_widget = SettingsWidget(self)
        self.grid_layout.addWidget(self.active_widget, 0, 1, 5, 1)


