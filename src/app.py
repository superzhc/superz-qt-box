import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from widgets.main import MainWindow

if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowIcon(QIcon("../images/logo.png"))
    main_window.show()
    sys.exit(application.exec_())
