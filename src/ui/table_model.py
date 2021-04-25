import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt

class TableModel(QtCore.AbstractTableModel):

    def __init__(self, data):
        super().__init__()
        self._data = data
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        
    def rowCount(self, index):
        return len(self._data)
    
    def columnCount(self, index):
        return len(self._data[0])
    
