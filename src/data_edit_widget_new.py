from PyQt5 import QtCore, QtGui, QtWidgets
from sops_widget import SOPSWidget
from media_viewer import *
from add_data_widget import *
from src.data_table_widget import DataTableWidget
from session import Session

class DataEditWidget(SOPSWidget):
    def __init__(self, parent=None, session_name=None):
        super().__init__(parent)
        self.session = Session.load(session_name)

        self.grid_layout = QtWidgets.QGridLayout(self)
        self.to_home = QtWidgets.QPushButton("Back")

        self.media_viewer = MediaViewer(self, True)
        self.code_widget = AddDataWidget(self)
        self.code_widget.setMinimumWidth(300)
        self.data_list = DataTableWidget(self, self.active_session)


        self.data_tab = QtWidgets.QTabWidget()
        self.data_tab.setTabPosition(2)
        self.data_tab.addTab(self.data_list, "Data")

        self.code_tab = QtWidgets.QTabWidget()
        self.code_tab.setTabPosition(3)
        self.code_tab.addTab(self.code_widget, "Add Data")

        self.grid_layout.addWidget(self.data_tab, 0, 0, 2, 1)
        self.grid_layout.addWidget(self.media_viewer, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.to_home, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.code_tab, 0, 2, 2, 1)

        self.data_tab.tabBarClicked.connect(self.data_tab_clicked)
        self.code_tab.tabBarClicked.connect(self.code_tab_clicked)
        self.to_home.clicked.connect(self.mainwindow.reset_central_widget)
        self.data_list.update_data()


    def refresh_data(self):
        self.session.save()
        self.session = Session.load(self.session_name)
        self.data_list.update_data()

    def data_tab_clicked(self, index):
        widget = self.data_tab.widget(index)
        visible = widget.isVisible()
        widget.setVisible(not visible)
        tab_size = self.data_tab.size()
        if visible is True:
            self.data_tab.setFixedWidth(tab_size.width() - widget.minimumWidth())
        else:
            self.update_data()
            self.data_tab.setFixedWidth(tab_size.width() + widget.minimumWidth())


        self.grid_layout.update()

    def code_tab_clicked(self, index):
        time = self.media_viewer.videoGroup.player.position()
        self.code_widget.update_time(time)
        widget = self.code_tab.widget(index)
        visible = widget.isVisible()
        widget.setVisible(not visible)
        tab_size = self.code_tab.size()
        if visible is True:
            self.code_tab.setFixedWidth(tab_size.width() - widget.minimumWidth())
        else:
            self.code_tab.setFixedWidth(tab_size.width() + widget.minimumWidth())


        self.grid_layout.update()



def main():
    app = QtWidgets.QApplication([])
    widget = DataEditWidget(session_name="Queens_LOPUS")
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()