from PyQt5 import QtWidgets

class SOPSWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainwindow = self.get_mainwindow()

    def get_mainwindow(self):
        widget_list = QtWidgets.QApplication.topLevelWidgets()
        main_window = [widget for widget in widget_list if isinstance(widget, QtWidgets.QMainWindow)]
        return main_window[0]

