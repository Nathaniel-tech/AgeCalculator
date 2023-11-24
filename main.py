import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont
from datetime import datetime

class AgeCalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Age Calculator')
        self.setGeometry(300, 300, 400, 200)

        self.label_instruction = QLabel('Enter your birthdate:')
        self.label_instruction.setFont(QFont('Arial', 12))

        self.edit_year = QLineEdit()
        self.edit_year.setPlaceholderText('Year (e.g., 1990)')

        self.edit_month = QLineEdit()
        self.edit_month.setPlaceholderText('Month (1-12)')

        self.edit_day = QLineEdit()
        self.edit_day.setPlaceholderText('Day (1-31)')

        self.btn_calculate = QPushButton('Calculate Age', self)
        self.btn_calculate.clicked.connect(self.calculate_age)

        self.label_result = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label_instruction)
        layout.addWidget(self.edit_year)
        layout.addWidget(self.edit_month)
        layout.addWidget(self.edit_day)
        layout.addWidget(self.btn_calculate)
        layout.addWidget(self.label_result)

        self.setLayout(layout)

    def calculate_age(self):
        try:
            birth_year = int(self.edit_year.text())
            birth_month = int(self.edit_month.text())
            birth_day = int(self.edit_day.text())

            if not (1 <= birth_month <= 12) or not (1 <= birth_day <= 31):
                raise ValueError("Invalid month or day")

            birth_date = datetime(birth_year, birth_month, birth_day)
            current_date = datetime.now()

            age = (current_date - birth_date).days // 365
            self.label_result.setText(f'You are {age} years old.')

        except ValueError as e:
            self.label_result.setText(f'Error: {str(e)}. Please enter valid numbers.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AgeCalculatorApp()
    window.show()
    sys.exit(app.exec_())
