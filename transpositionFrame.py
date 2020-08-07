# This Python file uses the following encoding: utf-8
import sys
sys.path.append("resources")
from strings import transposition_txt
from PyQt5.QtWidgets import (QWidget, QCheckBox, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from frameTemplate import frameTemplate
import ciphers.transposition as ts


class transpositionFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText(transposition_txt)

        self.cb_method.addItem("Encrypt")
        self.cb_method.addItem("Decrypt")
        self.cb_method.currentIndexChanged.connect(self.selectionChange)
        self.btn_encrypt.clicked.connect(self.encrypt)

        self.label_key = QLabel()
        self.label_key.setText('Ključ:')

        self.key_input = QLineEdit(self)

        self.encryption_v_box.addWidget(self.label_key)
        self.encryption_v_box.addWidget(self.key_input)

    def selectionChange(self, index):
        if (self.cb_method.itemText(index) == "Encrypt"):
            self.label_plaintext.setText("Plaintext:")
            self.label_ciphertext.setText("Ciphertext:")
            self.btn_encrypt.clicked.connect(self.encrypt)
            self.btn_encrypt.setText("Encrypt")
            self.plaintext.clear()
            self.ciphertext.clear()

        elif (self.cb_method.itemText(index) == "Decrypt"):
            self.label_plaintext.setText("Ciphertext:")
            self.label_ciphertext.setText("Plaintext:")
            self.btn_encrypt.clicked.connect(self.decrypt)
            self.btn_encrypt.setText("Decrypt")
            self.plaintext.clear()
            self.ciphertext.clear()

    def encrypt(self):
        text = ts.encrypt(self.plaintext.text(), self.key_input.text())
        self.ciphertext.setText(text)

    def decrypt(self):
        text = ts.decrypt(self.plaintext.text(), self.key_input.text())
        self.ciphertext.setText(text)

