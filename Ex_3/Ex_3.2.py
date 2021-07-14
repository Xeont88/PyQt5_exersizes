# Сеточный макет

import sys
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)
        grid.setSpacing(3)      # Установить промежуток между виджетами

        # Это метки, используемые в дальнейшем для кнопок.
        names = ['1','2', '3', '4', '5', '6', '7', '8', '9', '', '0']

        # Мы создаём список позиций для сетки.
        positions = [(i, j) for i in range(4) for j in range(3)]

        print('positions', positions)

        # Используя метод addWidget, создаются и добавляются кнопки к макету
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.move(600, 150)
        self.setWindowTitle('Grid')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
