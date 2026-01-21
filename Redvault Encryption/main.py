# main.py
import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow
from style import DARK_RED_THEME
from utils import show_disclaimer

app = QApplication(sys.argv)
app.setStyleSheet(DARK_RED_THEME)

window = MainWindow()

if not show_disclaimer(window):
    sys.exit(0)

window.show()
sys.exit(app.exec())
