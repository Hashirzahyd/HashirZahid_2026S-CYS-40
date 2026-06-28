from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import database

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CoreStock")
        self.setFixedSize(380, 450)
        self.setStyleSheet("background: white;")

        layout = QVBoxLayout()
        layout.setContentsMargins(45, 35, 45, 35)
        layout.setSpacing(10)

        logo = QLabel("C")
        logo.setFixedSize(50, 50)
        logo.setAlignment(Qt.AlignCenter)
        logo.setFont(QFont("Segoe UI", 20, QFont.Bold))
        logo.setStyleSheet("background:#6366f1; color:white; border-radius:12px;")

        title = QLabel("CoreStock")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))

        sub = QLabel("PC Store Management System")
        sub.setAlignment(Qt.AlignCenter)
        sub.setStyleSheet("color:#a1a1aa; font-size:12px;")

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("background:#e8e8ed;")
        line.setFixedHeight(1)

        self.username = QLineEdit()
        self.username.setPlaceholderText("Username")
        self.username.setFixedHeight(40)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setFixedHeight(40)

        btn = QPushButton("Login")
        btn.setFixedHeight(42)
        btn.setStyleSheet("background:#6366f1; color:white; border-radius:7px; font-size:13px; font-weight:bold; border:none;")
        btn.clicked.connect(self.do_login)

        hint = QLabel("admin / admin123")
        hint.setAlignment(Qt.AlignCenter)
        hint.setStyleSheet("color:#ccc; font-size:11px;")

        layout.addWidget(logo, alignment=Qt.AlignCenter)
        layout.addWidget(title)
        layout.addWidget(sub)
        layout.addWidget(line)
        layout.addSpacing(5)
        layout.addWidget(self.username)
        layout.addWidget(self.password)
        layout.addSpacing(8)
        layout.addWidget(btn)
        layout.addWidget(hint)
        self.setLayout(layout)

    def do_login(self):
        u = self.username.text().strip()
        p = self.password.text().strip()
        user = database.check_login(u, p)
        if user:
            from dashboard import Dashboard
            self.dash = Dashboard(user)
            self.dash.show()
            self.close()
        else:
            QMessageBox.warning(self, "Error", "Wrong username or password!")