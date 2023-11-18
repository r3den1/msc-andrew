import random
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush


class RandomCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.pushButton = QPushButton(self)
        self.pushButton.setText('Click me!!!')
        self.pushButton.clicked.connect(self.paint)
        self.do = False

    def paintEvent(self, event):
        if self.do:
            qp = QPainter(self)
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(random.randrange(0, 256),
                           random.randrange(0, 256),
                           random.randrange(0, 256)
                           ))
        x = random.randrange(0, 500)
        y = random.randrange(0, 500)
        r = random.randrange(0, 250)
        qp.drawEllipse(x, y, r, r)
        self.do = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomCircles()
    ex.show()
    sys.exit(app.exec_())
