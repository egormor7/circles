from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import sys
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellow_circles.ui', self)
        self.pushButton.clicked.connect(self.create_circles)
        self.pressed = False

    def create_circles(self):
        self.pressed = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        qp.end()

    def drawFlag(self, qp):
        if not self.pressed:
            return True
        for i in range(random.randint(10, 25)):
            size = random.randint(30, 90)
            x, y = random.randint(50, 600), random.randint(50, 500)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawEllipse(x, y, size, size)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
