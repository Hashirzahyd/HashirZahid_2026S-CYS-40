from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                              QTableWidget, QTableWidgetItem, QDialog, QFormLayout,
                              QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt
import database

class SuppliersPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(14, 14, 14, 14)
        top = QHBoxLayout()
        top.addWidget(QLabel("Suppliers"))
        top.addStretch()
        b = QPushButton("+ Add Supplier")
        b.clicked.connect(self.add)
        top.addWidget(b)
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID","Name","Contact","Email"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addLayout(top)
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.load()

    def load(self):
        data = database.get_suppliers()
        self.table.setRowCount(0)
        for row in data:
            r = self.table.rowCount()
            self.table.insertRow(r)
            for c, v in enumerate(row):
                i = QTableWidgetItem(str(v or ""))
                i.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(r, c, i)

    def add(self):
        d = SupForm(self)
        if d.exec_(): self.load()

class SupForm(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Add Supplier")
        self.setFixedSize(300, 190)
        self.setStyleSheet("background:white;")
        layout = QFormLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        self.name    = QLineEdit()
        self.contact = QLineEdit()
        self.email   = QLineEdit()
        s = QPushButton("Save")
        s.clicked.connect(self.save)
        layout.addRow("Name:",    self.name)
        layout.addRow("Contact:", self.contact)
        layout.addRow("Email:",   self.email)
        layout.addRow(s)
        self.setLayout(layout)

    def save(self):
        if not self.name.text().strip():
            QMessageBox.warning(self, "!", "Name required!"); return
        database.add_supplier(self.name.text(), self.contact.text(), self.email.text())
        self.accept()