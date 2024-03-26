import random
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QSpinBox

# Updated rootclass to include "Vagabond" and "Second Vagabond" based on player count
def generate_rootclass(player_count):
    rootclass = ["Marquise de Cat", "Eyrie Dynasties", "Woodland Alliance"]
    rootclass += ["Vagabond"]
    if player_count >= 5:
        rootclass.append("Second Vagabond")
    rootclass += ["Lizard Cult", "Riverfolk Company", "Underground Duchy", "Corvid Conspiracy", "Lord of the Hundreds", "Keepers in Iron"]
    return rootclass

vagabonds = ["Thief", "Tinker", "Ranger", "Vagrant", "Arbiter", "Scoundrel", "Adventurer", "Ronin", "Harrier"]

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Root Advanced Setup Draft")
        self.resize(600, 400)  # Smaller window size
        
        self.UiComponents()

    def UiComponents(self):
        self.result_label = QLabel(self)
        self.result_label.setGeometry(50, 130, 500, 150)  # Adjusted position, moved slightly down
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        player_count_label = QLabel("Player Count", self)
        player_count_label.setGeometry(250, 10, 100, 20)  
        player_count_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = player_count_label.font()
        font.setBold(True)
        player_count_label.setFont(font)
        
        self.player_count_spinbox = QSpinBox(self)
        self.player_count_spinbox.setGeometry(250, 40, 100, 30)  
        self.player_count_spinbox.setMinimum(3)
        self.player_count_spinbox.setMaximum(6)
        self.player_count_spinbox.valueChanged.connect(self.on_player_count_changed)

        draft_button = QPushButton("DRAFT", self)
        draft_button.setGeometry(220, 100, 160, 40)  
        draft_button.clicked.connect(self.on_draft_button_clicked)

        self.vagabond_button = QPushButton("Select Vagabond", self)
        self.vagabond_button.setGeometry(220, 280, 160, 40)  
        self.vagabond_button.clicked.connect(self.on_vagabond_button_clicked)
        self.vagabond_button.setEnabled(False)  # Initially disabled

        self.vagabond_label = QLabel(self)
        self.vagabond_label.setGeometry(50, 320, 500, 40)  
        self.vagabond_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def on_player_count_changed(self):
        # When player count changes, update rootclass and enable/disable vagabond button accordingly
        player_count = self.player_count_spinbox.value()
        rootclass = generate_rootclass(player_count)
        self.vagabond_button_enabled = "Vagabond" in rootclass or "Second Vagabond" in rootclass
        self.vagabond_button.setEnabled(self.vagabond_button_enabled)

    def on_draft_button_clicked(self):
        # When draft button clicked, select items from rootclass based on player count and display
        player_count = self.player_count_spinbox.value()
        rootclass = generate_rootclass(player_count)
        num_items_to_select = min(player_count + 1, len(rootclass))  # Ensure sample size doesn't exceed population
        selected_items = random.sample(rootclass, num_items_to_select)
        result_text = "\n".join(selected_items)
        self.result_label.setText(result_text)

    def on_vagabond_button_clicked(self):
        # When vagabond button clicked, select vagabond classes based on enabled buttons and display
        player_count = self.player_count_spinbox.value()
        rootclass = generate_rootclass(player_count)
        selected_vagabonds = []
        if "Vagabond" in rootclass:
            selected_vagabonds.append(random.choice(vagabonds))
        if "Second Vagabond" in rootclass:
            selected_vagabonds.append(random.choice(vagabonds))
        vagabond_text = "\n".join(selected_vagabonds)
        self.vagabond_label.setText(vagabond_text)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
