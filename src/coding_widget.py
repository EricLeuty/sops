from PyQt5 import QtCore, QtGui, QtWidgets
from sops_widget import SOPSWidget
from media_viewer import *
from data_edit_widget import *
from session import Session

class CodingWidget(SOPSWidget):
    def __init__(self, parent=None, session_name=None):
        super().__init__(parent)
        self.session_name = session_name
        self.session = Session.load(session_name)

        self.grid_layout = QtWidgets.QGridLayout(self)


        self.media_viewer = MediaViewer(self, True)
        self.code_widget = DataEditWidget(self)
        self.data_list = QtWidgets.QListWidget()
        self.dock = QtWidgets.QDockWidget()
        self.dock.setWidget(self.data_list)
        self.mainwindow.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.dock)

        self.grid_layout.addWidget(self.media_viewer, 0, 0, 1, 1)

        self.update_data()


    def show_code_widget(self):
        time = self.media_viewer.videoGroup.player.position()
        self.code_widget.update_time(time)
        self.grid_layout.addWidget(self.code_widget, 0, 1, 1, 1)
        self.code_widget.show()

    def hide_code_widget(self):
        self.code_widget.hide()
        self.grid_layout.removeWidget(self.code_widget)
        self.update_data()

    def update_data(self):
        self.data_list.clear()
        for row in self.session.data.data.iloc[:, 0]:
            temp = QtWidgets.QListWidgetItem(row)
            self.data_list.addItem(temp)
        self.data_list.update()


    def refresh_data(self):
        self.session.save()
        self.session = Session.load(self.session_name)


def main():
    app = QtWidgets.QApplication([])
    widget = CodingWidget(session_name="Queens_LOPUS")
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()