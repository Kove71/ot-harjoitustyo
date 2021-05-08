import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QModelIndex

class TableModel(QtCore.QAbstractTableModel):

    """Qt5:n käyttämä luokka, joka on vastuussa käyttöliittymäkomponentin datan käsitelystä. 
       Metodit ovat Qt5:n omia standardimetodeita. Tämä luokka käsittelee tietokannan dataa.
    """

   

    def __init__(self, data):
        super().__init__()
        self.header_labels = ["Id", "Title", "Release Date", "Director", "IMDB Rating", "Length Mins", "Review", "Watch Date"]
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
        if len(self.movie_data) == 0:
            return 0
        return len(self.movie_data[0])
    

    
