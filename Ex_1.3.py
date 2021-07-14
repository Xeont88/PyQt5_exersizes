import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication       # Нам необходим объект из модуля QtCore.

'''
Система обработки событий в PyQt5 построена на механизме сигналов и слотов. Если мы кликаем по кнопке, 
выдаётся сигнал clicked. Слот может быть слотом Qt или любым слотом, вызываемым из Python. QCoreApplication 
содержит цикл главного события; он обрабатывает и выполняет все события. Метод instance даёт нам его 
текущий экземпляр. Заметим, что QCoreApplication создаётся с QApplication. Кликнутый сигнал соединяется с 
методом quit(), который и завершает приложение. Взаимосвязь сделана между двумя объектами: отправителем и получателем. 
Отправитель – нажатие кнопки, получатель – объект приложения.
'''


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        qbtn = QPushButton(self, text='Quit')
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('Quit Button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())

