import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()  #  Метод super() возвращает объект родителя класса Example и мы вызываем его конструктор.
                            # Метод __init__() – это конструктор класса в языке Python.
        self.initUI()       # Создание GUI поручено методу initUI().

    def initUI(self):
        self.setGeometry(300,100,200, 220)  # позиции x и y нашего окна, ширина, высота окна
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('z.ico'))  # QIcon принимает путь к нашей иконке для её отображения.

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())


