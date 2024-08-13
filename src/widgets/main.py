from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction, QApplication

from ui.main_ui import Ui_MainWindow
from utils.importer import import_widget_class


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.menubar.triggered[QAction].connect(self.process_menu_trigger)

    def process_menu_trigger(self, action):
        action_object_name = action.objectName()
        print(f"用户点击菜单【{action.text()}】触发【{action_object_name}】")

        if action_object_name == "actionClose":
            self.close_main_window()

        try:
            widget = import_widget_class(action_object_name)
            if widget:
                self.inner_window = widget(self)
                self.setCentralWidget(self.inner_window)
        except Exception as err:
            print(err)
            self.open_home_window()

    def open_home_window(self):
        self.setCentralWidget(None)

    def close_main_window(self):
        application = QApplication.instance()
        application.quit()
