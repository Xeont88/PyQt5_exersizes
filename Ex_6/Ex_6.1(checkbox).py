# Check Box

import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show Title', self)
        cb.move(20, 20)
        # cb.setChecked(True)     # Почему-то в этом примере работает наоборот, как то связано с cb.toggle
        # cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 150, 200)
        self.setWindowTitle("QCheckBox")
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('Qcheck')
        else:
            self.setWindowTitle('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
