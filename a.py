import os
import sys
import subprocess

from googleapiclient.discovery import build
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *

import pyscreenshot as ImageGrab

sudoPass = 'lamborghini'

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignHCenter)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        text_box = QTextEdit()
        text_box.setText("abc")
        text_box.setFixedSize(200, 50)
        text_box.setReadOnly(True)
        layout.addWidget(text_box)
        layout.setAlignment(text_box, Qt.AlignHCenter)


        button = QPushButton("DO")
        button.setFixedSize(200, 50)
        layout.addWidget(button, 1)
        layout.setAlignment(button, Qt.AlignHCenter)

        self.show()

        command = '%s %s %s %s' % (os.path.abspath('./osx.sh'), 'QuickTime Player', '500', '500')
        os.system('echo %s|sudo -S %s' % (sudoPass, command))

def search():

    service = build("customsearch", "v1",
                    developerKey="AIzaSyB2fBI-MiPty_wgETQScuyCN33wSCtJUsg")

    rse = service.cse().list(
        q='lectures',
        cx='011673693733911086344:_vsdh-a05s0',
        exactTerms='U of T'
    ).execute()


    count = rse['queries']['request'][0]['totalResults']

    print(count)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("abc")

    window = MainWindow()
    app.exec_()


