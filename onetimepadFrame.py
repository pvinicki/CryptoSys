import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from frameTemplate import frameTemplate
import ciphers.onetimepad as otp

class onetimepadFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        super().initUI()

        self.definition.insertPlainText('U kriptografiji, Cezarova šifra jedan je od najjednostavnijih i najrasprostranjenijih načina šifriranja. To je tip šifre zamjene (supstitucije), u kome se svako slovo otvorenog teksta zamjenjuje odgovarajućim slovom abecede, pomaknutim za određeni broj mjesta. Na primjer, s pomakom 3, A se zamjenjuje slovom D, B slovom E itd. Ova metoda je dobila ime po Juliju Cezaru, koji ju je koristio za razmjenu poruka sa svojim generalima.')

        self.cb_method.addItem("Encrypt")
        self.btn_encrypt.clicked.connect(self.encrypt)


    def encrypt(self):
        text = otp.encrypt(self.plaintext.text())
        self.ciphertext.setText(text)
