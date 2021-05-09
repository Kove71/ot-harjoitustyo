import os
import sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from PyQt5.QtWidgets import QMainWindow

from ui.app_widget import ApplicationWidget


class MainWindow(QMainWindow):
    """Käyttöliittymän pääikkuna, johon asetetaan kaikki käyttöliittymäkomponentit.
    """

    def __init__(self):
        """Luokan konstruktori. Määrittelee ikkunan nimen, koon ja luo 
        ApplicationWidget-luokan, jossa käyttöliittymän toiminta on määritelty.
        """

        super().__init__()
        self.setWindowTitle("Movie Application")
        self.left = 0
        self.top = 0
        self.width = 640
        self.height = 480
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.application_widget = ApplicationWidget(self)
        self.setCentralWidget(self.application_widget)