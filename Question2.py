import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class ColorChangingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Special midterm exam in OOP')
        self.setGeometry(150, 50, 400, 300)

        self.button = QPushButton('Click to change color', self)
        self.button.clicked.connect(self.changeColor)

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def changeColor(self):
        self.button.setStyleSheet('background-color: yellow')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ColorChangingApp()
    ex.show()
    sys.exit(app.exec_())
