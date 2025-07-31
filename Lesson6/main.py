import sys
from PyQt6.QtWidgets import QApplication
from db import init_db
from app import App
from login import LoginWindow

def main():
    init_db()
    app = QApplication(sys.argv)

    main_window = {"app": None}

    def launch_app(user_role):
        main_window["app"] = App(user_role)
        main_window["app"].show()

    login = LoginWindow(on_success=launch_app)
    login.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()