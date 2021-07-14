# Центрирование окна на экране

import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # Мы получаем прямоугольник, точно определяющий форму главного окна.
        qr = self.frameGeometry()

        # Класс QtGui.QDesktopWidget предоставляет информацию о пользовательском рабочем столе, включая размер экрана.
        # Мы выясняем разрешение экрана нашего монитора. Из этого разрешения, мы получаем центральную точку.
        cp = QDesktopWidget().availableGeometry().center()

        # Наш прямоугольник уже имеет высоту и ширину. Теперь мы устанавливаем центр прямоугольника в центр экрана.
        # Размер прямоугольника не изменяется.
        qr.moveCenter(cp)

        # Мы перемещаем верхнюю левую точку окна приложения в верхнюю левую точку прямоугольника qr,
        # таким образом центрируя окно на нашем экране
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
