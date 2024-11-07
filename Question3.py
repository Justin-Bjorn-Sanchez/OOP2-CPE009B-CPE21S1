import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class NameDisplayApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Midterm in OOP")
        self.setGeometry(100, 100, 400, 200)
        self.initUI()

    def initUI(self):
        self.prompt_label = QLabel("Enter your fullname:", self)
        self.prompt_label.setStyleSheet("color: red;")

        self.input_field = QLineEdit(self)

        self.display_button = QPushButton("Click to display your Fullname", self)
        self.display_button.setStyleSheet("color: red;")
        self.display_button.clicked.connect(self.display_name)

        self.output_field = QLineEdit(self)
        self.output_field.setReadOnly(True)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.prompt_label)
        input_layout.addWidget(self.input_field)

        display_layout = QVBoxLayout()
        display_layout.addWidget(self.display_button)
        display_layout.addWidget(self.output_field)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(display_layout)

        self.setLayout(main_layout)

    def display_name(self):
        full_name = self.input_field.text()
        self.output_field.setText(full_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = NameDisplayApp()
    window.show()
    sys.exit(app.exec_())
