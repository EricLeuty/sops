from PyQt5 import QtCore, QtGui, QtWidgets
from sops_widget import SOPSWidget
from codeset import CodeSet
from dataset_edit_widget import CodesetEditWidget

class CodeSettingsWidget(SOPSWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.grid_layout = QtWidgets.QGridLayout(self)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)

        self.button_new_codeset = QtWidgets.QPushButton(text="New Codeset")
        self.button_edit_codeset = QtWidgets.QPushButton(text="Edit Codeset")
        self.button_import_codeset = QtWidgets.QPushButton(text="Import Codeset")
        self.button_delete_codeset = QtWidgets.QPushButton(text="Delete Codeset")

        self.codesets = QtWidgets.QListWidget()

        self.update_codesets()

        self.grid_layout.addWidget(self.button_new_codeset, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.button_import_codeset, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.button_edit_codeset, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.button_delete_codeset, 3, 0, 1, 1)
        self.grid_layout.addWidget(self.codesets, 0, 1, 5, 1)

        self.button_edit_codeset.clicked.connect(lambda state: self.codeset_open(self.codesets.currentItem()))
        self.codesets.doubleClicked.connect(lambda state: self.codeset_open(self.codesets.currentItem()))
        self.button_import_codeset.clicked.connect(self.import_codeset_clicked)

    def codeset_open(self, current_item):
        if current_item is not None:
            codeset_name = current_item.text()
            widget = CodesetEditWidget(self.mainwindow, codeset_name)
            self.mainwindow.setCentralWidget(widget)

    def import_codeset_clicked(self):
        filename, filter = QtWidgets.QFileDialog.getOpenFileName(parent=self, caption='Import Codeset')
        if filename:
            codeset = CodeSet.load_from_path(filename)
            codeset.save()
            self.mainwindow.load_codesets()
            self.update_codesets()

    def update_codesets(self):
        for codeset in self.parentWidget().parentWidget().codesets:
            temp_codeset = QtWidgets.QListWidgetItem(codeset)
            self.codesets.addItem(temp_codeset)







def main():
    app = QtWidgets.QApplication([])
    widget = CodeSettingsWidget()
    widget.show()

    app.exec_()

if __name__ == '__main__':
    main()


