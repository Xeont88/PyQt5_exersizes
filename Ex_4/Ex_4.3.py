import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton


class Example(QMainWindow):
    count = 0

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton(self, text='Button 1')
        btn1.move(30,50)
        btn2 = QPushButton(self, text='Button 2')
        btn2.move(200,50)

        # Обе кнопки подключены к одному слоту.
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 650, 250)
        self.setWindowTitle('Event Sender')
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == 'Button 1':
            self.count += 1
        else:
            self.count -= 1
        self.statusBar().showMessage(sender.text() + ' was pressed ' + str(self.count))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
