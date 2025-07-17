# Основные виджеты PyQt6:
# Виджет - Назначение
# QLabel - Текстовая метка
# QPushButton - Кнопка
# QLineEdit - Однострочное текстовое поле
# QTextEdit - Многострочное текстовое поле
# QCheckBox - Чекбокс(галочка)
# QRadioButton - Радиокнопка
# QComboBox - Выпадающий список
# QListWidget - Список
# QTableWidget - Таблица

#1
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
#
# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Пример PyQt6")
#
#         self.label = QLabel("Нажми на меня", self)
#
#         self.button = QPushButton("Нажми меня", self)
#         self.button.clicked.connect(self.on_click)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.label)
#         layout.addWidget(self.button)
#         self.setLayout(layout)
#
#     def on_click(self):
#         self.label.setText("Привет, PyQt6!")
#
# app = QApplication(sys.argv)
# window = MyApp()
# window.show()
# sys.exit(app.exec())

#2
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
#
# class InputApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Ввод текста")
#
#         self.input = QLineEdit(self)
#         self.label = QLabel("Введите что-то и нажмите кнопку", self)
#         self.button = QPushButton("Показать текст", self)
#         self.button.clicked.connect(self.show_text)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.input)
#         layout.addWidget(self.button)
#         layout.addWidget(self.label)
#         self.setLayout(layout)
#
#     def show_text(self):
#         text = self.input.text()
#         self.label.setText(f"Вы ввели: {text}")
#
# app = QApplication(sys.argv)
# window = InputApp()
# window.show()
# sys.exit(app.exec())

from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QCheckBox,
    QRadioButton, QComboBox, QLabel
)
import sys

class WidgetsDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Работа с несколькими виджетами")

        self.init_ui()
        self.init_connections()
        self.update_label()

    def init_ui(self):
        self.checkbox = QCheckBox("Согласен")
        self.checkbox.setToolTip("Отметьте, если согласны")

        self.radiobutton = QRadioButton("Выбери меня")
        self.radiobutton.setToolTip("Отметьте, чтобы выбрать")

        self.combobox = QComboBox()
        self.combobox.addItems(["Выбор 1", "Выбор 2", "Выбор 3"])
        self.combobox.setToolTip("Выберите один из вариантов")

        self.label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.checkbox)
        layout.addWidget(self.radiobutton)
        layout.addWidget(self.combobox)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def init_connections(self):
        self.checkbox.stateChanged.connect(self.update_label)
        self.radiobutton.toggled.connect(self.update_label)
        self.combobox.currentIndexChanged.connect(self.update_label)

    def update_label(self):
        parts = []

        if self.checkbox.isChecked():
            parts.append("☑ Согласен")
        else:
            parts.append("☐ Не согласен")

        if self.radiobutton.isChecked():
            parts.append("🔘 Радио: выбран")
        else:
            parts.append("⚪ Радио: не выбран")

        parts.append(f"📋 Выбор: {self.combobox.currentText()}")

        self.label.setText(" | ".join(parts))

app = QApplication(sys.argv)
window = WidgetsDemo()
window.show()
sys.exit(app.exec())
