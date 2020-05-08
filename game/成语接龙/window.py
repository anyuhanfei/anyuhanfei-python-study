'''
成语接龙窗口
'''
import time

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QApplication, QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt

import __init__ as init
from data import data
import api


class Window(QWidget):
    data = data  # 成语大全
    last_idiom = ""  # 上一个成语
    history_idiom = []  # 本局游戏历史

    def __init__(self):
        super().__init__()

        self.resize(780, 700)
        self.setWindowTitle('成语接龙')

        # 展示控件
        self.composer()
        self.content_label()
        self.player()
        self.annotation_label()
        self.top_widget()

        # 获取数据并存储
        # self.data = api.get_data(init.DATA_FILE)
        self.index()

    def index(self):
        '''游戏初始化'''
        res, idiom = api.composer_input(self.data)
        self.last_idiom = idiom
        self._show_explain(idiom)
        self.content_label.setText('%s请输入符合条件的一个成语:%s\n' % (self.content_label.text(), idiom))

    def _composer_inputing(self):
        '''电脑输入'''
        QApplication.processEvents()
        time.sleep(0.6)
        res, idiom = api.composer_input(self.data, self.last_idiom)
        if res is False:
            print('错误')
        else:
            for i in idiom:
                self.composer_input.setText('%s%s' % (self.composer_input.text(), i))
                QApplication.processEvents()  # 刷新界面
                time.sleep(0.3)
        self.composer_btn.click()

    def _player_submit(self):
        '''玩家提交'''
        player_idiom = self.player_input.text()
        res, msg = api.judge_player_input(self.data, self.last_idiom, player_idiom)
        self.player_input.setText('')
        self.content_label.setText('%s您的输入:%s\n%s\n' % (self.content_label.text(), player_idiom, msg))
        if res is False:
            return
        self.last_idiom = player_idiom
        self._show_explain(player_idiom)
        self._composer_inputing()

    def _composer_submit(self):
        '''电脑提交'''
        composer_idiom = self.composer_input.text()
        self.composer_input.setText('')
        self.content_label.setText('%s系统的输入:%s\n请继续回复:\n' % (self.content_label.text(), composer_idiom))
        self.last_idiom = composer_idiom
        self._show_explain(composer_idiom)

    def _show_explain(self, idiom):
        '''展示注释,并添加历史'''
        for i in range(3, -1, -1):
            if i != 0:
                self.annotation_label[i].setText(self.annotation_label[i-1].text())
            else:
                idiom_data = self.data[idiom]
                content = "%s\n\n注释: %s\n\n出处: %s\n" % (idiom, idiom_data[3], idiom_data[4])
                self.annotation_label[i].setText(content)
        self.history_idiom.append(idiom)

    def _reset(self):
        '''游戏重置'''
        self.last_idiom = ''
        self.history_idiom = []
        self.content_label.setText('游戏开始...\n')
        for i in range(3, -1, -1):
            self.annotation_label[i].setText('')
        QApplication.processEvents()
        time.sleep(0.1)
        self.index()

    def _print(self):
        '''打印'''
        save_file_name, other = QFileDialog.getSaveFileName(self, '另存为', './', 'TXT(*.txt)', 'TXT(*.txt)')
        history_idiom_str = api.history_idiom(self.history_idiom)
        if save_file_name != '':
            with open(save_file_name, "w+", encoding="utf-8") as f:
                f.write(history_idiom_str)

    def composer(self):
        '''电脑输入'''
        self.composer_input = QLineEdit(self)
        self.composer_input.move(10, 110)
        self.composer_input.resize(310, 40)
        self.composer_input.setFont(QFont("Timers", 20))
        self.composer_input.setReadOnly(True)

        self.composer_btn = QPushButton(self)
        self.composer_btn.move(335, 110)
        self.composer_btn.resize(70, 40)
        self.composer_btn.setText('提交')
        self.composer_btn.clicked.connect(self._composer_submit)

    def content_label(self):
        '''交互框'''
        self.content_label = QLabel(self)
        self.content_label.move(10, 160)
        self.content_label.resize(400, 480)
        self.content_label.setText('游戏开始...\n')
        self.content_label.setStyleSheet("border:2px solid black; background-color: black; color: white;")
        self.content_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

    def player(self):
        '''玩家输入'''
        self.player_input = QLineEdit(self)
        self.player_input.move(10, 650)
        self.player_input.resize(310, 40)
        self.player_input.setFont(QFont("Timers", 20))

        self.player_btn = QPushButton(self)
        self.player_btn.move(335, 650)
        self.player_btn.resize(70, 40)
        self.player_btn.setText('提交')
        self.player_btn.clicked.connect(self._player_submit)

    def annotation_label(self):
        '''注释框'''
        self.annotation_label = []
        y = 110
        for i in range(0, 4):
            self.annotation_label.append(QLabel(self))
            self.annotation_label[i].move(430, y)
            self.annotation_label[i].resize(330, 130)
            self.annotation_label[i].setStyleSheet("border:2px solid black;")
            self.annotation_label[i].setAlignment(Qt.AlignLeft | Qt.AlignTop)
            self.annotation_label[i].setWordWrap(True)
            self.annotation_label[i].setIndent(4)
            self.annotation_label[i].setMargin(4)
            y += 150

    def top_widget(self):
        '''一些头部的控件'''
        # 游戏介绍
        game_annotation = QLabel(self)
        game_annotation.move(10, 0)
        game_annotation.resize(400, 90)
        game_annotation.setText('成语接龙游戏介绍:\n\n系统会给出一个成语, 用前一个成语的最后一个字与下一句成语的第一个相同的字【音同即可】，首尾相接不断延伸，形成长龙。\n\n每回合请在%s秒内作答, 超时即为游戏结束。' % (init.GAME_LIMITED_TIME))
        game_annotation.setWordWrap(True)
        # 倒计时
        self.countdown = QLabel(self)
        self.countdown.move(450, 20)
        self.countdown.resize(80, 80)
        # self.countdown.setText('%s' % (init.GAME_LIMITED_TIME))
        self.countdown.setFont(QFont("Timers", 30))
        # 重置按钮
        self.reset_btn = QPushButton(self)
        self.reset_btn.move(610, 10)
        self.reset_btn.resize(60, 40)
        self.reset_btn.setText('重置')
        self.reset_btn.clicked.connect(self._reset)
        # 打印按钮
        self.print_btn = QPushButton(self)
        self.print_btn.move(610, 60)
        self.print_btn.resize(60, 40)
        self.print_btn.setText('打印')
        self.print_btn.clicked.connect(self._print)
        # 空白按钮
        self.blank_btn1 = QPushButton(self)
        self.blank_btn1.move(680, 10)
        self.blank_btn1.resize(60, 40)
        self.blank_btn1.setText('空白')
        # 空白按钮
        self.blank_btn2 = QPushButton(self)
        self.blank_btn2.move(680, 60)
        self.blank_btn2.resize(60, 40)
        self.blank_btn2.setText('空白')
