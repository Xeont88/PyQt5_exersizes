import sys
from PyQt5.QtWidgets import QWidget, QCalendarWidget, QLabel, QApplication
from PyQt5.QtCore import QDate


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        calend = QCalendarWidget(self)
        calend.setGridVisible(True)
        # calend.resize(200, 150)
        # calend.move(20, 20)
        calend.setGeometry(20, 20, 300, 200)
        calend.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = calend.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        print(date)
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
