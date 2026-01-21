# ui/encrypt_tab.py
from PySide6.QtWidgets import *
from crypto.engine import encrypt_file

class EncryptTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        warning = QLabel(
            "⚠️ TEXT FILES ONLY (.txt, .md, .csv). "
            "Using other formats may permanently destroy data."
        )
        warning.setStyleSheet("color:#ff6b6b; font-weight:bold;")
        layout.addWidget(warning)

        self.file = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)

        self.output = QLineEdit()
        self.key_display = QLineEdit()
        self.key_display.setReadOnly(True)

        btn = QPushButton("Encrypt")
        btn.setObjectName("primary")
        btn.clicked.connect(self.encrypt)

        layout.addWidget(QLabel("Input File"))
        layout.addWidget(self.file)
        layout.addWidget(QLabel("Password"))
        layout.addWidget(self.password)
        layout.addWidget(QLabel("Output File (.enc)"))
        layout.addWidget(self.output)
        layout.addWidget(btn)
        layout.addWidget(QLabel("Backup Recovery Key"))
        layout.addWidget(self.key_display)

    def encrypt(self):
        key = encrypt_file(
            self.file.text(),
            self.output.text(),
            self.password.text()
        )
        self.key_display.setText(key)
