'''
功能
    把已经获取到的文字保存到剪切板上
    这里视频教程为了稍微方便，把类中的两个方法分别定义为静态方法和类方法，它们都只需要通过类名.方法名的方式访问
提示
    如果出现win32con报错的情况，需要安装pypwin32（python -m pip install pypiwin32）。
    虽然说win32con是内置的，但是也有的版本会出错；
'''
import win32con

import win32clipboard

class GetText:
    ''' 把图像识别出的文字保存到剪切板 '''

    @staticmethod
    def getText():
        ''' 获取当前剪切板中的内容 '''
        win32clipboard.OpenClipboard()
        d = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
        return d
    
    @classmethod
    def setText(cls, aString):
        ''' 设置剪切板中的内容，这里把已经获取到的图片中的文字保存在剪切板中 '''
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, aString)
                        
if __name__ == "__main__":
    GetText.setText('666')
    GetText.getText()