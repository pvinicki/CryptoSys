# This Python file uses the following encoding: utf-8
import sys
from strings import transposition_txt
from PyQt5.QtWidgets import (QWidget, QCheckBox, QMessageBox, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from PyQt5 import QtGui
from frameTemplate import frameTemplate
from ciphers.transposition import Transposition


class transpositionFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.ts = Transposition()
        self.initUI()

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText(transposition_txt)

        self.cb_method.addItem("Encrypt")
        self.cb_method.addItem("Decrypt")
        self.cb_method.currentIndexChanged.connect(self.selectionChange)
        self.btn_encrypt.clicked.connect(self.encrypt)

        regex = QtCore.QRegExp("^[a-zA-Z]+$")
        validator = QtGui.QRegExpValidator(regex, self.plaintext)
        self.plaintext.setValidator(validator)

        self.label_key = QLabel()
        self.label_key.setText('Ključ:')

        self.key_input = QLineEdit(self)
        self.key_input.setInputMask('D,D,D,d,d;_')

        self.encryption_v_box.addWidget(self.label_key)
        self.encryption_v_box.addWidget(self.key_input)

    def selectionChange(self, index):
        self.btn_encrypt.clicked.disconnect()

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
        if(self.validateInput() and self.validateKey()):
            text = self.ts.encrypt(self.plaintext.text(), self.key)
            self.ciphertext.setText(text)
            self.plaintext.setStyleSheet('QLineEdit { border-color: #1e1e1e }')

    def decrypt(self):
        if(self.validateInput() and self.validateKey()):
            text = self.ts.decrypt(self.plaintext.text(), self.key)
            self.ciphertext.setText(text)
            self.plaintext.setStyleSheet('QLineEdit { border-color: #1e1e1e }')

    def validateInput(self):
        if(self.plaintext.text() == ''):
            self.plaintext.setPlaceholderText("Input required")
            self.plaintext.setStyleSheet('QLineEdit { border-color: #EC0505 }')
            return False

        return True

    def validateKey(self):
        self.key = []
        self.buffer = (self.key_input.text()).split(',')

        for element in self.buffer:
            if(element != ''):
                self.key.append(element)

        for element in self.key:
            self.key[self.key.index(element)] = int(element)

        print(self.key)
        for element in range(1, len(self.key) + 1):
            if element not in self.key:
                self.showWarning()
                return False

        return True

    def showWarning(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Invalid key")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.show()


