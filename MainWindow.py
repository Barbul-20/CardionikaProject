from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget, QWidget
from PyQt5.QtCore import QObject, pyqtSlot
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Загрузка интерфейса из файла .ui
        uic.loadUi('untitled.ui', self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())