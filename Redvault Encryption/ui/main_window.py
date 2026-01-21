# ui/main_window.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTabWidget
from ui.encrypt_tab import EncryptTab
from ui.decrypt_tab import DecryptTab

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RedVault Encryption")
        self.resize(800, 500)

        tabs = QTabWidget()
        tabs.addTab(EncryptTab(), "Encrypt")
        tabs.addTab(DecryptTab(), "Decrypt")

        layout = QVBoxLayout(self)
        layout.addWidget(tabs)
