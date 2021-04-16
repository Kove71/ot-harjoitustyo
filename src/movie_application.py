from ui.ui import MainWindow
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec_()