from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QTableWidget, QTableWidgetItem
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Урок 5: Добавление и Получение")
        self.setMinimumWidth(450)

        self.name_label = QLabel("Имя:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Введите имя")

        self.age_label = QLabel("Возраст:")
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Введите возраст (1–120)")

        self.age_input.returnPressed.connect(self.add_button_clicked)

        self.add_button = QPushButton("Добавить")

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Имя", "Возраст"])
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.table.setColumnWidth(0, 40)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 80)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def add_button_clicked(self):
        self.add_button.click()
