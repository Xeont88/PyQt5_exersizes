import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)   # делаем возможными события перетаскивания для виджета.

    # сообщаем о типе данных, который мы допускаем. В нашем случае, это обычный текст.
    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    # меняем текст виджета кнопки.
    def dropEvent(self, e):
        self.setText(e.mimeData().text())


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        #  активировать встроенную поддержку операций перетаскивания
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button('Button', self)
        button.move(190, 65)

        self.setWindowTitle("Simple Grag'n'Drop ")
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    app.exec_()
