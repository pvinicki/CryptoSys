import sys
from strings import onetimepad_txt
from PyQt5.QtWidgets import (QWidget, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from PyQt5 import QtGui
from frameTemplate import frameTemplate
from ciphers.onetimepad import OneTimePad

class onetimepadFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.otp = OneTimePad()
        self.initUI()

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText(onetimepad_txt)

        self.label_key = QLabel()
        self.label_key.setText("Generirani ključ:")

        self.key = QLineEdit()
        self.key.setReadOnly(True)

        self.encryption_v_box.addWidget(self.label_key)
        self.encryption_v_box.addWidget(self.key)

        regex = QtCore.QRegExp("^[a-zA-Z]+$")
        validator = QtGui.QRegExpValidator(regex, self.plaintext)
        self.plaintext.setValidator(validator)

        self.cb_method.addItem("Encrypt")
        self.btn_encrypt.clicked.connect(self.encrypt)


    def encrypt(self):
        self.result = self.otp.encrypt(self.plaintext.text())
        text = self.result[0]
        self.ciphertext.setText(text)

        self.generated_key = ''.join(self.result[1])
        self.key.setText(self.generated_key)
