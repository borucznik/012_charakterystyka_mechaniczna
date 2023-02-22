from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import sys
import csv


def paintEvent(self, event):
    painter = QPainter(self)
    painter.setPen(QPen(Qt.green, 8, Qt.SolidLine))
    painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
    painter.drawEllipse(40, 40, 400, 400)


"""
def dodaj():
    zmienna1 = liczba1.text()
    zmienna2 = liczba2.text()
    wynik = int(zmienna2)+int(zmienna1)
    label2.setText(str(wynik))
    print("zmienna1: " + zmienna1)
    print("zmienna2: " + zmienna2)
    print("wynik: " +wynik)

def usun():
    zmienna1 = liczba1.text()
    zmienna2 = liczba2.text()
    wynik = int(zmienna2) + int(zmienna1)
    label2.setText(str(wynik))
    print("zmienna1" + zmienna1)
    print("zmienna2" + zmienna2)
    print("wynik:" + wynik)
"""

# Read CSV file
with open("plik.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    next(reader, None)  # skip the headers
    data_read = [row for row in reader]
print(data_read)

def paintevent(self, event):
    painter = QPainter()
    painter.begin(self)
    painter.setRenderHint(QPainter.Antialiasing)
    painter.setPen(QtCore.qt.red)
    painter.setBrush(QtCore.qt.white)
    painter.drawLine(400,100,100,100)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Tutorial"
        self.top= 150
        self.left= 150
        self.width = 500
        self.height = 500
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

"""
app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(300, 300, 500, 500)
win.setWindowTitle("Charakterystyka mechaniczna")
"""
"""
label = QtWidgets.QLabel(win)
label.setText("Wynik")
label.adjustSize()
label.move(100, 100)

label2 = QtWidgets.QLabel(win)
label2.setText("Wynik")
label2.adjustSize()
label2.move(150, 100)

button = QtWidgets.QPushButton(win)
button.clicked.connect(dodaj)
button.setText("Dodaj")
button.move(100, 150)

button2 = QtWidgets.QPushButton(win)
button2.clicked.connect(usun)
button2.setText("Usun")
button2.move(50, 150)

liczba1 = QtWidgets.QLineEdit(win)
liczba1.move(300, 150)

liczba2 = QtWidgets.QLineEdit(win)
liczba2.move(300, 100)
"""
"""
win.show()
sys.exit(app.exec_())
"""