from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel, 
    QPushButton, 
    QLineEdit,
    QHBoxLayout, 
    QWidget, 
    QVBoxLayout,
    QListView
)   
from PyQt5.QtCore import Qt, QSize
import PyQt5.QtGui as Gui

import os, sys

p = os.path.abspath('.')
sys.path.insert(1, p)

from imdb_search import IMDBSearch
from search_result_model import SearchModel

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Movie Application")
        self.search_button = QPushButton("Search")
        self.add_movie_button = QPushButton("Add movie")
        self.add_movie_button.setEnabled(False)
        self.search_entry = QLineEdit()
        self.search_entry.setPlaceholderText("Search movie title")
        self.label = QLabel("Movies found: 0")
        self.model = SearchModel()
        self.search_view = QListView()
        self.search_view.setModel(self.model)
        self.search_button.clicked.connect(self.search_button_clicked)
        self.add_movie_button.clicked.connect(self.add_movie_clicked)
        self.setupLayout()
    
    def setupLayout(self):
        
        parent_layout = QVBoxLayout()
        search_bar_layout = QHBoxLayout()
        parent_layout.addLayout(search_bar_layout)
        parent_layout.addWidget(self.label)
        parent_layout.addWidget(self.search_view)
        parent_layout.addWidget(self.add_movie_button)
        search_bar_layout.addWidget(self.search_entry)
        search_bar_layout.addWidget(self.search_button)
        container = QWidget()
        container.setLayout(parent_layout)
        self.setCentralWidget(container)

    def search_button_clicked(self):
        text = self.search_entry.text()
        search = IMDBSearch()
        self.search_results = search.request_search(text)
        self.label.setText(f"Movies found: {search.n}")
        self.model.movie_list = self.search_results
        self.model.layoutChanged.emit()
        self.add_movie_button.setEnabled(True)

    def add_movie_clicked(self):
        index = self.search_view.selectedIndexes()[0].row()
        api = IMDBSearch()
        api.request_title(self.search_results[index].id)
            

 


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()