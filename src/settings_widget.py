from PyQt5 import QtCore, QtGui, QtWidgets
import os

from sops_widget import SOPSWidget


class SettingsWidget(SOPSWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.grid_layout = QtWidgets.QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        self.settings_label = QtWidgets.QLabel("Settings")

        self.grid_layout.addWidget(self.settings_label, 0, 0, 1, 1)