'''
成语接龙入口文件

左上是电脑输入框, 玩家不可输入.
左上到中间是一个大的交互界面, 用来展示游戏进度和历史.
右侧是最近两个成语的解释.
左下是输入框, 玩家输入的地方
'''
import sys

from PyQt5.QtWidgets import QApplication

from window import Window


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec_())
