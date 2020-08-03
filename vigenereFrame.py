# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QSpinBox, QComboBox, QPlainTextEdit, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame)
from PyQt5 import QtCore
from frameTemplate import frameTemplate
import ciphers.vigenere as vg


class vigenereFrame(frameTemplate):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI():
        super().initUI()


