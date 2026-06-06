import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 300, 200)

        self.label_user = QLabel("Username:")
        self.input_user = QLineEdit()

        self.label_pass = QLabel("Password:")
        self.input_pass = QLineEdit()
        self.input_pass.setEchoMode(QLineEdit.Password)

        self.btn = QPushButton("LOGIN")
        self.btn.clicked.connect(self.check_login)

        layout = QVBoxLayout()
        layout.addWidget(self.label_user)
        layout.addWidget(self.input_user)
        layout.addWidget(self.label_pass)
        layout.addWidget(self.input_pass)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def check_login(self):
        user = self.input_user.text()
        pwd = self.input_pass.text()
        if user == "Hashir" and pwd == "1234":
            QMessageBox.information(self, "Success", "Login successful!")
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials.")

app = QApplication(sys.argv)
window = LoginWindow()
window.show()
sys.exit(app.exec_())
