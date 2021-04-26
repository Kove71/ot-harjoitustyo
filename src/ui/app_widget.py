import os
import sys
p = os.path.abspath('.')
sys.path.insert(1, p)

from PyQt5.QtWidgets import ( # pylint: disable=no-name-in-module
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QLineEdit,
    QHBoxLayout,
    QWidget,
    QVBoxLayout,
    QTableView,
    QListView,
    QTabWidget
)

from services.imdb_api import IMDBSearch # pylint: disable=wrong-import-position
from ui.table_model import TableModel # pylint: disable=wrong-import-position
from ui.search_result_model import SearchModel
from repositories.database_actions import DatabaseActions

class ApplicationWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        self.tabs = QTabWidget()
        self.search_tab = QWidget()
        self.database_tab = QWidget()

        self.tabs.addTab(self.search_tab, "Search")
        self.tabs.addTab(self.database_tab, "Movies")

        self.setup_search_ui()
        self.setup_database_ui()

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    

    def setup_search_ui(self):
        self.search_button = QPushButton("Search")
        self.add_movie_button = QPushButton("Add movie")
        self.add_movie_button.setEnabled(False)
        self.search_entry = QLineEdit()
        self.search_entry.setPlaceholderText("Search movie title")
        self.movies_found_label = QLabel("Movies found: 0")
        self.movie_added_label = QLabel("")
        self.search_model = SearchModel()
        self.search_view = QListView()
        self.search_view.setModel(self.search_model)
        self.search_button.clicked.connect(self.search_button_clicked)
        self.add_movie_button.clicked.connect(self.add_movie_clicked)
        self.setup_search_layout()

    def setup_search_layout(self):
        self.search_tab.layout = QVBoxLayout()
        search_bar_layout = QHBoxLayout()
        search_bar_layout.addWidget(self.search_entry)
        search_bar_layout.addWidget(self.search_button)

        self.search_tab.layout.addLayout(search_bar_layout)
        self.search_tab.layout.addWidget(self.movies_found_label)
        self.search_tab.layout.addWidget(self.search_view)
        self.search_tab.layout.addWidget(self.add_movie_button)
        self.search_tab.layout.addWidget(self.movie_added_label)
        self.search_tab.setLayout(self.search_tab.layout)

    def search_button_clicked(self):
        text = self.search_entry.text()
        text.strip()
        search = IMDBSearch()
        self.movie_added_label.setText("")
        self.search_results = search.request_search(text)
        self.movies_found_label.setText(f"Movies found: {search.result_length}")
        self.search_model.movie_list = self.search_results
        self.search_model.layoutChanged.emit()
        self.add_movie_button.setEnabled(True)

    def add_movie_clicked(self):
        if len(self.search_view.selectedIndexes()) > 0:
            index = self.search_view.selectedIndexes()[0].row()
            api = IMDBSearch()
            if api.request_title(self.search_results[index].id):
                self.movie_added_label.setText("Movie added!")
            database = DatabaseActions()
            self.table_model.movie_data = database.select_movies()
            self.table_model.layoutChanged.emit()
                
    def setup_database_ui(self):
        database = DatabaseActions()
        self.table_model = TableModel(database.select_movies())
        self.table_view = QTableView()
        self.table_view.setModel(self.table_model)
        self.setup_database_layout()
    
    def setup_database_layout(self):
        self.database_tab.layout = QVBoxLayout()
        self.database_tab.layout.addWidget(self.table_view)
        self.database_tab.setLayout(self.database_tab.layout)