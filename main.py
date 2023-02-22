#sources and helps:
#https://learnpython.com/blog/read-csv-into-list-python/
#https://www.geeksforgeeks.org/how-to-embed-matplotlib-graph-in-pyqt5/




from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
import csv

# importing various libraries
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random


"""
# Read CSV file
with open("plik_2.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    #next(reader, None)  # skip the headers
    data_read = [row for row in reader]
    data_read_float = [float(row) for row in reader]
print(data_read)
print(data_read_float)
"""
#Read CSV file once again
file = open("plik_2.csv", "r")
data_read = list(csv.reader(file, delimiter=","))
file.close()
print (data_read)
data_read2 = [row[2] for row in data_read]
print (data_read2)
#axis Y - second column from csv
data_read3 = [float(row[1]) for row in data_read[1:]]
print (data_read3)
#axis X - second column from csv
data_read4 = [float(row[0]) for row in data_read[1:]]
print (data_read4)

# main window
# which inherits QDialog
class Window(QDialog):

    # constructor
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that
        # displays the 'figure'it takes the
        # 'figure' instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # this is the Navigation widget
        # it takes the Canvas widget and a parent
        self.toolbar = NavigationToolbar(self.canvas, self)

        # Just some button connected to 'plot' method
        self.button = QPushButton('Plot')

        # adding action to the button
        self.button.clicked.connect(self.plot)

        # creating a Vertical Box layout
        layout = QVBoxLayout()

        # adding tool bar to the layout
        layout.addWidget(self.toolbar)

        # adding canvas to the layout
        layout.addWidget(self.canvas)

        # adding push button to the layout
        layout.addWidget(self.button)

        # setting layout to the main window
        self.setLayout(layout)

    # action called by the push button
    def plot(self):
        # random data
        datay = [random.random() for i in range(50)]
        datay = [1,3,5]
        datay = data_read3
        datax = data_read4

        # clearing old figure
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # plot data
        ax.plot(datax,datay, '*')

        # refresh canvas
        self.canvas.draw()


# driver code
if __name__ == '__main__':
    # creating apyqt5 application
    app = QApplication(sys.argv)

    # creating a window object
    main = Window()

    # showing the window
    main.show()

    # loop
    sys.exit(app.exec_())
