#sources and helps:
#https://learnpython.com/blog/read-csv-into-list-python/
#https://www.geeksforgeeks.org/how-to-embed-matplotlib-graph-in-pyqt5/

# importing various libraries
import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
import csv

#Read CSV file once again
file = open("plik_2.csv", "r")
data_read = list(csv.reader(file, delimiter=","))
file.close()
print (data_read)
data_read2 = [row[1] for row in data_read]
print (data_read2)
#axis Y - second column from csv
data_read3 = [float(row[1]) for row in data_read[1:]]
print (data_read3)
#axis X - second column from csv
data_read4 = [float(row[0]) for row in data_read[1:]]
print (data_read4)

#calculate mean\averange value of both values
sum_Y = sum(data_read3)
sum_X = sum(data_read4)
count_elements  = len(data_read3)
mean_Y = sum_Y/count_elements
mean_X = sum_X/count_elements

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
        # random data or manually put data
        #datay = [random.random() for i in range(50)]
        #datay = [1,3,5]
        #datax = [1,2,3]

        #data from csv file after conversion of list on float
        datay = data_read3
        datax = data_read4

        # clearing old figure
        self.figure.clear()

        # create an axis
        ax = self.figure.add_subplot(111)

        # plot data
        #ax.plot(datax,datay, '*')

        #or we try scatter
        ax.scatter(datax,datay,label='Punkty pracy')
        #averange/mean value
        ax.scatter(mean_X,mean_Y, label='Średni punkt pracy')
        #cosmetics
        ax.grid(True)
        ax.set_title('Charakterystyka mechaniczna')
        ax.set_xlabel('Predkosc obrotowa obr/min')
        ax.set_ylabel('Moment obrotowy Nm')
        ax.legend()

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
