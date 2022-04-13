from PyQt5 import QtWidgets, QtCore, QtGui
from session import Session
from sops_widget import SOPSWidget
import sys
import math
import matplotlib
import pandas as pd
matplotlib.use('Qt5Agg')

from matplotlib.backends\
    .backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.cm import get_cmap

class DataAnalysisWidget(SOPSWidget):
    def __init__(self, parent=None, session_name=None):
        super().__init__(parent)
        self.session = Session.load(session_name)
        self.data = self.session.data.data.copy()
        self.grid_layout = QtWidgets.QGridLayout(self)
        self.figure = PltWidget(self.grid_layout)
        self.student = QtWidgets.QComboBox()
        self.plot = QtWidgets.QPushButton("Plot Data")
        self.plot_all = QtWidgets.QPushButton("Plot All")
        self.save_fig = QtWidgets.QPushButton("Save Figure")
        self.to_home = QtWidgets.QPushButton("Back")
        self.canvas = PltWidget(self)
        self.data_list = QtWidgets.QTableWidget(self)
        self.data_list.setMinimumWidth(200)

        self.max_time = self.data["Start Time"].max()

        self.unique_codes = self.data["Behavior Code"].unique()
        code_numbers = [idx for idx in range(len(self.unique_codes))]
        self.unique_codes = pd.Series(data=code_numbers, index=self.unique_codes)
        self.data["Code ID"] = self.data["Behavior Code"].map(self.unique_codes)

        set3 = get_cmap('Set3')
        self.unique_students = self.data["Student ID"].unique()
        self.color_map = pd.Series(data=set3.colors[:len(self.unique_students)], index=self.unique_students)
        self.data["cmap"] = self.data["Student ID"].map(self.color_map)

        for student_id in self.unique_students:
            self.student.addItem(str(student_id), userData=student_id)

        self.reset_plot()
        self.update_data()

        self.grid_layout.addWidget(self.student, 0, 0, 1, 2)
        self.grid_layout.addWidget(self.plot, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.plot_all, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.to_home, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.save_fig, 2, 1, 1, 1)
        self.grid_layout.addWidget(self.canvas, 0, 2, 4, 5)
        self.grid_layout.addWidget(self.data_list, 4, 0, 1, 7)


        self.plot.clicked.connect(self.plot_student_data)
        self.plot_all.clicked.connect(self.plot_all_data)
        self.to_home.clicked.connect(self.to_home_clicked)
        self.save_fig.clicked.connect(self.save_fig_clicked)

    def reset_plot(self):
        self.canvas.axes.cla()
        self.canvas.axes.set_xlim([0, self.max_time + 1])
        self.canvas.axes.set_ylim([0, len(self.unique_codes)])


    def plot_student_data(self):
        self.reset_plot()

        current_id = self.student.currentData()
        selected_data = self.data.loc[self.data["Student ID"] == current_id]

        self.canvas.axes.scatter(selected_data["Start Time"], selected_data["Code ID"])
        self.canvas.axes.set_yticks(self.unique_codes, labels=self.unique_codes.index)
        self.canvas.axes.set_xlabel("Time (s)")
        self.canvas.axes.set_ylabel("Behaviour Code")
        self.canvas.axes.set_title("Student: {}".format(current_id))
        self.canvas.fig.tight_layout(pad=2)
        self.canvas.draw()

    def plot_all_data(self):
        self.reset_plot()
        for student in self.unique_students:
            temp_data = self.data.loc[self.data["Student ID"] == student]
            self.canvas.axes.scatter(temp_data["Start Time"], temp_data["Code ID"], c=temp_data["cmap"],
                                     label=student)

        self.canvas.axes.set_yticks(self.unique_codes, labels=self.unique_codes.index)
        self.canvas.axes.set_xlabel("Time (s)")
        self.canvas.axes.set_ylabel("Behaviour Code")
        self.canvas.axes.set_title("Whole Class Data")
        self.canvas.axes.legend(bbox_to_anchor=(1.04,1), loc="upper left")
        self.canvas.fig.tight_layout(pad=2)
        self.canvas.draw()

        print(self.canvas.size)

    def to_home_clicked(self):
        self.mainwindow.reset_central_widget()


    def save_fig_clicked(self):
        filename, filter = QtWidgets.QFileDialog.getSaveFileName(parent=self, caption='Save Figure')
        if filename:
            self.canvas.fig.savefig(filename)

    def update_data(self):
        self.data_list.clear()
        shape = self.session.data.data.shape

        self.data_list.setRowCount(shape[0])
        self.data_list.setColumnCount(shape[1])
        self.data_list.setHorizontalHeaderLabels(self.session.data.data.columns)
        for row in range(shape[0]):
            item = self.session.data.data.iloc[row]
            for col in range(shape[1]):
                temp = QtWidgets.QTableWidgetItem(str(item[col]))
                self.data_list.setItem(row, col, temp)






class PltWidget(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=4, height=3, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(PltWidget, self).__init__(self.fig)


    def add_plot(self, xdata, ydata, label=None, format=None):
        self.axes.plot(xdata, ydata)

    def clear_plot(self):
        self.fig.clear()






