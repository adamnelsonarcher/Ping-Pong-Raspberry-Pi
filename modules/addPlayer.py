import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class AddPlayerDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add New Player')

        self.layout = QVBoxLayout()

        self.name_label = QLabel('Player Name:')
        self.layout.addWidget(self.name_label)
        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_input)

        self.password_label = QLabel('Password:')
        self.layout.addWidget(self.password_label)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.password_input)

        self.add_button = QPushButton('Add Player')
        self.add_button.clicked.connect(self.accept)
        self.layout.addWidget(self.add_button)

        self.setLayout(self.layout)

    def get_player_data(self):
        return self.name_input.text().strip(), self.password_input.text()
