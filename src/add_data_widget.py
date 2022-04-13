from PyQt5 import QtCore, QtGui, QtWidgets
from sops_widget import SOPSWidget
from dataset import *
import math
NUM_COLUMNS = 4

class AddDataWidget(SOPSWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent



        self.current_code = ""
        self.gridlayout = QtWidgets.QGridLayout(self)

        self.button_group = QtWidgets.QButtonGroup(self)
        self.button_group.setExclusive(True)

        self.start_time_label = QtWidgets.QLabel("Start Time: ")
        self.start_time = QtWidgets.QSpinBox()
        self.start_time.setValue(0)
        self.end_time_label = QtWidgets.QLabel("End Time: ")
        self.end_time = QtWidgets.QSpinBox()
        self.end_time.setValue(1)
        self.student_label = QtWidgets.QLabel("Student: ")

        self.student = QtWidgets.QComboBox()
        self.cancel = QtWidgets.QPushButton("Cancel")
        self.create = QtWidgets.QPushButton("Create")

        self.gridlayout.addWidget(self.start_time_label, 0, 0, 1, 1)
        self.gridlayout.addWidget(self.start_time, 0, 1, 1, NUM_COLUMNS - 1)

        row_skip = 1

        if self.parent.session.end_time_enabled:
            self.gridlayout.addWidget(self.end_time_label, 1, 0, 1, 1)
            self.gridlayout.addWidget(self.end_time, 1, 1, 1, NUM_COLUMNS - 1)
            row_skip = 2

        idx = 0
        for code in self.parentWidget().session.codeset.codes:
            data = self.parentWidget().session.codeset.codes[code]
            button = QtWidgets.QPushButton(code, self)
            button.setToolTip(data["description"])
            button.setCheckable(True)
            self.button_group.addButton(button, id=idx)
            row = idx // NUM_COLUMNS
            col = idx % NUM_COLUMNS
            self.gridlayout.addWidget(button, row + row_skip + 1, col)

            idx += 1

        for student in self.parentWidget().session.studentset.students:
            temp_student = self.parentWidget().session.studentset.students[student]
            self.student.addItem(temp_student.to_str(), userData=temp_student)

        self.gridlayout.addWidget(self.student_label, row_skip, 0, 1, 1)
        self.gridlayout.addWidget(self.student, row_skip, 1, 1, NUM_COLUMNS-1)
        self.gridlayout.addWidget(self.cancel, idx//NUM_COLUMNS + row_skip + 1, 0, 1, NUM_COLUMNS // 2)
        self.gridlayout.addWidget(self.create, idx // NUM_COLUMNS + row_skip + 1, 2, 1, NUM_COLUMNS // 2)



        self.start_time.valueChanged.connect(self.set_end_time_min)
        self.button_group.buttonClicked.connect(lambda event: self.set_code(event))
        self.cancel.clicked.connect(self.parent.code_tab_clicked)
        self.create.clicked.connect(self.create_datapoint)




    def set_code(self, event):
        self.current_code = event.text()

    def update_time(self, time):
        time = float(time) / 1000
        self.start_time.setValue(time)

    def set_time_maxium(self, max_time):
        time = float(max_time) / 1000
        self.start_time.setMaximum(max_time)
        self.end_time.setMaximum(max_time)

    def create_datapoint(self):
        if self.parent.session.end_time_enabled:
            datapoint = Datum(self.student.currentData().id_number, self.current_code, self.start_time.value(),
                              device_id="dev1", end_time=self.end_time.value())
        else:
            datapoint = Datum(self.student.currentData().id_number, self.current_code, self.start_time.value(),
                              device_id="dev1")
        self.parent.session.data.add_datum(datapoint)
        self.parent.refresh_data()

    def set_end_time_min(self):
        min = self.start_time.value()
        if self.end_time.value() < min:
            self.end_time.setValue(min)
        self.end_time.setMinimum(min)





def main():
    app = QtWidgets.QApplication([])
    widget = AddDataWidget()
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()
