# This Python file uses the following encoding: utf-8
import sys
import os
from numpy.linalg import inv
from strings import hill_txt
from PyQt5.QtWidgets import (QWidget, QMessageBox, QCheckBox, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from PyQt5 import QtGui
from frameTemplate import frameTemplate
from ciphers.hill import Hill

class hillFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.hl = Hill()
        self.initUI()

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText(hill_txt)

        self.cb_method.addItem("Encrypt")
        self.cb_method.addItem("Decrypt")
        self.btn_encrypt.clicked.connect(self.encrypt)
        self.cb_method.currentIndexChanged.connect(self.selectionChange)

        regex = QtCore.QRegExp("^[a-zA-Z]+$")
        validator = QtGui.QRegExpValidator(regex, self.plaintext)
        self.plaintext.setValidator(validator)

        self.label_key = QLabel()
        self.label_key.setText('Ključ:')

        self.key_input = QGridLayout()
        self.hbox_key = QHBoxLayout()
        for row in range(3):
            for col in range(3):
                self.input_field = QLineEdit()
                self.inputs.append(self.input_field)
                self.input_field.setInputMask('D00;_')
                self.input_field.setFixedWidth(40)
                self.key_input.addWidget(self.input_field, row, col)

        self.hbox_key.addStretch(1)
        self.hbox_key.addLayout(self.key_input)
        self.hbox_key.addStretch(1)
        self.encryption_v_box.addWidget(self.label_key)
        self.encryption_v_box.addLayout(self.hbox_key)

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
        if(self.validateInput() and self.validateKey() and self.checkInvertibility()):
            text = self.hl.encrypt(self.plaintext.text(), self.key)
            self.ciphertext.setText(text)
            self.plaintext.setStyleSheet('QLineEdit { border-color: #1e1e1e }')

    def decrypt(self):
        if(self.validateInput() and self.validateKey() and self.checkInvertibility()):
            text = self.hl.decrypt(self.plaintext.text())
            self.ciphertext.setText(text)
            self.plaintext.setStyleSheet('QLineEdit { border-color: #1e1e1e }')

    def getKey(self):
        self.key = []
        buffer = []

        for input in self.inputs:
            buffer.append(int(input.text()))

            if(len(buffer) == 3):
                self.key.append(buffer)
                buffer = []

        return self.key

    def validateKey(self):
        for input in self.inputs:
            if(not input.hasAcceptableInput()):
                return False

        return True

    def validateInput(self):
        if(self.plaintext.text() == ''):
            self.plaintext.setPlaceholderText("Input required")
            self.plaintext.setStyleSheet('QLineEdit { border-color: #EC0505 }')
            return False

        return True

    def checkInvertibility(self):
        self.key = self.getKey()
        minor_matrixA = (self.key[1][1] * self.key[2][2]) - (self.key[1][2] * self.key[2][1])
        minor_matrixB = (self.key[1][0] * self.key[2][2]) - (self.key[1][2] * self.key[2][0])
        minor_matrixC = (self.key[1][0] * self.key[2][1]) - (self.key[1][1] * self.key[2][0])
        determinant = (self.key[0][0] * minor_matrixA) - (self.key[0][1] * minor_matrixB) - (self.key[0][2] * minor_matrixC)

        if(determinant == 0):
            self.showWarning()
            return False

        return True

    def showWarning(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Critical)
        self.msg.setText("Given matrix is not invertible")
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.show()

