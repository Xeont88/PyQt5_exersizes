import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)        # объект приложения, и список параметров из консоли
    w = QWidget()                       # Окно
    w.resize(300, 200)                  # Размер окна
    w.move(400, 400)                    # Положение окна на экране
    w.setWindowTitle("Simple Huimple")  # Название экрана
    w.show()                            # отображает виджет на экране

    sys.exit(app.exec_())               # 
