from PyQt5 import QtWidgets

class SOPSWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainwindow = self.get_mainwindow()
        self.active_session = None

    def get_mainwindow(self):
        widget_list = QtWidgets.QApplication.topLevelWidgets()
        main_window = [widget for widget in widget_list if isinstance(widget, QtWidgets.QMainWindow)]
        return main_window[0]

    def set_active_session(self, active_session):
        if not self.active_session:
            self.active_session = active_session
        else:
            print("Error: An active session is already assigned.")

    def clear_active_session(self):
        if self.active_session:
            self.active_session = None
        else:
            print("Error: There is no active session to clear.")

