import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):             # self - объект окна
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        # Чтобы создать подсказку, мы вызываем метод setTooltip(). Мы можем использовать HTML форматирование текста.
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton(self, text='Button',)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # Меняем размер у кнопки, перемещаем её в окно. Метод sizeHint() даёт рекомендуемый размер для кнопки.
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
