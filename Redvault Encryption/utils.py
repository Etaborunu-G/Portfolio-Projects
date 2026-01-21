# utils.py
from PySide6.QtWidgets import QMessageBox

def show_disclaimer(parent):
    msg = QMessageBox(parent)
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle("Important Notice")
    msg.setText(
        "This application ONLY supports text-based documents.\n\n"
        "Encrypting images, PDFs, Word files, or binaries may result "
        "in irreversible data loss.\n\n"
        "The application is NOT responsible for lost or corrupted data."
    )
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    return msg.exec() == QMessageBox.Ok
