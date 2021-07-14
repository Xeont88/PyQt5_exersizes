import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox, QPushButton, QToolTip
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 200)
        self.setWindowIcon(QIcon('z.ico'))
        self.center()
        self.setWindowTitle("All In One!")
        btn = QPushButton(self, text='Push Me!')
        btn.clicked.connect(self.message)
        btn.move(50, 50)
        QToolTip.setFont(QFont('ComicSans', 8))
        btn.setToolTip('This is a <b>Push Button</b>!')

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit?',
                                     'Вы действительно хотите выйти?',
                                     QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel, QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            print('Quit')
            event.accept()
        else:
            print('stay')
            event.ignore()

    def message(self):
        reply = QMessageBox.question(self, 'Yo!', 'Just Push The Button', QMessageBox.Ok, QMessageBox.Ok)
        print('ok')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
