# Python3.6.0 新手推荐3
import json
# 导入模块
import requests  # pip install requests
from lxml import etree  # whl
import time


class MaoYan(object):
    '''下载猫眼电影Top100'''

    # 初始化方法（函数）
    def __init__(self):
        # 当你访问网址的时候 告诉服务器你是浏览器在访问的
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

    def getOnePage(self, url):
        '''获取网页源码'''
        html = requests.get(url, headers=self.header)
        return html.text

    def parseOnePage(self, text):
        '''解析网站  提取网站信息  用XPath'''
        html = etree.HTML(text)
        # 电影名称
        name = html.xpath('//p[@class="name"]//text()')
        # 主演
        star = html.xpath('//p[@class="star"]//text()')

        for item in range(len(name)):
            yield {
                'name': name[item],
                'star': star[item].strip()
            }

    @classmethod # 类方法
    def write2File(cls, content):
        '''写入文件'''
        with open(r'D:\python\PYTHON\myTest\tool\maoyan\top100.txt', 'a', encoding='utf-8') as fp:
            fp.write(json.dumps(content, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    maoyan = MaoYan()
    for offSet in range(10):
        time.sleep(1)  # 程序运行到这个地方要停顿一秒
        url = 'http://maoyan.com/board/4?offset={}'.format(offSet*10)
        html = maoyan.getOnePage(url)
        # 生成器  可迭代
        text = maoyan.parseOnePage(html)
        for item in text:
            maoyan.write2File(item)
            print(item)
