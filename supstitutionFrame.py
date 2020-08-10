import sys
sys.path.append("resources")
from strings import supstitution_txt
from PyQt5.QtWidgets import (QWidget, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from frameTemplate import frameTemplate
from ciphers.supstitution import Supstitution


class supstitutionFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.sp = Supstitution()
        self.initUI()

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText(supstitution_txt)

        self.cb_method.addItem("Encrypt")
        self.cb_method.addItem("Decrypt")
        self.cb_method.addItem("Brute Force")
        self.cb_method.currentIndexChanged.connect(self.selectionChange)

        self.btn_encrypt.clicked.connect(self.encrypt)

        #odabir ključa šifriranja
        self.spinbox_key = QSpinBox()
        self.spinbox_key.setRange(1,26)
        self.spinbox_key.singleStep()

        #oznaka za odabir ključa
        self.label_key = QLabel()
        self.label_key.setText('Ključ:')

        self.encryption_v_box.addWidget(self.label_key)
        self.encryption_v_box.addWidget(self.spinbox_key)


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

        elif(self.cb_method.itemText(index) == "Brute Force"):
            self.label_plaintext.setText("Ciphertext:")
            self.label_ciphertext.setText("Plaintext:")
            self.btn_encrypt.clicked.connect(self.bruteForce)
            self.btn_encrypt.setText("Decrypt")
            self.plaintext.clear()
            self.ciphertext.clear()

    def encrypt(self):
        text = self.sp.encrypt(self.plaintext.text(), self.spinbox_key.value())
        self.ciphertext.setText(text)

    def decrypt(self):
        text = self.sp.decrypt(self.plaintext.text(), self.spinbox_key.value())
        self.ciphertext.setText(text)

    def bruteForce(self):
        text = self.sp.bruteForce(self.plaintext.text())
        self.ciphertext.setText(text)

