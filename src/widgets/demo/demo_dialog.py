from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QMessageBox, QInputDialog, QFileDialog

from ui.demo.demo_dialog_ui import Ui_DemoDialog


class DemoDialogWindow(QtWidgets.QWidget, Ui_DemoDialog):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

        # 对话框不同模态
        self.btnNonModal.clicked.connect(self.showNonModalDialog)
        self.btnWindowModal.clicked.connect(self.showWindowModalDialog)
        self.btnApplicationModal.clicked.connect(self.showApplicationModalDialog)

        # QMessageBox 消息对话框
        self.btnInformation.clicked.connect(self.showInformationMessageBoxDialog)
        self.btnQuestion.clicked.connect(self.showQuestionMessageBoxDialog)
        self.btnWarning.clicked.connect(self.showWarningMessageBoxDialog)
        self.btnCritical.clicked.connect(self.showCriticalMessageBoxDialog)
        self.btnAbout.clicked.connect(self.showAboutMessageBoxDialog)

        # QInputDialog 输入对话框
        self.btnIntInputDialog.clicked.connect(self.showIntInputDialog)
        self.btnDoubleInputDialog.clicked.connect(self.showDoubleInputDialog)
        self.btnStringInputDialog.clicked.connect(self.showTextInputDialog)
        self.btnComboInputDialog.clicked.connect(self.showComboInputDialog)

        # QFileDialog 文件操作对话框
        self.btnOpenFile.clicked.connect(self.showOpenFileDialog)
        self.btnOpenFileWithFilter.clicked.connect(self.showOpenFileWithFilterDialog)
        self.btnSaveFile.clicked.connect(self.showSaveFileDialog)

    def showNonModalDialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("非模态，可以和程序的其他窗口交互")
        dialog.setWindowModality(Qt.NonModal)
        btn = QPushButton("确定", dialog)
        btn.move(50, 50)
        dialog.exec_()

    def showWindowModalDialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("窗口模态")
        dialog.setWindowModality(Qt.WindowModal)
        btn = QPushButton("确定", dialog)
        btn.move(50, 50)
        dialog.exec_()

    def showApplicationModalDialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("应用程序模态")
        dialog.setWindowModality(Qt.ApplicationModal)
        btn = QPushButton("确定", dialog)
        btn.move(50, 50)
        dialog.exec_()

    def showInformationMessageBoxDialog(self):
        reply = QMessageBox.information(self, "标题", "消息内容",
                                        QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Yes | QMessageBox.No | QMessageBox.Abort | QMessageBox.Retry | QMessageBox.Ignore,
                                        QMessageBox.Yes)
        QMessageBox.information(self, "返回结果", f"用户点击的按钮为{reply}", QMessageBox.Ok, QMessageBox.Ok)

    def showQuestionMessageBoxDialog(self):
        reply = QMessageBox.question(self, "标题", "消息内容", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        QMessageBox.information(self, "返回结果", f"用户点击的按钮为{reply}", QMessageBox.Ok, QMessageBox.Ok)

    def showWarningMessageBoxDialog(self):
        reply = QMessageBox.warning(self, "标题", "消息内容", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        QMessageBox.information(self, "返回结果", f"用户点击的按钮为{reply}", QMessageBox.Ok, QMessageBox.Ok)

    def showCriticalMessageBoxDialog(self):
        reply = QMessageBox.critical(self, "标题", "消息内容", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        QMessageBox.information(self, "返回结果", f"用户点击的按钮为{reply}", QMessageBox.Ok, QMessageBox.Ok)

    def showAboutMessageBoxDialog(self):
        QMessageBox.about(self, "标题", "消息内容")

    def showIntInputDialog(self):
        data, ok = QInputDialog.getInt(self, "输入对话框", "请输入一个整数:")
        if ok:
            QMessageBox.about(self, "返回结果", f"用户输入的整数为：{data}")

    def showDoubleInputDialog(self):
        data, ok = QInputDialog.getDouble(self, "输入对话框", "请输入一个浮点数:")
        if ok:
            QMessageBox.about(self, "返回结果", f"用户输入的浮点数为：{data}")

    def showTextInputDialog(self):
        data, ok = QInputDialog.getText(self, "输入对话框", "请输入一个文本:")
        if ok:
            QMessageBox.about(self, "返回结果", f"用户输入的文本为：{data}")

    def showComboInputDialog(self):
        data, ok = QInputDialog.getItem(self, "输入对话框", "请选择一个选项:", ["北京", "上海", "深圳"], 0, False)
        if ok:
            QMessageBox.about(self, "返回结果", f"用户选择的选项为：{data}")

    def showOpenFileDialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "D:\\")
        QMessageBox.about(self, "返回结果", file_name)

    def showSaveFileDialog(self):
        dir_name, _ = QFileDialog.getSaveFileName(self, "保存文件", "D:\\")
        QMessageBox.about(self, "消息", dir_name)

    def showOpenFileWithFilterDialog(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "打开文件", "D:\\", "Text File (*.txt)")
        QMessageBox.about(self, "返回结果", file_name)
