# This Python file uses the following encoding: utf-8
import sys
sys.path.append("resources")
from strings import hill_txt
from PyQt5.QtWidgets import (QWidget, QCheckBox, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from frameTemplate import frameTemplate
import ciphers.hill as hl

class hillFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.inputs = []
        self.initUI()

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText(hill_txt)

        self.cb_method.addItem("Encrypt")
        self.btn_encrypt.clicked.connect(self.encrypt)

        self.label_key = QLabel()
        self.label_key.setText('Key:')

        self.key_input = QGridLayout()
        self.hbox_key = QHBoxLayout()
        for row in range(3):
            for col in range(3):
                self.input_field = QLineEdit()
                self.inputs.append(self.input_field)
                self.input_field.setInputMask('000;_')
                self.input_field.setFixedWidth(40)
                self.key_input.addWidget(self.input_field, row, col)

        self.hbox_key.addStretch(1)
        self.hbox_key.addLayout(self.key_input)
        self.hbox_key.addStretch(1)
        self.encryption_v_box.addWidget(self.label_key)
        self.encryption_v_box.addLayout(self.hbox_key)

    def encrypt(self):
        text = hl.encrypt(self.plaintext.text(), self.getKey())
        self.ciphertext.setText(text)

    def getKey(self):
        self.key = []
        buffer = []

        for input in self.inputs:
            buffer.append(int(input.text()))

            if(len(buffer) == 3):
                self.key.append(buffer)
                buffer = []

        return self.key


