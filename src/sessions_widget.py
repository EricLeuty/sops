from PyQt5 import QtCore, QtGui, QtWidgets
from session import *
from coding_widget import *

class SessionsWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.grid_layout = QtWidgets.QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        self.button_new_session = QtWidgets.QPushButton(text="New Session")
        self.button_open = QtWidgets.QPushButton(text="Open Session")
        self.button_delete = QtWidgets.QPushButton(text="Delete Session")
        self.recent_sessions = QtWidgets.QListWidget()

        for session_name in self.parentWidget().parentWidget().sessions:
            temp_session = QtWidgets.QListWidgetItem(session_name)
            self.recent_sessions.addItem(temp_session)

        self.grid_layout.addWidget(self.button_new_session, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.button_open, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.button_delete, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.recent_sessions, 0, 1, 5, 1)

        self.button_open.clicked.connect(lambda state: self.recent_session_open(self.recent_sessions.currentItem()))
        self.recent_sessions.doubleClicked.connect(lambda state: self.recent_session_open(self.recent_sessions.currentItem()))


    def recent_session_open(self, current_item):
        if current_item is not None:
            session_name = current_item.text()
            widget = CodingWidget(self.parent().parent(), session_name)
            self.parentWidget().parentWidget().setCentralWidget(widget)





def main():
    app = QtWidgets.QApplication([])
    widget = SessionsWidget()
    widget.show()

    app.exec_()

if __name__ == '__main__':
    main()
