from PyQt5 import QtCore, QtGui, QtWidgets
from sops_widget import SOPSWidget
from media_viewer import *
from add_data_widget import *
from src.data_table_widget import DataTableWidget
from session import Session
import os
import pandas as pd

class DataEditWidget(SOPSWidget):
    def __init__(self, parent=None, session_name=None):
        super().__init__(parent)
        self.session = Session.load(session_name)
        self.grid_layout = QtWidgets.QGridLayout(self)
        self.to_home = QtWidgets.QPushButton("Back")

        self.media_viewer = MediaViewer(self, True)
        self.code_widget = AddDataWidget(self)

        self.data_list = QtWidgets.QTableWidget(self)
        self.data_list.setMinimumHeight(300)
        self.code_widget.setMinimumWidth(300)

        self.data_tab = QtWidgets.QTabWidget()
        self.data_tab.setTabPosition(0)
        self.data_tab.addTab(self.data_list, "Data")

        self.code_tab = QtWidgets.QTabWidget()
        self.code_tab.setTabPosition(3)
        self.code_tab.addTab(self.code_widget, "Add Data")

        self.media_viewer.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.data_tab.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.code_tab.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)

        self.grid_layout.addWidget(self.media_viewer, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.to_home, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.code_tab, 0, 1, 3, 1)
        self.grid_layout.addWidget(self.data_tab, 2, 0, 1, 1)

        self.data_tab.tabBarClicked.connect(self.data_tab_clicked)
        self.code_tab.tabBarClicked.connect(self.code_tab_clicked)
        self.to_home.clicked.connect(self.to_home_clicked)
        self.media_viewer.videoGroup.player.durationChanged.connect(lambda x: self.code_widget.set_time_maxium(x))
        self.media_viewer.videoGroup.player.positionChanged.connect(lambda x: self.code_widget.update_time(x))
        self.update_data()
        self.session.data.data.drop(self.session.data.data[self.session.data.data['Start Time'] > 16000].index, inplace=True)

    def update_data(self):
        self.data_list.clear()
        shape = self.session.data.data.shape
        self.data_list.setRowCount(shape[0])
        self.data_list.setColumnCount(shape[1])
        self.data_list.setHorizontalHeaderLabels(self.session.data.data.columns)
        for row in range(shape[0]):
            item = self.session.data.data.iloc[row]
            for col in range(shape[1]):

                if col == 0:
                    student = self.session.studentset.students[item[col]]
                    cell = student.to_str()
                else:
                    cell = str(item[col])
                temp = QtWidgets.QTableWidgetItem(cell)
                self.data_list.setItem(row, col, temp)


    def refresh_data(self):
        self.session.save()
        self.session = Session.load(self.session.name)
        self.update_data()

    def data_tab_clicked(self, index):
        widget = self.data_tab.widget(index)
        visible = widget.isVisible()
        widget.setVisible(not visible)
        tab_size = self.data_tab.size()
        if visible is True:
            self.data_tab.setFixedHeight(tab_size.height() - widget.minimumHeight())
        else:
            self.update_data()
            self.data_tab.setFixedHeight(tab_size.height() + widget.minimumHeight())


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

    def to_home_clicked(self):
        self.media_viewer.videoGroup.player.positionChanged.disconnect()
        self.mainwindow.reset_central_widget()



def main():
    app = QtWidgets.QApplication([])
    widget = DataEditWidget(session_name="Queens_LOPUS")
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()