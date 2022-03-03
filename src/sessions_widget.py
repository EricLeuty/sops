from PyQt5 import QtCore, QtGui, QtWidgets
from sops_widget import SOPSWidget
from coding_widget import CodingWidget
from new_session_widget import NewSessionWidget

class SessionsWidget(SOPSWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.grid_layout = QtWidgets.QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        self.button_new_session = QtWidgets.QPushButton(text="New Session")
        self.button_open = QtWidgets.QPushButton(text="Open Session")
        self.button_delete = QtWidgets.QPushButton(text="Delete Session")
        self.recent_sessions = QtWidgets.QListWidget()

        self.load_sessions()

        self.grid_layout.addWidget(self.button_new_session, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.button_open, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.button_delete, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.recent_sessions, 0, 1, 5, 1)

        self.button_open.clicked.connect(self.recent_session_open)
        self.recent_sessions.doubleClicked.connect(self.recent_session_open)
        self.button_new_session.clicked.connect(self.new_session)
        self.button_delete.clicked.connect(self.delete_session)

    def recent_session_open(self):
        current_item = self.recent_sessions.currentItem()
        if current_item is not None:
            session_name = current_item.text()
            widget = CodingWidget(self.mainwindow, session_name)
            self.mainwindow.setCentralWidget(widget)

    def delete_session(self):
        current_item = self.recent_sessions.currentItem()
        if current_item is not None:
            session_name = current_item.text()
            self.mainwindow.sessions.remove(session_name)
            self.load_sessions()

    def new_session(self):
        self.close()
        widget = NewSessionWidget(self.mainwindow)
        self.mainwindow.setCentralWidget(widget)

    def load_sessions(self):
        self.recent_sessions.clear()
        for session_name in self.mainwindow.sessions:
            temp_session = QtWidgets.QListWidgetItem(session_name)
            self.recent_sessions.addItem(temp_session)


def main():
    app = QtWidgets.QApplication([])
    widget = SessionsWidget()
    widget.show()

    app.exec_()

if __name__ == '__main__':
    main()
