from PyQt5 import QtCore, QtGui, QtWidgets
import os
from pathlib import Path
from sops_widget import SOPSWidget
from data_edit_widget import DataEditWidget
from session import Session
from new_session_widget import NewSessionWidget

class SessionsWidget(SOPSWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.grid_layout = QtWidgets.QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        self.button_new_session = QtWidgets.QPushButton(text="New Session")
        self.button_import_session = QtWidgets.QPushButton(text="Import Session")
        self.button_edit = QtWidgets.QPushButton(text="Edit Session Data")
        self.button_analyze = QtWidgets.QPushButton(text="Analyze Session Data")
        self.button_delete = QtWidgets.QPushButton(text="Delete Session")
        self.recent_sessions = QtWidgets.QListWidget()

        self.load_sessions()

        self.grid_layout.addWidget(self.button_new_session, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.button_import_session, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.button_edit, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.button_analyze, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.button_delete, 4, 0, 1, 1)
        self.grid_layout.addWidget(self.recent_sessions, 0, 1, 6, 1)

        self.button_edit.clicked.connect(self.recent_session_open)
        self.button_analyze.clicked.connect(self.analyze_session_clicked)
        self.recent_sessions.doubleClicked.connect(self.recent_session_open)
        self.button_new_session.clicked.connect(self.new_session)
        self.button_delete.clicked.connect(self.delete_session_clicked)

    def recent_session_open(self):
        current_item = self.recent_sessions.currentItem()
        if current_item is not None:
            session_name = current_item.text()
            widget = DataEditWidget(self.mainwindow, session_name)
            self.mainwindow.setCentralWidget(widget)

    def analyze_session_clicked(self):
        current_item = self.recent_sessions.currentItem()
        if current_item is not None:
            session_name = current_item.text()
            widget = DataEditWidget(self.mainwindow, session_name)
            self.mainwindow.setCentralWidget(widget)

    def delete_session_clicked(self):
        current_item = self.recent_sessions.currentItem()
        self.confirm_delete = QtWidgets.QMessageBox()
        self.confirm_delete.setIcon(QtWidgets.QMessageBox.Warning)
        self.confirm_delete.setText("Are you sure that you would like to permanently delete {}?".format(current_item.text()))
        self.confirm_delete.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        self.confirm_delete.buttonClicked.connect(self.delete_session)
        retval = self.confirm_delete.exec_()
        if retval == QtWidgets.QMessageBox.Yes:
            current_item = self.recent_sessions.currentItem()

            if current_item is not None:
                session_name = current_item.text()
                session_path = Path(os.getcwd()).parent / "Sessions" / session_name
                os.remove(session_path)
                self.mainwindow.load_data()
                self.load_sessions()

    def import_session_clicked(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Import Session')
        if filename:
            session = Session.load_from_path(filename)
            session.save()
            self.mainwindow.load_sessions()
            self.load_sessions()


    def delete_session(self, msg):
        pass

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
