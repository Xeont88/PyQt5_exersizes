import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event Handler')
        self.show()

    # переопределяем обработчик события keyPressEvent()
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            print('Ecsape', Qt.Key_Escape)
        if event.key() == Qt.Key_Alt:
            print( Qt.Key_Alt)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
