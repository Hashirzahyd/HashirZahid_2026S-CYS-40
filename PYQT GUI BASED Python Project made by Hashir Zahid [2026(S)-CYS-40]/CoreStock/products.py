from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                              QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox,
                              QDialog, QFormLayout, QComboBox, QSpinBox, QDoubleSpinBox)
from PyQt5.QtCore import Qt
import database

class ProductsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(14, 14, 14, 14)

        top = QHBoxLayout()
        top.addWidget(QLabel("Products"))
        top.addStretch()
        a = QPushButton("+ Add Product")
        a.clicked.connect(self.add)
        top.addWidget(a)

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search...")
        self.search.textChanged.connect(self.do_search)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID","Name","Category","Price","Qty","Low Limit"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)

        bot = QHBoxLayout()
        bot.addStretch()
        e = QPushButton("Edit")
        e.clicked.connect(self.edit)
        d = QPushButton("Delete")
        d.setStyleSheet("background:#ef4444; color:white; border-radius:7px; padding:6px 14px; font-weight:bold; border:none;")
        d.clicked.connect(self.delete)
        bot.addWidget(e)
        bot.addWidget(d)

        layout.addLayout(top)
        layout.addWidget(self.search)
        layout.addWidget(self.table)
        layout.addLayout(bot)
        self.setLayout(layout)
        self.load()

    def load(self):
        self.fill(database.get_products())

    def fill(self, data):
        self.table.setRowCount(0)
        for row in data:
            r = self.table.rowCount()
            self.table.insertRow(r)
            for c, v in enumerate(row):
                i = QTableWidgetItem(str(v or ""))
                i.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(r, c, i)

    def do_search(self):
        w = self.search.text().lower()
        self.fill([p for p in database.get_products() if w in p[1].lower() or w in (p[2] or "").lower()])

    def add(self):
        d = PForm(self)
        if d.exec_(): self.load()

    def edit(self):
        row = self.table.currentRow()
        if row == -1:
            QMessageBox.warning(self, "!", "Select a product first!"); return
        data = [self.table.item(row, i).text() for i in range(6)]
        d = PForm(self, data)
        if d.exec_(): self.load()

    def delete(self):
        row = self.table.currentRow()
        if row == -1:
            QMessageBox.warning(self, "!", "Select a product first!"); return
        pid  = int(self.table.item(row, 0).text())
        name = self.table.item(row, 1).text()
        if QMessageBox.question(self, "Delete?", f"Delete '{name}'?") == QMessageBox.Yes:
            database.delete_product(pid)
            self.load()

class PForm(QDialog):
    def __init__(self, parent, data=None):
        super().__init__(parent)
        self.data = data
        self.setWindowTitle("Add Product" if not data else "Edit Product")
        self.setFixedSize(320, 290)
        self.setStyleSheet("background:white;")
        layout = QFormLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        self.name  = QLineEdit()
        self.cat   = QComboBox()
        self.cat.addItems(["GPU","CPU","RAM","Monitor","Storage","Motherboard","Keyboard","Mouse","Other"])
        self.price = QDoubleSpinBox()
        self.price.setMaximum(999999)
        self.qty   = QSpinBox()
        self.qty.setMaximum(99999)
        self.low   = QSpinBox()
        self.low.setValue(5)
        if data:
            self.name.setText(data[1])
            self.cat.setCurrentText(data[2])
            self.price.setValue(float(data[3] or 0))
            self.qty.setValue(int(data[4] or 0))
            self.low.setValue(int(data[5] or 5))
        layout.addRow("Name:",     self.name)
        layout.addRow("Category:", self.cat)
        layout.addRow("Price:",    self.price)
        layout.addRow("Quantity:", self.qty)
        layout.addRow("Low Alert:",self.low)
        s = QPushButton("Save")
        s.clicked.connect(self.save)
        layout.addRow(s)
        self.setLayout(layout)

    def save(self):
        if not self.name.text().strip():
            QMessageBox.warning(self, "!", "Name is required!"); return
        if self.data:
            database.update_product(int(self.data[0]), self.name.text(), self.cat.currentText(), self.price.value(), self.qty.value(), self.low.value())
        else:
            database.add_product(self.name.text(), self.cat.currentText(), self.price.value(), self.qty.value(), self.low.value())
        self.accept()