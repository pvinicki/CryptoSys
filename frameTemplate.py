# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import (QWidget, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)


class frameTemplate(QFrame):
    def __init__(self):
        super().__init__()

    def initUI(self):
        print('initializing frame template')
        self.definition = QPlainTextEdit()
        self.grid_layout = QGridLayout()

        #dropdown odabir metode kriptiranja/dekriptiranja
        self.cb_method = QComboBox()

        #polje za korisnikov unos
        self.plaintext   = QLineEdit(self)
        self.ciphertext  = QLineEdit(self)

        #Oznake polja za korisnikov unos
        self.label_plaintext  = QLabel()
        self.label_ciphertext = QLabel()
        self.label_plaintext.setText("Plaintext:")
        self.label_ciphertext.setText("Ciphertext:")

        #gumb za kriptiranje/dekriptiranje
        self.btn_encrypt = QPushButton("Encrypt")

        #hbox za polja unosa
        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.plaintext)
        self.h_box.addWidget(self.ciphertext)
        self.h_box.insertSpacing(1, 7)

        #hbox za oznake
        self.label_h_box = QHBoxLayout()
        self.label_h_box.addWidget(self.label_plaintext)
        self.label_h_box.addWidget(self.label_ciphertext)

        #vbox sa hboxom oznaka i gumbom (čini sučelje za šifriranje)
        self.encryption_v_box = QVBoxLayout()
        self.encryption_v_box.addLayout(self.label_h_box)
        self.encryption_v_box.addLayout(self.h_box)
        self.encryption_v_box.addWidget(self.btn_encrypt)

        #kompletan layout, sučelje za šifriranje i objašnjenje metode kriptiranja
        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.definition)
        self.v_box.addWidget(self.cb_method)
        self.v_box.addLayout(self.encryption_v_box)
        self.v_box.setSpacing(10)
        self.v_box.addStretch(1)

        #self.container = QHBoxLayout()
        #self.container.addLayout(self.v_box)
        #self.container.addStretch(1)

        self.grid_layout.addLayout(self.v_box, 0, 0, -1, 2)
        self.setLayout(self.grid_layout)
