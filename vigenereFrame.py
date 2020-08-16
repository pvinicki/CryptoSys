# This Python file uses the following encoding: utf-8
import sys
import os
from strings import vigenere_txt
from PyQt5.QtWidgets import (QWidget, QCheckBox, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from PyQt5 import QtGui
from frameTemplate import frameTemplate
from ciphers.vigenere import Vigenere


class vigenereFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.vg = Vigenere()
        self.initUI()

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText(vigenere_txt)

        self.cb_method.addItem("Encrypt")
        self.cb_method.addItem("Decrypt")
        self.cb_method.currentIndexChanged.connect(self.selectionChange)
        self.btn_encrypt.clicked.connect(self.encrypt)

        self.label_key = QLabel()
        self.label_key.setText('Ključ:')

        self.key_input = QLineEdit(self)

        regex = QtCore.QRegExp("^[a-zA-Z]+$")
        validator = QtGui.QRegExpValidator(regex, self.key_input)
        self.key_input.setValidator(validator)

        text_validator = QtGui.QRegExpValidator(regex, self.plaintext)
        self.plaintext.setValidator(validator)

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
                self.btn_encrypt.clicked.disconnect()
                self.btn_encrypt.clicked.connect(self.autokeyEncrypt)
            else:
                self.btn_encrypt.clicked.disconnect()
                self.btn_encrypt.clicked.connect(self.encrypt)

            self.btn_encrypt.setText("Encrypt")
            self.plaintext.clear()
            self.ciphertext.clear()

        elif (self.cb_method.itemText(index) == "Decrypt"):
            self.label_plaintext.setText("Ciphertext:")
            self.label_ciphertext.setText("Plaintext:")

            if(self.checkbox_autokey.isChecked()):
                self.btn_encrypt.clicked.disconnect()
                self.btn_encrypt.clicked.connect(self.autokeyDecrypt)
            else:
                self.btn_encrypt.clicked.disconnect()
                self.btn_encrypt.clicked.connect(self.decrypt)

            self.btn_encrypt.setText("Decrypt")
            self.plaintext.clear()
            self.ciphertext.clear()

    def stateChange(self):
        self.btn_encrypt.clicked.disconnect()

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
        if(self.validateKey()):
            text = self.vg.encrypt(self.plaintext.text(), self.key_input.text())
            self.ciphertext.setText(text)
            self.key_input.setStyleSheet('QLineEdit { border-color: #1e1e1e }')

    def decrypt(self):
        if(self.validateKey()):
            text = self.vg.decrypt(self.plaintext.text(), self.key_input.text())
            self.ciphertext.setText(text)
            self.key_input.setStyleSheet('QLineEdit { border-color: #1e1e1e }')

    def autokeyEncrypt(self):
        if(self.validateKey()):
            text = self.vg.autokeyEncrypt(self.plaintext.text(), self.key_input.text())
            self.ciphertext.setText(text)
            self.key_input.setStyleSheet('QLineEdit { border-color: #1e1e1e }')

    def validateKey(self):
        if(self.key_input.text() == ''):
            self.key_input.setPlaceholderText("Key is required")
            self.key_input.setStyleSheet('QLineEdit { border-color: #EC0505 }')
            return False

        return True

    def autokeyDecrypt(self):
        if(self.validateKey()):
            text = self.vg.autokeyDecrypt(self.plaintext.text(), self.key_input.text())
            self.ciphertext.setText(text)
            self.key_input.setStyleSheet('QLineEdit { border-color: #1e1e1e }')

