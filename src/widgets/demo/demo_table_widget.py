from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QComboBox

from ui.demo.demo_table_widget_ui import Ui_DemoTableWidget


class DemoTableWidgetWindow(QWidget, Ui_DemoTableWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        rows, columns = 4, 4
        # 设置表格的行数
        self.tableWidget.setRowCount(rows)
        # 设置表格的列数
        self.tableWidget.setColumnCount(columns)
        self.tableWidget.setHorizontalHeaderLabels([f"标题{index + 1}" for index in range(columns)])

        for row in range(rows):
            for column in range(columns):
                if column == 2:
                    """
                    在单元格中放置控件
                    """
                    cb_item = QComboBox()
                    cb_item.addItems(["男", "女"])
                    self.tableWidget.setCellWidget(row, column, cb_item)
                else:
                    item = QTableWidgetItem(f"P({row},{column})")
                    self.tableWidget.setItem(row, column, item)

        # 设置表格可伸缩
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 表格默认选中的是单个单元格，通过下面的代码可以设置成整行选中
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
