'''
功能
    监控键盘按键,监控截图的按键并且保存图片到同目录下
前置
    需要安装keyboard负责监控按键，在命令行中执行pip install keyboard来安装
    需要安装PIL负责保存剪切板中的图片，在命令行中执行pip install Pillow来安装
提示
    在vscode里可以使用右键排序import语句
    在vscode中在执行中需要中断执行使用ctrl+c
扩展
    pip install pyinstallor 打包成exe文件
    PyInstaller语法：用命令行或者PowerShell，用cd命令进入.py所在的目录，
    然后执行命令：pyinstaller -F Yourname.py（以后研究）
'''
import sys
from time import sleep

import keyboard
from PIL import ImageGrab

from baiDuApi import BaiDuAPI
from getText import GetText


def screenShot():
    ''' 用于截图并保存 '''

    # 等待按下的键盘按键，多个按键用+连接，这里是截图开始
    if keyboard.wait(hotkey='alt+ctrl+a') is None:
        # 同上，这里是截图开始
        if keyboard.wait(hotkey='Enter') is None:
            # 因为获取剪切板的图片太快了，所以要停顿一小段时间
            sleep(0.01)
            # 复制剪切板中的图片
            im = ImageGrab.grabclipboard()
            sleep(0.01)
            im.save('Picture.png')


if __name__ == "__main__":
    # 为了可以多次截图而不是截一次图就结束程序
    baidu_api = BaiDuAPI()

    for i in range(sys.maxsize):
        if i == 0:
            print("注意事项：请使用QQ的默认截图按键（Ctrl+alt+a）,截图完成后请敲击回车键完成截图!")
            print("截图完成后，你截取图片中的文字自动复制，您可自由粘贴！")
            print("现在开始截取你需要的图片吧！\n")
        else:
            print("您已成功截图，请截取下一张图！\n")
        screenShot()

        res = baidu_api.pictureText()
        print('截取的内容：' + res)

        GetText.setText(res)
        sleep(0.01)
        GetText.getText()

