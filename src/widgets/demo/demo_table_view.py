from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHeaderView

from ui.demo.demo_table_view_ui import Ui_DemoTableView


class DemoTableViewWindow(QWidget, Ui_DemoTableView):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        rows, columns = (4, 4)
        self.model = QStandardItemModel(rows, columns)
        self.model.setHorizontalHeaderLabels([f"标题{index + 1}" for index in range(columns)])

        for row in range(rows):
            for column in range(columns):
                item = QStandardItem(f"Point({row},{column})")
                self.model.setItem(row, column, item)

        self.tableView.setModel(self.model)
        # 表格填满窗口
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
