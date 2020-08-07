import sys
sys.path.append("resources")
from strings import onetimepad_txt
from PyQt5.QtWidgets import (QWidget, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from frameTemplate import frameTemplate
import ciphers.onetimepad as otp

class onetimepadFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText(onetimepad_txt)

        self.cb_method.addItem("Encrypt")
        self.btn_encrypt.clicked.connect(self.encrypt)


    def encrypt(self):
        text = otp.encrypt(self.plaintext.text())
        self.ciphertext.setText(text)
