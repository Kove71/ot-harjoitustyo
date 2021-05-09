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
    QAbstractItemView,
    QTabWidget,
    QStackedLayout
)
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from services.imdb_api import IMDBSearch # pylint: disable=wrong-import-position
from ui.table_model import TableModel # pylint: disable=wrong-import-position
from ui.search_result_model import SearchModel # pylint: disable=wrong-import-position
from ui.edit_window import EditWindow # pylint: disable=wrong-import-position
from repositories.database_actions import DatabaseActions # pylint: disable=wrong-import-position

class ApplicationWidget(QWidget):

    """Käyttöliittymästä vastaava luokka, jossa on on vastuussa suurimmasta osasta käyttöliittymää. 
    Se perii PyQt5:n QWidget-luokan ja ui:n pääikkunan.
    """

    def __init__(self, parent):
        """Luokan konstruktori, alustaa PyQt5:n tab-rakenteen, johon myöhemmin voi lisätä
        käyttöliittymäkomponentteja.

        Args:
            parent: pääikkuna, johon luokka "kiinnittyy"
        """

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
        """Alustaa käyttöliittymäkomponentit Search-näkymässä,
        jossa voi hakea elokuvia.
        """

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
        """Alustaa Search-näkymän asettelun.
        """

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
        """Suoritetaan kun painetaan "Search"-nappia. Ottaa hakutekstin ja kutsuu 
        sen perusteella IMDBSearch-luokan request_search-metodia. Metodi palauttaa
        listan tuloksista, joilla päivitetään listanäkymä. 
        """

        text = self.search_entry.text()
        text = text.strip()
        search = IMDBSearch()
        self.movie_added_label.setText("")
        self.search_results = search.request_search(text)
        self.movies_found_label.setText(f"Movies found: {search.result_length}")
        self.search_model.movie_list = self.search_results
        self.search_model.layoutChanged.emit()
        self.add_movie_button.setEnabled(True)

    def add_movie_clicked(self):
        """Suoritetaan kun painetaan "Add movie"-nappia. Tarkistaa, että listasta on 
        valittu jokin elokuva ja lisää sen tietokantaan käyttämällä IMDBSearch-luokan 
        request_title-metodia. Päivittää sen jälkeen tietokantanäkymän.
        """

        if len(self.search_view.selectedIndexes()) > 0:
            index = self.search_view.selectedIndexes()[0].row()
            api = IMDBSearch()
            if api.request_title(self.search_results[index].id):
                self.movie_added_label.setText("Movie added!")
            database = DatabaseActions()
            self.table_model.movie_data = database.select_movies()
            self.table_model.layoutAboutToBeChanged.emit()
            self.table_model.layoutChanged.emit()
                
    def setup_database_ui(self):
        """Alustaa käyttöliittymäkomponentit tietokantanäkymässä, 
        jossa voi selata lisättyjä elokuvia ja niiden tietoja.
        """

        database = DatabaseActions()
        self.table_model = TableModel(database.select_movies())
        self.table_view = QTableView()


        self.proxy_model = QtCore.QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.table_model)
        
        self.table_view.setModel(self.proxy_model)
        self.table_view.setSortingEnabled(True)
        self.table_view.verticalHeader().hide()
        self.table_view.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.edit_button = QPushButton("Edit")
        self.remove_button = QPushButton("Remove")
        self.edit_button.clicked.connect(self.edit_button_clicked)
        self.remove_button.clicked.connect(self.remove_button_clicked)
        self.setup_database_layout()
 
    def setup_database_layout(self):
        """Alustaa tietokantanäkymän asettelun.
        """

        self.database_tab.layout = QVBoxLayout()
        table_button_layout = QHBoxLayout()
        self.database_tab.layout.addWidget(self.table_view)
        table_button_layout.addWidget(self.edit_button, alignment=Qt.AlignLeft)
        table_button_layout.addWidget(self.remove_button, alignment=Qt.AlignRight)
        self.database_tab.layout.addLayout(table_button_layout)
        self.database_tab.setLayout(self.database_tab.layout)

    def edit_button_clicked(self):
        """Suoritetaan kun "Edit"-nappia painetaan. Tarkistaa onko elokuvaa valittu, 
        ja avaa ikkunan, jossa voi muokata valitun elokuvan tietoja. Luo instanssin 
        EditWindow-luokasta ja näyttää sen.

        """

        if len(self.table_view.selectedIndexes()) > 0:
            movie_id = self.table_view.selectedIndexes()[0].data()
            movie_title = self.table_view.selectedIndexes()[1].data()
            movie_release = self.table_view.selectedIndexes()[2].data()
            self.w = EditWindow(movie_id, movie_title, movie_release)
            self.w.update_button.clicked.connect(self.update_button_clicked)
            self.w.show()

    def remove_button_clicked(self):
        """Suoritetaan kun "Remove"-nappia painetaan. Tarkistaa onko elokuvaa valittu
        ja poistaa valitun elokuvan DatabaseActions-luokan delete_row-metodilla. Päivittää
        sitten käyttöliittymän.
        """

        if len(self.table_view.selectedIndexes()) > 0:
            movie_id = self.table_view.selectedIndexes()[0].data()
            database = DatabaseActions()
            database.delete_row(movie_id)
            self.table_model.movie_data = database.select_movies()
            self.table_model.layoutAboutToBeChanged.emit()
            self.table_model.layoutChanged.emit()

    def update_button_clicked(self):
        """Suoritetaan kun EditWindow-luokan "Update"-nappia painetaan.
        Pävittää tietokannan tiedot EditWindow:n parametreilla ja päivittää
        tietokannan. Lopuksi sulkee EditWindow-ikkunan.
        """

        database = DatabaseActions()
        watch_date_entry = self.w.watch_date_entry.date()
        date = watch_date_entry.toString("yyyy-MM-dd")
        database.update_data(self.w.id, self.w.review_entry.currentText(), date)
        self.table_model.movie_data = database.select_movies()
        self.table_model.layoutAboutToBeChanged.emit()
        self.table_model.layoutChanged.emit()
        self.w.close()
        