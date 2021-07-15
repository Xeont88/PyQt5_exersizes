# выбор цветовых значений

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QFrame, QColorDialog, QApplication
from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)
        self.btn = QPushButton(self, text='Dialog')
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Color dialog')
        self.show()

    def showDialog(self):
        # вывод 
        col = QColorDialog.getColor()
        # вывод значений цветов rgb, 0-255
        print(int(col.name()[1:3],16), int(col.name()[3:5],16), int(col.name()[5:7],16))
        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
