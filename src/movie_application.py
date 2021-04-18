from PyQt5.QtWidgets import QApplication # pylint: disable=no-name-in-module
from ui.ui import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec_()
