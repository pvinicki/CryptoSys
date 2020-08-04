# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import (QWidget, QCheckBox, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from frameTemplate import frameTemplate
import ciphers.vigenere as vg


class vigenereFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText('Supstitucijska šifra elemente p otvorenog teksta zamjenjuje (supstituira) elementima šifrata c ovisno o ključu k. Element otvorenog teksta može biti slovo (znak) ili niz slova (znakova). ')

        self.cb_method.addItem("Encrypt")
        self.cb_method.addItem("Decrypt")
        self.cb_method.currentIndexChanged.connect(self.selectionChange)
        self.btn_encrypt.clicked.connect(self.encrypt)

        self.label_key = QLabel()
        self.label_key.setText('Ključ:')

        self.key_input = QLineEdit(self)

        self.checkbox_autokey = QCheckBox("Autokey")
        self.checkbox_autokey.setChecked(False)
        self.checkbox_autokey.stateChanged.connect(self.stateChange)

        self.encryption_v_box.addWidget(self.label_key)
        self.encryption_v_box.addWidget(self.key_input)
        self.encryption_v_box.addWidget(self.checkbox_autokey)

    def selectionChange(self, index):
        if (self.cb_method.itemText(index) == "Encrypt"):
            self.label_plaintext.setText("Plaintext:")
            self.label_ciphertext.setText("Ciphertext:")

            if(self.checkbox_autokey.isChecked()):
                self.btn_encrypt.clicked.connect(self.autokeyEncrypt)
            else:
                self.btn_encrypt.clicked.connect(self.encrypt)

            self.btn_encrypt.setText("Encrypt")
            self.plaintext.clear()
            self.ciphertext.clear()

        elif (self.cb_method.itemText(index) == "Decrypt"):
            self.label_plaintext.setText("Ciphertext:")
            self.label_ciphertext.setText("Plaintext:")

            if(self.checkbox_autokey.isChecked()):
                self.btn_encrypt.clicked.connect(self.autokeyDecrypt)
            else:
                self.btn_encrypt.clicked.connect(self.decrypt)

            self.btn_encrypt.setText("Decrypt")
            self.plaintext.clear()
            self.ciphertext.clear()

    def stateChange(self):
        if(self.checkbox_autokey.isChecked()):
            if (str(self.cb_method.currentText()) == "Encrypt"):
                self.btn_encrypt.clicked.connect(self.autokeyEncrypt)
            else:
                self.btn_encrypt.clicked.connect(self.autokeyDecrypt)

        else:
            if (str(self.cb_method.currentText()) == "Encrypt"):
                self.btn_encrypt.clicked.connect(self.encrypt)
            else:
                self.btn_encrypt.clicked.connect(self.decrypt)

    def encrypt(self):
        text = vg.encrypt(self.plaintext.text(), self.key_input.text())
        self.ciphertext.setText(text)

    def decrypt(self):
        text = vg.decrypt(self.plaintext.text(), self.key_input.text())
        self.ciphertext.setText(text)

    def autokeyEncrypt(self):
        text = vg.autokeyEncrypt(self.plaintext.text(), self.key_input.text())
        self.ciphertext.setText(text)

    def autokeyDecrypt(self):
        pass

