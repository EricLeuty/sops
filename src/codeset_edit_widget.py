from PyQt5 import QtCore, QtGui, QtWidgets
from sops_widget import SOPSWidget
from codeset import CodeSet, CodeItem


class CodesetEditWidget(SOPSWidget):
    def __init__(self, parent=None, codeset_name=None):
        super().__init__(parent)
        self.setObjectName("codeset_edit_widget")

        self.codeset = CodeSet.load(codeset_name)

        self.grid_layout = QtWidgets.QGridLayout(self)
        self.button_add_code = QtWidgets.QPushButton(text="Add Code")
        self.button_delete_code = QtWidgets.QPushButton(text="Delete Code")
        self.button_back = QtWidgets.QPushButton(text="Back")
        self.codes = QtWidgets.QListWidget()

        for code in self.codeset.codes:
            temp_code = QtWidgets.QListWidgetItem(code)
            self.codes.addItem(temp_code)

        self.code_label = QtWidgets.QLabel(text="Code:")
        self.description = QtWidgets.QLabel(text="Description:")

        self.box_code = QtWidgets.QTextEdit()
        self.box_desc = QtWidgets.QTextEdit()

        self.confirm = QtWidgets.QPushButton(text="Done")

        self.grid_layout.addWidget(self.button_add_code, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.button_delete_code, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.button_back, 2, 0, 1, 1)
        self.grid_layout.addWidget(self.codes, 0, 1, 5, 1)

        self.grid_layout.addWidget(self.code_label, 0, 2, 1, 1)
        self.grid_layout.addWidget(self.box_code, 0, 3, 1, 1)
        self.grid_layout.addWidget(self.description, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.box_desc, 1, 3, 1, 1)
        self.grid_layout.addWidget(self.confirm, 2, 2, 1, 2)

        self.codes.clicked.connect(lambda state: self.code_selected(self.codes.currentItem()))
        self.confirm.clicked.connect(lambda state: self.confirm_change(self.codes.currentItem()))
        self.button_back.clicked.connect(lambda state: self.back())

    def code_selected(self, current_item):
        if current_item is not None:

            code_name = current_item.text()
            code = self.codeset.codes[code_name]
            self.box_code.setText(code_name)
            self.box_desc.setText(code['description'])

    def confirm_change(self, current_item):
        if current_item is not None:
            code_name = current_item.text()
            self.codeset.codes[code_name]['description'] = self.box_desc.toPlainText()

    def back(self):
        self.close()
        self.mainwindow.reset_central_widget()


