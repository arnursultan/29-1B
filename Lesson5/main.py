import sys
from PyQt6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from db import init_db, add_person, get_all_people
from main_ui import MainWindow

def run():
    app = QApplication(sys.argv)
    init_db()

    window = MainWindow()

    def show_message(title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec()

    def load_data():
        people = get_all_people()
        window.table.setRowCount(0)
        for row_num, row in enumerate(people):
            window.table.insertRow(row_num)
            for col_num, item in enumerate(row):
                window.table.setItem(row_num, col_num, QTableWidgetItem(str(item)))

    def on_add():
        name = window.name_input.text().strip()
        age_text = window.age_input.text().strip()

        if not name or not age_text:
            show_message("Ошибка", "Пожалуйста, заполните все поля.")
            return

        if not age_text.isdigit():
            show_message("Ошибка", "Возраст должен быть числом.")
            return

        age = int(age_text)
        if not (1 <= age <= 120):
            show_message("Ошибка", "Возраст должен быть от 1 до 120.")
            return

        try:
            add_person(name, age)
        except Exception as e:
            show_message("Ошибка", f"Ошибка при сохранении: {e}")
            return

        window.name_input.clear()
        window.age_input.clear()
        window.name_input.setFocus()
        load_data()

    window.add_button.clicked.connect(on_add)
    load_data()

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run()
