#

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QMessageBox
from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import QCoreApplication       # Нам необходим объект из модуля QtCore.


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        exitAction = QAction(QIcon('z.ico'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Application')
        exitAction.triggered.connect(qApp.quit)
        # exitAction.triggered.connect(QCoreApplication.instance().quit)    # Неудачная попытка
        self.statusBar()
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAction)

        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Menu bar')
        self.show()


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
