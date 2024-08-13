from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtWidgets import QWidget

from ui.demo.demo_form_input_ui import Ui_DemoFormInputWindow


class DemoFormInputWindow(QWidget, Ui_DemoFormInputWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.init_input_validator()

    def init_input_validator(self):
        int_validator = QIntValidator(self)
        int_validator.setRange(0, 100)
        self.txt_int_validator.setValidator(int_validator)

        double_validator = QDoubleValidator(self)
        double_validator.setRange(0, 100)
        double_validator.setNotation(QDoubleValidator.StandardNotation)
        double_validator.setDecimals(2)
        self.txt_double_validator.setValidator(double_validator)

        # 字母和数字
        reg = QRegExp("[a-zA-Z0-9]+$")
        reg_validator = QRegExpValidator(self)
        reg_validator.setRegExp(reg)
        self.txt_reg_validator.setValidator(reg_validator)
