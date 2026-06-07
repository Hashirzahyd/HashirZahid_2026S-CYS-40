from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                              QTableWidget, QTableWidgetItem, QDialog, QFormLayout,
                              QComboBox, QSpinBox, QMessageBox)
from PyQt5.QtCore import Qt
from datetime import date
import database

class StockPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(14, 14, 14, 14)
        top = QHBoxLayout()
        top.addWidget(QLabel("Stock In / Out"))
        top.addStretch()
        b = QPushButton("+ Record Movement")
        b.clicked.connect(self.record)
        top.addWidget(b)
        low = database.get_low_stock()
        if low:
            alert = QLabel("⚠  Low Stock: " + ", ".join(p[1] for p in low))
            alert.setStyleSheet("background:#fef2f2; color:#dc2626; border:1px solid #fca5a5; border-radius:6px; padding:7px;")
        else:
            alert = QLabel("✓  All stock levels are fine")
            alert.setStyleSheet("background:#f0fdf4; color:#16a34a; border:1px solid #86efac; border-radius:6px; padding:7px;")
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID","Product","Type","Qty","Date"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addLayout(top)
        layout.addWidget(alert)
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.load()

    def load(self):
        data = database.get_movements()
        self.table.setRowCount(0)
        for row in data:
            r = self.table.rowCount()
            self.table.insertRow(r)
            for c, v in enumerate(row):
                i = QTableWidgetItem(str(v or ""))
                i.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(r, c, i)

    def record(self):
        d = SForm(self)
        if d.exec_(): self.load()

class SForm(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Record Movement")
        self.setFixedSize(300, 200)
        self.setStyleSheet("background:white;")
        layout = QFormLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        self.product = QComboBox()
        self.products = database.get_products()
        for p in self.products:
            self.product.addItem(f"{p[1]} (qty:{p[4]})", p[1])
        self.mtype = QComboBox()
        self.mtype.addItems(["IN","OUT"])
        self.qty = QSpinBox()
        self.qty.setMinimum(1)
        self.qty.setMaximum(9999)
        s = QPushButton("Save")
        s.clicked.connect(self.save)
        layout.addRow("Product:", self.product)
        layout.addRow("Type:",    self.mtype)
        layout.addRow("Qty:",     self.qty)
        layout.addRow(s)
        self.setLayout(layout)

    def save(self):
        name = self.product.currentData()
        move = self.mtype.currentText()
        qty  = self.qty.value()
        if move == "OUT":
            p = next((x for x in self.products if x[1] == name), None)
            if p and p[4] < qty:
                QMessageBox.warning(self, "!", f"Only {p[4]} in stock!"); return
        database.add_movement(name, move, qty, str(date.today()))
        self.accept()