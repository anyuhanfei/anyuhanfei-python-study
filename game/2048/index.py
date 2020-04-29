'''
类似 2048 小游戏的 python 项目练习

生成一个 n * n 的矩阵, 和4个按钮代表方向键.
每个回合生成 1~2 个 值为 2 或 4 的方块, 每次滑动将所有方块移动至指定方向, 相同的方块叠加(值与方块).
死亡判断: 无法新增方块.
'''
import sys

from PyQt5.QtWidgets import QApplication

from window import Window

app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec_())
