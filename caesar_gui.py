import sys
from strings import caesar_txt
from PyQt5.QtWidgets import (QWidget, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from PyQt5 import QtGui
from frameTemplate import frameTemplate
from ciphers.caesar import Caesar

class caesarFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.cs = Caesar()
        self.initUI()

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText(caesar_txt)

        self.cb_method.addItem("Encrypt")
        self.cb_method.addItem("Decrypt")
        self.cb_method.currentIndexChanged.connect(self.selectionChange)

        regex = QtCore.QRegExp("^[a-zA-Z]+$")
        validator = QtGui.QRegExpValidator(regex, self.plaintext)
        self.plaintext.setValidator(validator)

        self.btn_encrypt.clicked.connect(self.encrypt)

    def selectionChange(self, index):
        self.btn_encrypt.clicked.disconnect()

        if (self.cb_method.itemText(index) == "Encrypt"):
            self.label_plaintext.setText("Plaintext:")
            self.label_ciphertext.setText("Ciphertext:")
            self.btn_encrypt.clicked.connect(self.encrypt)
            self.btn_encrypt.setText("Encrypt")
            self.plaintext.clear()
            self.ciphertext.clear()

        elif(self.cb_method.itemText(index) == "Decrypt"):
            self.label_plaintext.setText("Ciphertext:")
            self.label_ciphertext.setText("Plaintext:")
            self.btn_encrypt.clicked.connect(self.decrypt)
            self.btn_encrypt.setText("Decrypt")
            self.plaintext.clear()
            self.ciphertext.clear()

    def encrypt(self):
        text = self.cs.encrypt(self.plaintext.text())
        self.ciphertext.setText(text)

    def decrypt(self):
        text = self.cs.decrypt(self.plaintext.text())
        self.ciphertext.setText(text)
