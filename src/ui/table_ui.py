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
    QTableView
)

from services.imdb_api import IMDBSearch # pylint: disable=wrong-import-position
from ui.table_model import TableModel # pylint: disable=wrong-import-position
from repositories.database_actions import DatabaseActions

