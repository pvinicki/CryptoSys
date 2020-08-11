# This Python file uses the following encoding: utf-8
from strings import des_txt
from PyQt5.QtWidgets import (QWidget, QCheckBox, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from PyQt5 import QtGui
from frameTemplate import frameTemplate
import ciphers.DES as des


class desFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText(des_txt)

        self.cb_method.addItem("Encrypt")
        self.cb_method.addItem("Decrypt")
        self.cb_method.currentIndexChanged.connect(self.selectionChange)

        #input data type
        self.checkbox_text = QCheckBox()
        self.checkbox_text.setText('Text')
        self.checkbox_text.setChecked(True)

        self.checkbox_hex = QCheckBox()
        self.checkbox_hex.setText('Hex')

        self.checkbox_hex.toggled.connect(lambda checked: checked and self.checkbox_text.setChecked(False))
        self.checkbox_text.toggled.connect(lambda checked: checked and self.checkbox_hex.setChecked(False))
        self.checkbox_hex.toggled.connect(lambda checked: not checked and self.checkbox_text.setChecked(True))
        self.checkbox_text.toggled.connect(lambda checked: not checked and self.checkbox_hex.setChecked(True))

        self.checkbox_hbox = QHBoxLayout()
        self.checkbox_hbox.addWidget(self.checkbox_text)
        self.checkbox_hbox.addWidget(self.checkbox_hex)


        self.label_key = QLabel()
        self.label_key.setText('Ključ:')

        self.key_input = QLineEdit(self)
        regex = QtCore.QRegExp("[0-9a-fA-F]{16}")
        validator = QtGui.QRegExpValidator(regex, self.key_input)
        self.key_input.setValidator(validator)

        self.encryption_v_box.addLayout(self.checkbox_hbox)
        self.encryption_v_box.addWidget(self.label_key)
        self.encryption_v_box.addWidget(self.key_input)

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

    def stateChange(self, checkbox):
        if(not(checkbox.isChecked()) and (checkbox.text() == 'Text')):
            checkbox.setChecked(True)
            self.checkbox_hex.setChecked(False)

        elif(not(checkbox.isChecked()) and (checkbox.text() == 'Hex')):
            checkbox.setChecked(True)
            self.checkbox_text.setChecked(False)

    def encrypt(self):
        if(self.validateKey() and self.validateInput()):
            if(self.checkbox_text.isChecked()):
                text = des.encrypt(self.plaintext.text(), self.key_input.text(), True)
                self.key_input.setStyleSheet('QLineEdit { border-color: #1e1e1e }')
            else:
                text = des.encrypt(self.plaintext.text(), self.key_input.text(), False)
                self.key_input.setStyleSheet('QLineEdit { border-color: #1e1e1e }')

            self.ciphertext.setText(text)

    def decrypt(self):
        text = des.decrypt(self.plaintext.text())
        self.ciphertext.setText(text)

    def validateKey(self):
        if(len(self.key_input.text()) != 16):
            self.key_input.setPlaceholderText("Key needs to be 16 hexadecimal characters")
            self.key_input.setStyleSheet('QLineEdit { border-color: #EC0505 }')
            return False

        return True

    def validateInput(self):
        if(self.checkbox_text.isChecked()):
            if((len(self.plaintext.text()) * 8) % 64 == 0  and  self.plaintext.text() != ''):
                return True
            else:
                self.plaintext.setPlaceholderText("Invalid input")
                self.plaintext.setStyleSheet('QLineEdit { border-color: #EC0505 }')
                return False

        else:
            if((len(self.plaintext.text()) * 4) % 64 == 0 and self.plaintext.text() != ''):
                return True
            else:
                self.plaintext.setPlaceholderText("Invalid input")
                self.plaintext.setStyleSheet('QLineEdit { border-color: #EC0505 }')
                return False

