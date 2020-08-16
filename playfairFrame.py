import sys
from strings import playfair_txt
from PyQt5.QtWidgets import (QWidget, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from PyQt5 import QtGui
from frameTemplate import frameTemplate
from ciphers.playfair import Playfair

class playfairFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.pf = Playfair()
        self.initUI()

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText(playfair_txt)
        self.cb_method.addItem("Encrypt")
        self.cb_method.addItem("Decrypt")
        self.cb_method.currentIndexChanged.connect(self.selectionChange)
        self.btn_encrypt.clicked.connect(self.encrypt)

        regex = QtCore.QRegExp("^[a-zA-Z]+$")
        validator = QtGui.QRegExpValidator(regex, self.plaintext)
        self.plaintext.setValidator(validator)

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
        if(self.validateInput()):
            text = self.pf.encrypt(self.plaintext.text())
            self.ciphertext.setText(text)
            self.plaintext.setPlaceholderText("")
            self.plaintext.setStyleSheet('QLineEdit { border-color: #1e1e1e }')

    def decrypt(self):
        if(self.validateInput()):
            text = self.pf.decrypt(self.plaintext.text())
            self.ciphertext.setText(text)
            self.plaintext.setPlaceholderText("")
            self.plaintext.setStyleSheet('QLineEdit { border-color: #1e1e1e }')

    def validateInput(self):
        if(self.plaintext.text() == ''):
            self.plaintext.setPlaceholderText("Input required")
            self.plaintext.setStyleSheet('QLineEdit { border-color: #EC0505 }')
            return False

        return True
