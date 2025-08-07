import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox,
    QFileDialog, QLineEdit, QFontDialog
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from database import init_db, get_data, update_data, reset_all

class HamsterClicker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🐹 Hamster Combat Кликер")
        self.resize(400, 520)

        init_db()
        self.score, self.image_path, self.label_text = get_data()

        self.layout = QVBoxLayout()

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.set_image(self.image_path)
        self.layout.addWidget(self.image_label)

        self.label = QLabel(f"{self.label_text}: {self.score}")
        self.label.setFont(QFont("Arial", 18))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        self.hit_button = QPushButton("👊 Ударить хомяка!")
        self.hit_button.setFont(QFont("Arial", 16))
        self.hit_button.clicked.connect(self.hit)
        self.layout.addWidget(self.hit_button)

        self.text_input = QLineEdit()
        self.text_input.setPlaceholderText("Изменить название счётчика")
        self.text_input.returnPressed.connect(self.change_label_text)
        self.layout.addWidget(self.text_input)

        photo_btn = QPushButton("🖼 Загрузить фото")
        photo_btn.clicked.connect(self.load_image)
        self.layout.addWidget(photo_btn)

        font_btn = QPushButton("🖋 Изменить шрифт")
        font_btn.clicked.connect(self.change_font)
        self.layout.addWidget(font_btn)

        reset_btn = QPushButton("♻️ Сбросить всё")
        reset_btn.clicked.connect(self.reset)
        self.layout.addWidget(reset_btn)

        self.setLayout(self.layout)

    def set_image(self, path):
        if path:
            pixmap = QPixmap(path)
            if not pixmap.isNull():
                self.image_label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
            else:
                self.image_label.setText("⚠️ Не удалось загрузить изображение")
        else:
            self.image_label.setText("🖼 Нет изображения")

    def hit(self):
        self.score += 1
        update_data(score=self.score)
        self.label.setText(f"{self.label_text}: {self.score}")

    def change_label_text(self):
        new_text = self.text_input.text().strip()
        if new_text:
            self.label_text = new_text
            update_data(label_text=new_text)
            self.label.setText(f"{self.label_text}: {self.score}")
            self.text_input.clear()

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Выбери картинку", "", "Images (*.png *.jpg *.jpeg *.gif)")
        if path:
            self.image_path = path
            update_data(image_path=path)
            self.set_image(path)

    def change_font(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.label.setFont(font)
            self.hit_button.setFont(font)
            self.text_input.setFont(font)

    def reset(self):
        reply = QMessageBox.question(self, "Сброс", "Сбросить весь прогресс?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            reset_all()
            self.score, self.image_path, self.label_text = get_data()
            self.label.setText(f"{self.label_text}: {self.score}")
            self.set_image(self.image_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HamsterClicker()
    window.show()
    sys.exit(app.exec())
