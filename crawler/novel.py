import requests
from lxml import etree
import os

novel_type_dict = {1: 'qihuan', 2: 'xiuzhen', 3: 'xiandai', 4: 'weilai', 5: 'wangyou', 6: 'qingchun', 7: 'junshi', 8: 'xuanyi', 9: 'chuanyue', 10: 'yanqing'}
print('小说编号:', end=" ")
print(novel_type_dict)
novel_type_number = int(input("请输入小说分类编号:"))
novel_type = novel_type_dict[novel_type_number]


# 创建分类文件夹并改变工作目录
try:
    os.mkdir("./%s" % novel_type)
except:
    pass
os.chdir("./%s" % novel_type)

page_number = int(input('请输入开始页码:'))
error_number = 0
while True:
    print('正在下载%s第%s页' % (novel_type, page_number))
    if page_number == 1:
        url = "https://www.shukeba.com/%s/" % novel_type
    else:
        url = "https://www.shukeba.com/%s/%s.html" % (novel_type, page_number)
    res = requests.get(url)
    
    if res.status_code != 200:
        error_number += 1
        if error_number > 5:
            print('已多次打开页面失败！')
            print('本次下载至%s第%s页' % (novel_type, page_number))
            input('下载失败或已下载至最后一页！')
            break
        
    res.encoding = 'utf-8'

    page = etree.HTML(res.text)

    # 图片，标题，作者，id, 简介
    book_img = page.xpath('//*[@class="book"]/div/img/@src')
    book_title = page.xpath('//*[@class="book"]/div/img/@alt')
    book_author = page.xpath('//*[@class="book"]/div/p[1]/a/text()')
    book_id = page.xpath('//*[@class="book"]/div[1]/a/@href')
    book_intro = page.xpath('//*[@class="book"]/div[2]/p[3]/a/text()')

    # 循环
    index = 0
    length = len(book_img)
    while index < length:
        print('正在下载%s' % book_title[index])
        b_id = book_id[index][1:-1]
        txt_url = 'http://downtxt.shukeba.com/main.php?action-downtxt-id-' + b_id
        txt_res = requests.get(txt_url)
        txt_res.encoding = 'utf-8'
        
        try:
            os.mkdir(book_title[index])
        except:
            pass
        # 小说
        title_dir = "./" + book_title[index] + "/" + book_title[index] + ".txt"
        with open(title_dir, 'wb') as c:
            c.write(txt_res.content)
        # 图片
        img_res = requests.get(book_img[index])
        img_dir = "./" + book_title[index] + "/" + book_author[index] + ".png"
        with open(img_dir, 'wb') as i:
            i.write(img_res.content)
        # 简介
        intro_dir = "./" + book_title[index] + "/intro.txt"
        with open(intro_dir, 'w+') as n:
            n.write(book_intro[index])
        # 参数递增
        index += 1
    # 参数递增
    page_number += 1
        