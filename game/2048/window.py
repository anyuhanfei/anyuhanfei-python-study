import time

from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QFrame

import __init__ as init
import function


class Window(QWidget):
    矩阵 = []

    def __init__(self):
        super().__init__()

        self.setWindowTitle('2048')
        self.resize(600, 600)

        self.创建矩阵(init.生成矩阵边长)
        self.创建方向按钮()

    def 创建矩阵(self, 边长):
        '''创建一个指定边长的矩阵'''
        for i in range(0, 边长):
            for o in range(0, 边长):
                if o == 0:
                    self.矩阵.append([1, 2, 3, 4])
                self.矩阵[i][o] = QLabel(self)
                self.矩阵[i][o].move(100 + o * 50, 100 + i * 50)
                self.矩阵[i][o].resize(50, 50)
                self.矩阵[i][o].setText('0')
                self.矩阵[i][o].setStyleSheet("font-size: 26px;")
                self.矩阵[i][o].setFrameShadow(QFrame.Raised)

    def 创建方向按钮(self):
        '''创建4个方向按钮'''
        # 上箭头
        self.up_btn = QPushButton(self)
        self.up_btn.move(300, 500)
        self.up_btn.resize(50, 50)
        self.up_btn.setText('↑')
        self.up_btn.clicked.connect(lambda: self._move('up'))
        # 左箭头
        self.left_btn = QPushButton(self)
        self.left_btn.move(250, 550)
        self.left_btn.resize(50, 50)
        self.left_btn.setText('←')
        self.left_btn.clicked.connect(lambda: self._move('left'))
        # 下箭头
        self.down_btn = QPushButton(self)
        self.down_btn.move(300, 550)
        self.down_btn.resize(50, 50)
        self.down_btn.setText('↓')
        self.down_btn.clicked.connect(lambda: self._move('down'))
        # 右箭头
        self.right_btn = QPushButton(self)
        self.right_btn.move(350, 550)
        self.right_btn.resize(50, 50)
        self.right_btn.setText('→')
        self.right_btn.clicked.connect(lambda: self._move('right'))

    def _move(self, 方向):
        '''调用移动矩阵方法'''
        self.矩阵 = function.移动矩阵(self.矩阵, 方向)
        time.sleep(0.3)
        res = function.生成新方块(self.矩阵)
        self.矩阵 = res[0]
        if res[1] is True:
            # 死亡
            pass
