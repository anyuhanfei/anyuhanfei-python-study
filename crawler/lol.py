'''
    爬取lol英雄皮肤
    http://lol.qq.com/biz/hero/champion.js此js中有各个英雄的名称和id
'''

import requests
import re
import json
import time

# 获取js源代码，获取英雄id
# 拼接url地址
# 获取下载图片地址
# 下载图片

def getLOLImages() :
    ''' 获取英雄皮肤图片 '''
    url_js = 'http://lol.qq.com/biz/hero/champion.js'
    res_js = requests.get(url_js) #请求网址
    res_js = res_js.content # text 字符串   content 二进制字节
    html_js = res_js.decode() # 二进制解码
    req = '"keys":(.*?),"data"' #适配正则表达式
    list_js = re.findall(req, html_js) #获取符合的数据
    dict_js = json.loads(list_js[0]) #把获取到的json字符串转换成字典
    # 定义图片列表
    pic_list = []
    for key in dict_js :
        for i in range(20):
            num = str(i)
            if len(num) == 1:
                hero_num = "00" + num
            elif len(num) == 2:
                hero_num = "0" + num
            numstr = key + hero_num
            url = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big' + numstr + '.jpg'
            pic_list.append(url)

    #图片名称
    list_filepath = []
    path = 'D:\\python\\PYTHON\\myTest\\reptilian\\mReptilian\\LOLpic\\pic\\'
    for name in dict_js.values() :
        for i in range(20):
            file_path = path + name + str(i) + '.jpg'
            list_filepath.append(file_path)
    
    # 下载图片
    n = 0
    for picurl in pic_list:
        res = requests.get(picurl)
        n += 1
        # 判断状态码来筛选无效url
        if res.status_code == 200:
            print('正在下载',list_filepath[n])
            time.sleep(1)
            with open(list_filepath[n],'wb') as f:
                f.write(res.content)



if __name__ == '__main__' :
    getLOLImages()