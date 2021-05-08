import sys 
import os
p = os.path.abspath('.')
sys.path.insert(1, p)

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLineEdit,
    QComboBox,
    QVBoxLayout,
    QLabel,
    QDateEdit,
    QHBoxLayout
)

from PyQt5.QtCore import QDate

from repositories.database_actions import DatabaseActions

class EditWindow(QWidget):

    """Käyttöliittymäluokka edit-ikkunalle. Perii QWidget-luokan.
    
    Attributes:
        id: elokuvan id
        title: elokuvan nimi
    """

    def __init__(self, movie_id, movie_title, movie_release):
        """Luokan konstruktori.

        Args:
            movie_id: elokuvan tietokanta-id
            movie_title: elokuvan nimi
            movie_release: elokuvan julkaisupäivä
        """
        
        super().__init__()
        self.id = movie_id
        self.title = movie_title
        self.release = movie_release
        self.setup_ui()

    def setup_ui(self):
        """Alustaa ikkunan käyttöliittymäkomponentit.
        """

        minimum_date = QDate.fromString(self.release, "yyyy-MM-dd")
        maximum_date = QDate.currentDate()
        self.title_label = QLabel(self.title)
        self.review_label = QLabel("Review:")
        self.watch_date_label = QLabel("Watch date:")
        self.review_entry = QComboBox()
        self.watch_date_entry = QDateEdit(QDate.currentDate())
        self.watch_date_entry.setDisplayFormat("yyyy-MM-dd")
        self.watch_date_entry.setMinimumDate(minimum_date)
        self.watch_date_entry.setMaximumDate(maximum_date)
        self.update_button = QPushButton("Update")
        self.review_entry.addItems(["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
        self.setup_layout()

    
    def setup_layout(self):
        """Alustaa ikkunan käyttöliittymäasettelun
        """

        layout = QVBoxLayout()
        review_layout = QHBoxLayout()
        watch_date_layout = QHBoxLayout()
        review_layout.addWidget(self.review_label)
        review_layout.addWidget(self.review_entry)
        watch_date_layout.addWidget(self.watch_date_label)
        watch_date_layout.addWidget(self.watch_date_entry)
        layout.addWidget(self.title_label)
        layout.addLayout(review_layout)
        layout.addLayout(watch_date_layout)
        layout.addWidget(self.update_button)

        self.setLayout(layout)
