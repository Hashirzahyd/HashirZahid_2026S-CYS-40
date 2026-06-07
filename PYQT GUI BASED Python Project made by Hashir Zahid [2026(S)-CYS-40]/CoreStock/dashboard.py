from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTabWidget, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import database

class Dashboard(QWidget):
    def __init__(self, user):
        super().__init__()
        self.user = user
        self.setWindowTitle("CoreStock")
        self.setMinimumSize(900, 560)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # header
        header = QFrame()
        header.setFixedHeight(54)
        header.setStyleSheet("background:#1c1c1e;")
        h = QHBoxLayout(header)
        h.setContentsMargins(16, 0, 16, 0)

        logo = QLabel("C")
        logo.setFixedSize(30, 30)
        logo.setAlignment(Qt.AlignCenter)
        logo.setFont(QFont("Segoe UI", 13, QFont.Bold))
        logo.setStyleSheet("background:#6366f1; color:white; border-radius:8px;")

        name = QLabel("CoreStock")
        name.setFont(QFont("Segoe UI", 13, QFont.Bold))
        name.setStyleSheet("color:white;")

        sub = QLabel("PC Store Management")
        sub.setStyleSheet("color:#555; font-size:11px;")

        who = QLabel(user[1] + "  |  " + user[3])
        who.setStyleSheet("color:#888; font-size:11px;")

        out = QPushButton("Logout")
        out.setFixedSize(68, 26)
        out.setStyleSheet("background:#6366f1; color:white; border-radius:6px; font-size:11px; border:none;")
        out.clicked.connect(self.logout)

        h.addWidget(logo)
        h.addSpacing(8)
        h.addWidget(name)
        h.addSpacing(6)
        h.addWidget(sub)
        h.addStretch()
        h.addWidget(who)
        h.addSpacing(10)
        h.addWidget(out)

        # stats
        stats = QFrame()
        stats.setFixedHeight(84)
        stats.setStyleSheet("background:#f8f8fa; border-bottom:1px solid #e8e8ed;")
        s = QHBoxLayout(stats)
        s.setContentsMargins(16, 10, 16, 10)
        s.setSpacing(10)

        prods = database.get_products()
        low   = database.get_low_stock()
        sups  = database.get_suppliers()
        units = sum(p[4] for p in prods)

        for title, val, color in [
            ("Products",    len(prods), "#6366f1"),
            ("Total Units", units,      "#1c1c1e"),
            ("Low Stock",   len(low),   "#ef4444"),
            ("Suppliers",   len(sups),  "#1c1c1e"),
        ]:
            card = QFrame()
            card.setStyleSheet("background:white; border-radius:9px; border:1px solid #e8e8ed;")
            cl = QVBoxLayout(card)
            cl.setContentsMargins(12, 6, 12, 6)
            n = QLabel(str(val))
            n.setFont(QFont("Segoe UI", 18, QFont.Bold))
            n.setStyleSheet(f"color:{color};")
            l = QLabel(title)
            l.setStyleSheet("color:#aaa; font-size:10px;")
            cl.addWidget(n)
            cl.addWidget(l)
            s.addWidget(card)

        # tabs
        tabs = QTabWidget()
        from products  import ProductsPage
        from stock     import StockPage
        from suppliers import SuppliersPage
        from reports   import ReportsPage
        tabs.addTab(ProductsPage(),  "Products")
        tabs.addTab(StockPage(),     "Stock In/Out")
        tabs.addTab(SuppliersPage(), "Suppliers")
        tabs.addTab(ReportsPage(),   "Reports")

        layout.addWidget(header)
        layout.addWidget(stats)
        layout.addWidget(tabs)
        self.setLayout(layout)

    def logout(self):
        from login import LoginWindow
        self.w = LoginWindow()
        self.w.show()
        self.close()