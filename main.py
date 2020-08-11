import sys
import os
os.chdir('D:\Faks\CryptoSys\CryptoSys')
stylesheet = os.path.abspath('css/stylesheet.css')
sys.path.append("resources")
ciphers = ['Cezar', 'Supstitucija', 'Vigenere', 'Playfair','Hill', 'Transpozicija', 'Jednokratna bilj.', 'DES kriptosustav']
from PyQt5.QtWidgets import (QWidget,QMainWindow, QLineEdit, QLabel, QCheckBox,  QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame, QMainWindow)
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from caesar_gui         import caesarFrame
from supstitutionFrame  import supstitutionFrame
from vigenereFrame      import vigenereFrame
from playfairFrame      import playfairFrame
from transpositionFrame import transpositionFrame
from onetimepadFrame    import onetimepadFrame
from hillFrame          import hillFrame
from desFrame           import desFrame

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.grid_layout = QGridLayout()
        self.setWindowTitle('CryptoSys')
        self.buttons = []

        self.initUI()

        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.grid_layout)
        self.setCentralWidget(self.centralWidget)


        self.setStyleSheet(open(stylesheet).read())
        self.setFixedWidth(600)

    #konfiguracija korisnickog sucelja
    def initUI(self):
        self.frame = caesarFrame()
        self.frame.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)

        self.v_box = QVBoxLayout()
        logo = QLabel(self)
        pixmap = QtGui.QPixmap(os.path.abspath('images/logo.png'))

        logo.setPixmap(pixmap)
        self.v_box.addWidget(logo)

        for x in range(8):
            self.button = QPushButton(ciphers[x])
            self.buttons.append(self.button)
            self.button.clicked.connect(lambda: self.buttonClicked())
            self.v_box.addWidget(self.button)

        self.grid_layout.addLayout(self.v_box, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.frame, 0, 1, -1, -1)

        self.grid_layout.setColumnStretch(0, 1)
        self.grid_layout.setColumnStretch(1, 12)
        self.grid_layout.setRowStretch(1, 12)

    def updateFrame(self, frame):
        self.grid_layout.removeWidget(self.frame)
        self.frame.setParent(None)

        self.frame = frame
        self.frame.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)
        self.grid_layout.addWidget(self.frame, 0, 1, -1, -1)

    #handler event za odabire gumba koji mijenjaju trenutni frame
    def buttonClicked(self):
        self.button = self.sender()
        if(self.button.text() == 'Cezar'):
            frame = caesarFrame()
            self.updateFrame(frame)

        elif(self.button.text() == 'Supstitucija'):
            print('suptitucija')
            frame = supstitutionFrame()
            self.updateFrame(frame)

        elif(self.button.text() == 'Vigenere'):
            frame = vigenereFrame()
            self.updateFrame(frame)

        elif(self.button.text() == 'Playfair'):
            frame = playfairFrame()
            self.updateFrame(frame)

        elif(self.button.text() == 'Hill'):
            frame = hillFrame()
            self.updateFrame(frame)

        elif(self.button.text() == 'Transpozicija'):
            frame = transpositionFrame()
            self.updateFrame(frame)

        elif(self.button.text() == 'Jednokratna bilj.'):
            frame = onetimepadFrame()
            self.updateFrame(frame)

        elif(self.button.text() == 'DES kriptosustav'):
            frame = desFrame()
            self.updateFrame(frame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(os.path.abspath('images/icon.png')))
    #app.setWindowIcon(QtGui.QIcon('://icon.png'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
