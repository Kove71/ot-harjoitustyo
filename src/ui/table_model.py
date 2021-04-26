import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super().__init__()
        self.movie_data = data
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.movie_data[index.row()][index.column()]
        
    def rowCount(self, index):
        return len(self.movie_data)
    
    def columnCount(self, index):
        return len(self.movie_data[0])
    
