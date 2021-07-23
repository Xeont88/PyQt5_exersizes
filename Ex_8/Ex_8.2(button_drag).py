import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag, QMouseEvent, QDragEnterEvent, QDropEvent


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        print('button created', self.pos().x(), self.pos().y())

    def mouseMoveEvent(self, e) -> None:
        # if e.buttons() != Qt.RightButton:
        if e.buttons() != Qt.MidButton:
            return

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e) -> None:
        QPushButton.mousePressEvent(self, e)
        if e.button() == Qt.LeftButton:
            print('press')


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('Push Me!!!', self)
        self.button.move(100, 65)
        print('y=', self.button.y())
        print('x=', self.button.x())
        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 300, 300)

    def dragEnterEvent(self, a0) -> None:
        a0.accept()

    def dropEvent(self, a0) -> None:
        position = a0.pos()
        self.button.move(position)
        a0.setDropAction(Qt.MoveAction)
        a0.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    app.exec_()
