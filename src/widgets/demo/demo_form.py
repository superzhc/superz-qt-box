import json
import os

from PyQt5.QtWidgets import QWidget

from ui.demo.demo_form_ui import Ui_DemoForm

current_dir = os.path.dirname(__file__)
pca_path = os.path.join(current_dir, "../../../data/pca-code.json")


class DemoFormWindow(QWidget, Ui_DemoForm):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        with open(pca_path, "r", encoding="UTF-8") as f:
            self.pca = json.load(f)

        self.pca_map = {
            province["name"]: {
                city["name"]: [
                    area["name"] for area in city["children"]
                ]
                for city in province["children"]
            }
            for province in self.pca}

        self.init_cb_province()
        self.init_cb_city()
        self.init_cb_province()
        self.cbProvince.currentIndexChanged.connect(self.province_changed)
        self.cbCity.currentIndexChanged.connect(self.city_changed)

    def init_cb_province(self):
        self.cbProvince.addItem("-请选择省-")
        if self.pca:
            self.cbProvince.addItems(self.pca_map.keys())

    def init_cb_city(self):
        self.cbCity.addItem("-请选择市-")

    def init_cb_area(self):
        self.cbArea.addItem("-请选择区/县-")

    def province_changed(self):
        current_province = self.cbProvince.currentText()
        self.cbCity.clear()
        self.cbArea.clear()

        if not current_province == "-请选择省-":
            self.cbCity.addItems(self.pca_map[current_province].keys())

    def city_changed(self):
        current_province = self.cbProvince.currentText()
        current_city = self.cbCity.currentText()
        self.cbArea.clear()

        self.cbArea.addItem("-请选择区/县-")
        if current_city and not current_city == "-请选择市-":
            self.cbArea.addItems(self.pca_map[current_province][current_city])
