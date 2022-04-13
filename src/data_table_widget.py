from PyQt5 import QtCore, QtGui, QtWidgets
from sops_widget import SOPSWidget
from session import Session

class DataTableWidget(SOPSWidget):
    def __init__(self, parent=None, active_session=None):
        super().__init__(parent)
        self.session = active_session
        self.data_list = QtWidgets.QTableWidget(self)
        self.data_list.setMinimumWidth(200)

    def update_data(self):
        self.data_list.clear()
        shape = self.session.data.data.shape
        self.data_list.setRowCount(shape[0])
        self.data_list.setColumnCount(shape[1])
        self.data_list.setHorizontalHeaderLabels(self.session.data.data.columns)
        for row in self.data.data[:]:
            print(row)
            item = self.session.data.data.iloc[row]
            for col in range(shape[1]):
                temp = QtWidgets.QTableWidgetItem(str(item[col]))
                self.data_list.setItem(row, col, temp)