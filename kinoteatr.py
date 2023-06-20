import webbrowser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLabel
import webbrowser

def film1():
    webbrowser.open("https://www.youtube.com/watch?v=ThJEkx1Y2Pw&t=281s")


def film2():
    webbrowser.open("https://www.youtube.com/watch?v=gNSOC3YmsAk")


def film3():
    webbrowser.open("vhttps://www.youtube.com/watch?v=6pInycwhHMs")

def film4():
    webbrowser.open("https://www.youtube.com/watch?v=NHkdu_P6emU")


app = QApplication([])
win = QWidget()
win.show()

txt = QLabel("Кинотеатр")
btn1 = QPushButton("Джон Уик")
btn1.clicked.connect(film1)

btn2 = QPushButton("Человек паук")
btn2.clicked.connect(film2)

btn3 = QPushButton("Гарри Поттер")
btn3.clicked.connect(film3)

btn4 = QPushButton("Мстители")
btn4.clicked.connect(film4)

lineV = QVBoxLayout()
lineH1 = QVBoxLayout()
lineH2 = QVBoxLayout()

lineH1.addWidget(btn1)
lineH1.addWidget(btn2)

lineH2.addWidget(btn3)
lineH2.addWidget(btn4)

lineV.addLayout(lineH1)
lineV.addLayout(lineH2)

win.setLayout(lineV)

app.exec()
