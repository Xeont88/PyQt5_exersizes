import sys
from PyQt5.QtWidgets import (QWidget, QCalendarWidget, QComboBox, QLabel, QSplitter, QStyle,QHBoxLayout, QLineEdit, QApplication, QFrame)
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # splitter settings
        hbox = QHBoxLayout(self)
        topLeft = QFrame(self)
        topLeft.setFrameShape(QFrame.StyledPanel)
        topRight = QFrame(self)
        topRight.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topLeft)
        splitter1.addWidget(topRight)
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        # picture
        pix_map = QPixmap('Perfect_stop_ico.png')
        lbl = QLabel(self)
        lbl.setPixmap(pix_map)
        pixmap_box = QHBoxLayout(self)
        pixmap_box.addWidget(lbl)
        topLeft.setLayout(pixmap_box)

        # comboBox
        a=[]
        for s in range(10):
            a.append(str(s))
        self.combo_box = QComboBox(self)    # self - доступный в других методах
        self.combo_box.addItems(a)
        combox_hbox = QHBoxLayout(self)     # без self - локальный
        combox_hbox.addWidget(self.combo_box)
        topRight.setLayout(combox_hbox)

        # LineEdit
        self.line_edit = QLineEdit(self)
        self.combo_box.activated[str].connect(self.onActivatedCombobox)
        combox_hbox.addWidget(self.line_edit)

        # Calendar Widget
        calendar = QCalendarWidget(self)
        calendar.setGridVisible(True)
        calendar.resize(200, 150)
        calend_box = QHBoxLayout(self)
        calend_box.addWidget(calendar)
        bottom.setLayout(calend_box)


        # window settings
        self.setGeometry(300, 300, 500, 350)
        self.setWindowTitle('Exersize 7. All in one')
        self.show()


    def onActivatedCombobox(self, text):
        self.line_edit.setText(text)
        self.line_edit.adjustSize()
        self.combo_box.move(50, 80)
        self.line_edit.move(50, 120)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())
