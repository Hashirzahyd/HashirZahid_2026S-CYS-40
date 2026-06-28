import sys
from PyQt5.QtWidgets import QApplication
import database
from login import LoginWindow

database.setup()
app = QApplication(sys.argv)
app.setStyleSheet("""
    QWidget { font-family: Segoe UI; font-size: 13px; color: #1c1c1e; background: white; }
    QPushButton { background: #6366f1; color: white; border-radius: 7px; padding: 6px 14px; font-weight: bold; border: none; }
    QPushButton:hover { background: #4f46e5; }
    QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox { border: 1px solid #e8e8ed; border-radius: 6px; padding: 5px 8px; background: #f8f8fa; }
    QLineEdit:focus { border: 1px solid #6366f1; background: white; }
    QTableWidget { background: white; border: 1px solid #e8e8ed; gridline-color: #f3f3f6; }
    QTableWidget::item:selected { background: #eef2ff; color: #4338ca; }
    QHeaderView::section { background: #f8f8fa; color: #6b6b6b; font-weight: bold; padding: 7px; border: none; border-bottom: 1px solid #e8e8ed; }
    QTabBar::tab { background: transparent; color: #a1a1aa; padding: 9px 20px; border-bottom: 2px solid transparent; }
    QTabBar::tab:selected { color: #6366f1; border-bottom: 2px solid #6366f1; font-weight: bold; }
    QTabWidget::pane { border: 1px solid #e8e8ed; }
    QDialog { background: white; }
""")
window = LoginWindow()
window.show()
sys.exit(app.exec_())