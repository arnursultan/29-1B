# import sys
# from PyQt6.QtWidgets import QApplication, QLabel, QWidget
#
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle("Моё первое окно")
# window.setGeometry(100, 100, 280, 80)
#
# label = QLabel('<h2>Привет, PyQt6<h2>', parent=window)
# label.move(60, 15)
#
# window.show()
# sys.exit(app.exec())

import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окно через класс")
        self.setGeometry(100, 100, 300, 100)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel("Привет от класса!", self)
        label.move(80, 30)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())