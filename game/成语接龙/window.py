'''
成语接龙窗口
'''


from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(780, 600)
        self.setWindowTitle('成语接龙')

        self.composer_input()
        self.composer_btn()
        self.content_label()
        self.player_input()
        self.player_btn()
        self.annotation_label_one()
        self.annotation_label_two()

    def composer_input(self):
        self.composer_input = QLineEdit(self)
        self.composer_input.move(10, 10)
        self.composer_input.resize(310, 40)

    def composer_btn(self):
        self.composer_btn = QPushButton(self)
        self.composer_btn.move(335, 10)
        self.composer_btn.resize(70, 40)

    def content_label(self):
        self.content_label = QLabel(self)
        self.content_label.move(10, 60)
        self.content_label.resize(400, 480)
        self.content_label.setText('游戏开始...')
        self.content_label.setStyleSheet("border:2px solid black;")

    def player_input(self):
        self.player_input = QLineEdit(self)
        self.player_input.move(10, 550)
        self.player_input.resize(310, 40)

    def player_btn(self):
        self.player_btn = QPushButton(self)
        self.player_btn.move(335, 550)
        self.player_btn.resize(70, 40)

    def annotation_label_one(self):
        self.annotation_label_one = QLabel(self)
        self.annotation_label_one.move(430, 10)
        self.annotation_label_one.resize(330, 280)
        self.annotation_label_one.setStyleSheet("border:2px solid black;")

    def annotation_label_two(self):
        self.annotation_label_two = QLabel(self)
        self.annotation_label_two.move(430, 310)
        self.annotation_label_two.resize(330, 280)
        self.annotation_label_two.setStyleSheet("border:2px solid black;")
