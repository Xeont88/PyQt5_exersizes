import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QObject, pyqtSignal


# Сигнал создаётся с pyqtSignal() как атрибут класса внешнего класса Communicate.
class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Пользовательский сигнал closeApp присоединяется к слоту close() класса QMainWindow.
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Emit Signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()
        print('mouse clicked')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
