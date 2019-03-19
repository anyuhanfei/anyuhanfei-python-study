'''
功能
    通过百度的文字识别API来识别已经保存好的图片
前置
    需要在百度云中创建文字识别的应用，从而获取AppID等信息
安装
    需要安装百度api,pip install baidu-aip
bug
    本想用其他文件来保存appkey等信息，然后通过第三方库获取，可是会一直找不到节，所以只能改为普通方式
'''

from aip import AipOcr
import configparser

class BaiDuAPI():
    ''' 图片文字识别 '''
    file_path = 'password.ini'
    image_path = 'Picture.png'

    def __init__(self, file_path = None):
        if file_path != None:
            self.file_path = file_path
        # target = configparser.ConfigParser()
        # target.read('gbk',self.file_path)
        # app_id = target.get('my','AppId')
        # api_key = target.get('my','AppKey')
        # secret_key = target.get('my','AppId')
        app_id = '11383668'
        api_key = 'skDw1evEa49bMgyrS68C3Mke'
        secret_key = 'QbiwCEs0Yfv3FmU8cVfWAVSpvPqp1fRM'
        self.client = AipOcr(app_id, api_key, secret_key)

    def pictureText(self,image_path = None):
        ''' 读取图片中的图片 '''
        if image_path != None:
            self.image_path = image_path
        images = self.gerPicture()
        texts = self.client.basicGeneral(images)
        allTexts = '\n'
        for word in texts['words_result']:
            allTexts = allTexts + word.get('words', '')
        return allTexts

    def gerPicture(self):
        with open(self.image_path, 'rb') as fp:
            return fp.read()


if __name__ == '__main__':
    baidu_api = BaiDuAPI()
    res = baidu_api.pictureText()
    print(res)
