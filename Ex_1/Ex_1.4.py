# Dialog windows

import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,300,250)
        self.setWindowTitle('Message box')
        self.show()

    #  вызывается QCloseEvent. необходимо переопределить обработчик событий closeEvent().
    def closeEvent(self, event):
        # Третий аргумент указывает комбинацию кнопок, появляющихся в диалоге.
        # Последний параметр – кнопка по умолчанию.
        # Это кнопка, которая первоначально имеет на себе указатель клавиатуры.
        reply = QMessageBox.question(self, 'Quit', 'R u sure to quit?', QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            print('goooood bye!')
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
