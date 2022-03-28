from PyQt5 import QtWidgets, QtCore, QtGui
from session import Session
from sops_widget import SOPSWidget

class DataAnalysisWidget(SOPSWidget):
    def __init__(self, parent=None, session_name=None):
        super().__init__(parent)
        self.session_name = session_name
        self.session = Session.load(session_name)
        self.grid_layout = QtWidgets.QGridLayout(self)



