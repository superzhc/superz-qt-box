from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit

from ui.demo.demo_tab_widget_ui import Ui_DemoTabWidget


class DemoTabWidgetWindow(QWidget, Ui_DemoTabWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        self.tab1 = QWidget()
        self.tabWidget.addTab(self.tab1, "页面1")
        self.set_tab_content(self.tab1, 姓名=QLineEdit(), 联系电话=QLineEdit())
        self.tabWidget.setTabText(0, "联系方式")

        self.tab2 = QWidget()
        self.tabWidget.addTab(self.tab2, "页面2")
        self.set_tab_content(self.tab2, t=QLineEdit())

        self.tab3 = QWidget()
        self.tabWidget.addTab(self.tab3, "页面3")

    def set_tab_content(self, tab: QWidget, **kwargs):
        layout = QFormLayout()
        for label, control in kwargs.items():
            layout.addRow(label, control)
        tab.setLayout(layout)
