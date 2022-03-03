from PyQt5 import QtCore, QtGui, QtWidgets
from sops_widget import SOPSWidget
from observation import *
import math
NUM_COLUMNS = 4

class DataEditWidget(SOPSWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.current_code = ""
        self.gridlayout = QtWidgets.QGridLayout(self)

        self.start_time = QtWidgets.QSpinBox()
        self.start_time.setValue(0)
        self.student = QtWidgets.QComboBox()
        self.cancel = QtWidgets.QPushButton("Cancel")
        self.create = QtWidgets.QPushButton("Create")
        self.button_group = QtWidgets.QButtonGroup(self)

        idx = 0
        for code in self.parentWidget().session.codeset.codes:
            row = idx // NUM_COLUMNS
            col = idx % NUM_COLUMNS
            button = QtWidgets.QPushButton(code, self)
            self.button_group.addButton(button, id=idx)
            self.gridlayout.addWidget(button, row + 2, col)

            idx += 1

        for student in self.parentWidget().session.student_set:
            self.student.addItem(student)

        self.gridlayout.addWidget(self.start_time, 0, 0, 1, NUM_COLUMNS)
        self.gridlayout.addWidget(self.student, 1, 0, 1, NUM_COLUMNS)
        self.gridlayout.addWidget(self.cancel, idx//NUM_COLUMNS + 2, 0, 1, NUM_COLUMNS // 2)
        self.gridlayout.addWidget(self.create, idx // NUM_COLUMNS + 2, 2, 1, NUM_COLUMNS // 2)

        self.button_group.buttonClicked.connect(lambda event: self.set_code(event))
        self.cancel.clicked.connect(self.parentWidget().hide_code_widget)
        self.create.clicked.connect(self.create_datapoint)


    def set_code(self, event):
        self.current_code = event.text()

    def update_time(self, time):
        self.start_time.setValue(time)

    def create_datapoint(self):
        datapoint = Datum(self.student.currentText(), self.current_code, "Device_1", self.start_time.value())
        self.parentWidget().session.add_datum(datapoint)
        self.parentWidget().refresh_data()
        self.parentWidget().hide_code_widget()





def main():
    app = QtWidgets.QApplication([])
    widget = DataEditWidget()
    widget.show()
    app.exec_()

if __name__ == '__main__':
    main()
