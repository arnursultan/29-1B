from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QHBoxLayout, QComboBox
)
from db import check_user, create_user

class LoginWindow(QWidget):
    def __init__(self, on_success):
        super().__init__()
        self.setWindowTitle("Вход в систему")
        self.on_success = on_success

        self.layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Имя пользователя")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        login_btn = QPushButton("Войти")
        login_btn.clicked.connect(self.login)

        register_btn = QPushButton("Регистрация")
        register_btn.clicked.connect(self.open_register_window)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(login_btn)
        btn_layout.addWidget(register_btn)

        self.layout.addWidget(QLabel("Авторизация"))
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_input)
        self.layout.addLayout(btn_layout)

        self.setLayout(self.layout)

    def login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        ok, role = check_user(username, password)
        if ok:
            self.on_success(role)
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль.")

    def open_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Регистрация")
        self.resize(300, 180)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Новый логин")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Новый пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.role_box = QComboBox()
        self.role_box.addItems(["user", "admin"])

        register_btn = QPushButton("Создать пользователя")
        register_btn.clicked.connect(self.register)

        layout.addWidget(QLabel("Регистрация нового пользователя"))
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(QLabel("Роль:"))
        layout.addWidget(self.role_box)
        layout.addWidget(register_btn)

        self.setLayout(layout)

    def register(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()
        role = self.role_box.currentText()

        success, message = create_user(username, password, role)
        if success:
            QMessageBox.information(self, "Успешно", message)
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", message)
