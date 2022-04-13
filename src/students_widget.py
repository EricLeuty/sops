from PyQt5 import QtCore, QtGui, QtWidgets
import os
from pathlib import Path
from sops_widget import SOPSWidget
from studentset import StudentSet

class StudentsWidget(SOPSWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_layout = QtWidgets.QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        self.button_edit_studentset = QtWidgets.QPushButton(text="Edit Studentset")
        self.button_import_studentset = QtWidgets.QPushButton(text="Import Studentset")
        self.button_delete_studentset = QtWidgets.QPushButton(text="Delete Studentset")

        self.studentsets = QtWidgets.QListWidget()

        self.update_studentsets()

        self.grid_layout.addWidget(self.button_import_studentset, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.button_edit_studentset, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.button_delete_studentset, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.studentsets, 0, 1, 4, 1)

        self.button_import_studentset.clicked.connect(self.import_studentset_clicked)
        self.button_delete_studentset.clicked.connect(self.delete_studentset_clicked)


    def import_studentset_clicked(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Import Codeset')
        if filename:
            studentset = StudentSet.load_from_path(filename)
            studentset.save()
            self.mainwindow.load_studentsets()
            self.update_studentsets()

    def update_studentsets(self):
        self.studentsets.clear()
        for studentset in self.parentWidget().parentWidget().studentsets:
            temp_studentset = QtWidgets.QListWidgetItem(studentset)
            self.studentsets.addItem(temp_studentset)

    def delete_studentset_clicked(self):
        current_item = self.studentsets.currentItem()
        self.confirm_delete = QtWidgets.QMessageBox()
        self.confirm_delete.setIcon(QtWidgets.QMessageBox.Warning)
        self.confirm_delete.setText(
            "Are you sure that you would like to permanently delete {}?".format(current_item.text()))
        self.confirm_delete.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
        self.confirm_delete.buttonClicked.connect(self.delete_studentset)
        retval = self.confirm_delete.exec_()
        if retval == QtWidgets.QMessageBox.Yes:
            current_item = self.studentsets.currentItem()

            if current_item is not None:
                studentset_name = current_item.text()
                studentset_path = Path(os.getcwd()).parent / "Studentsets" / studentset_name
                os.remove(studentset_path)
                self.mainwindow.load_data()
                self.update_studentsets()

    def delete_studentset(self):
        pass







def main():
    app = QtWidgets.QApplication([])
    widget = StudentsWidget()
    widget.show()

    app.exec_()

if __name__ == '__main__':
    main()
