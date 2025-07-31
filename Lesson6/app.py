from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLineEdit, QTableWidget, QTableWidgetItem,
    QMessageBox, QSpinBox, QLabel, QFileDialog
)
from db import get_all, search_by_name, delete_by_id, add_person
from utils import export_to_csv

class App(QWidget):
    def __init__(self, user_role):
        super().__init__()
        self.user_role = user_role
        self.setWindowTitle(f"CRUD: Панель управления ({self.user_role})")
        self.resize(700, 450)

        self.layout = QVBoxLayout()

        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск по имени")
        search_btn = QPushButton("🔍 Найти")
        search_btn.clicked.connect(self.search)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_btn)

        self.layout.addLayout(search_layout)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Имя", "Возраст"])
        self.table.setSortingEnabled(True)
        self.layout.addWidget(self.table)

        form_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя")
        self.age_input = QSpinBox()
        self.age_input.setRange(0, 150)
        add_btn = QPushButton("➕ Добавить")
        add_btn.clicked.connect(self.add_record)
        form_layout.addWidget(QLabel("Имя:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Возраст:"))
        form_layout.addWidget(self.age_input)
        form_layout.addWidget(add_btn)

        self.layout.addLayout(form_layout)

        btn_layout = QHBoxLayout()

        self.delete_btn = QPushButton("🗑 Удалить выбранное")
        self.delete_btn.clicked.connect(self.delete_selected)
        if self.user_role != "admin":
            self.delete_btn.hide()

        export_btn = QPushButton("📁 Экспорт CSV")
        export_btn.clicked.connect(self.export_csv)

        btn_layout.addWidget(self.delete_btn)
        btn_layout.addWidget(export_btn)

        self.layout.addLayout(btn_layout)

        self.setLayout(self.layout)
        self.load_data()

    def load_data(self, data=None):
        records = data if data else get_all()
        self.table.setRowCount(0)

        for row_idx, (pid, name, age) in enumerate(records):
            self.table.insertRow(row_idx)
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(pid)))
            self.table.setItem(row_idx, 1, QTableWidgetItem(name))
            self.table.setItem(row_idx, 2, QTableWidgetItem(str(age)))

    def search(self):
        name = self.search_input.text()
        if name:
            data = search_by_name(name)
            self.load_data(data)
        else:
            self.load_data()

    def delete_selected(self):
        if self.user_role != "admin":
            QMessageBox.warning(self, "Доступ запрещён", "Удаление доступно только администратору.")
            return

        row = self.table.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления.")
            return
        pid = int(self.table.item(row, 0).text())
        confirm = QMessageBox.question(
            self, "Удаление",
            f"Удалить запись ID {pid}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirm == QMessageBox.StandardButton.Yes:
            delete_by_id(pid)
            self.load_data()

    def add_record(self):
        name = self.name_input.text().strip()
        age = self.age_input.value()
        if not name:
            QMessageBox.warning(self, "Ошибка", "Имя не может быть пустым.")
            return
        add_person(name, age)
        self.name_input.clear()
        self.age_input.setValue(0)
        self.load_data()

    def export_csv(self):
        path, _ = QFileDialog.getSaveFileName(self, "Сохранить CSV", "", "CSV Files (*.csv)")
        if path:
            export_to_csv(path)
            QMessageBox.information(self, "Успешно", f"Файл сохранён: {path}")
