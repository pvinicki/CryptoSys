import sys
from PyQt5.QtWidgets import (QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout,QPushButton, QApplication, QFrame, QMainWindow)
ciphers = ['Cezar', 'Supstitucija', 'Vigenere', 'Playfair','Hill', 'Transpozicija', 'Jednokratna bilj.', 'DES kriptosustav']
from caesar_gui import caesarFrame
from supstitutionFrame import supstitutionFrame

class basicWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout()
        self.setWindowTitle('CryptoSys')
        self.setLayout(self.grid_layout)
        self.buttons = []

        #configuring UI
    def initUI(self):
        self.frame = caesarFrame()
        self.frame.setFrameStyle(QFrame.StyledPanel | QFrame.Plain)

        self.v_box = QVBoxLayout()
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

    #handler event za odabire gumba koji mijenja frame
    def buttonClicked(self):
        self.button = self.sender()
        if(self.button.text() == 'Cezar'):
            frame = caesarFrame()
            self.updateFrame(frame)

        elif(self.button.text() == 'Supstitucija'):
            print('suptitucija')
            frame = supstitutionFrame()
            self.updateFrame(frame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = basicWindow()
    window.initUI()
    window.show()
    sys.exit(app.exec_())
