# ui/decrypt_tab.py
from PySide6.QtWidgets import *
from crypto.engine import (
    decrypt_with_password,
    decrypt_with_backup_key
)

class DecryptTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.enc = QLineEdit()
        self.out = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.backup = QLineEdit()

        layout.addWidget(QLabel("Encrypted File"))
        layout.addWidget(self.enc)

        layout.addWidget(QLabel("Password (leave blank if forgotten)"))
        layout.addWidget(self.password)

        layout.addWidget(QLabel("Backup Recovery Key"))
        layout.addWidget(self.backup)

        layout.addWidget(QLabel("Output File"))
        layout.addWidget(self.out)

        btn = QPushButton("Decrypt")
        btn.setObjectName("primary")
        btn.clicked.connect(self.decrypt)

        layout.addWidget(btn)

    def decrypt(self):
        if self.password.text():
            decrypt_with_password(
                self.enc.text(),
                self.out.text(),
                self.password.text()
            )
        else:
            decrypt_with_backup_key(
                self.enc.text(),
                self.out.text(),
                self.backup.text()
            )
