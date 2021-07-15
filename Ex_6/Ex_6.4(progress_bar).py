import sys
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication
from PyQt5.QtCore import QBasicTimer


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pBar = QProgressBar(self)
        self.pBar.setGeometry(30, 40, 210, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.btn2 = QPushButton('Reset', self)
        self.btn2.move(120, 80)
        self.btn2.clicked.connect(self.resetTimer)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 250, 140)
        self.setWindowTitle('ProgressBar')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step = self.step + 1
        self.pBar.setValue(self.step)

    def resetTimer(self):
        self.timer.stop()
        self.step = 0
        self.btn.setText('Start')
        self.pBar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
