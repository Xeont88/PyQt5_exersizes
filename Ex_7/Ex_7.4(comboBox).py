import sys
from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Ubuntu', self)

        list = ['Ubuntu', 'Mandriva', 'Fedora', 'Arch', 'Gentoo']
        combo = QComboBox(self)
        combo.addItems(list)
        combo.move(50, 50)

        self.lbl.move(50, 150)
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(30, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())

