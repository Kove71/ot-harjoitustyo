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
    QListView
)

from services.imdb_api import IMDBSearch # pylint: disable=wrong-import-position
from ui.search_result_model import SearchModel # pylint: disable=wrong-import-position

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.search_results = []
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Movie Application")
        self.search_button = QPushButton("Search")
        self.add_movie_button = QPushButton("Add movie")
        self.add_movie_button.setEnabled(False)
        self.search_entry = QLineEdit()
        self.search_entry.setPlaceholderText("Search movie title")
        self.label = QLabel("Movies found: 0")
        self.movie_added_label = QLabel("")
        self.model = SearchModel()
        self.search_view = QListView()
        self.search_view.setModel(self.model)
        self.search_button.clicked.connect(self.search_button_clicked)
        self.add_movie_button.clicked.connect(self.add_movie_clicked)
        self.setup_layout()

    def setup_layout(self):
        parent_layout = QVBoxLayout()
        search_bar_layout = QHBoxLayout()
        parent_layout.addLayout(search_bar_layout)
        parent_layout.addWidget(self.label)
        parent_layout.addWidget(self.search_view)
        parent_layout.addWidget(self.add_movie_button)
        parent_layout.addWidget(self.movie_added_label)
        search_bar_layout.addWidget(self.search_entry)
        search_bar_layout.addWidget(self.search_button)
        container = QWidget()
        container.setLayout(parent_layout)
        self.setCentralWidget(container)

    def search_button_clicked(self):
        text = self.search_entry.text()
        text.strip()
        search = IMDBSearch()
        self.movie_added_label.setText("")
        self.search_results = search.request_search(text)
        self.label.setText(f"Movies found: {search.result_length}")
        self.model.movie_list = self.search_results
        self.model.layoutChanged.emit()
        self.add_movie_button.setEnabled(True)

    def add_movie_clicked(self):
        index = self.search_view.selectedIndexes()[0].row()
        api = IMDBSearch()
        if api.request_title(self.search_results[index].id):
            self.movie_added_label.setText("Movie added!")


if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
