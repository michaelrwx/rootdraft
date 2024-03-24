import random
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QWidget

rootclass = ["Marquise de Cat", "Eyrie Dynasties", "Woodland Alliance", "Vagabond", "Lizard Cult", "Riverfolk Company", "Underground Duchy", "Corvid Conspiracy", "Lord of the Hundreds", "Keepers in Iron"]
vagabonds = ["Thief", "Tinker", "Ranger", "Vagrant", "Arbiter", "Scoundrel", "Adventurer", "Ronin", "Harrier"]

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Root Advanced Setup Draft")
        self.resize(700, 700)
        
        self.UiComponents()

    def UiComponents(self):
        draft = QPushButton("DRAFT", self)
        draft.setGeometry(300, 150, 100, 40) #x-coordinate, y-coordinate, length of box, width of box
        vagabonder = QPushButton("VAGABOND", self)
        vagabonder.setGeometry(300, 250, 100, 40) #x-coordinate, y-coordinate, length of box, width of box

app = QApplication(sys.argv)

window = MainWindow() #Takes from the class and labels it into window
window.show() #If this doesn't happen then there is no window shown

app.exec()