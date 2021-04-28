import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):
   
    header_labels = ["Title", "Release Date", "Director", "IMDB Rating", "Length", "Review", "Watch Date"]

    def __init__(self, data):
        super().__init__()
        self.movie_data = data
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.movie_data[index.row()][index.column()]

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.header_labels[section]
        return QtCore.QAbstractTableModel.headerData(self, section, orientation, role)

    def rowCount(self, index):
        return len(self.movie_data)
    
    def columnCount(self, index):
        return len(self.movie_data[0])
    
