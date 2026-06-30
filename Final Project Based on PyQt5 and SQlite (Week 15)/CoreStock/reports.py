from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
                              QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt
import database

class ReportsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(14, 14, 14, 14)
        top = QHBoxLayout()
        top.addWidget(QLabel("Stock Report"))
        top.addStretch()
        e = QPushButton("Export CSV")
        e.clicked.connect(self.export)
        top.addWidget(e)
        data = database.get_movements()
        tin  = sum(m[3] for m in data if m[2] == "IN")
        tout = sum(m[3] for m in data if m[2] == "OUT")
        summary = QLabel(f"Total IN: {tin}   |   Total OUT: {tout}   |   Transactions: {len(data)}")
        summary.setStyleSheet("background:#f8f8fa; border:1px solid #e8e8ed; border-radius:6px; padding:8px; color:#444;")
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID","Product","Type","Qty","Date"])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addLayout(top)
        layout.addWidget(summary)
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

    def export(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save", "report.csv", "CSV (*.csv)")
        if path:
            data = database.get_movements()
            with open(path, "w") as f:
                f.write("ID,Product,Type,Qty,Date\n")
                for row in data:
                    f.write(",".join(str(x or "") for x in row) + "\n")
            QMessageBox.information(self, "Done", "Saved!")