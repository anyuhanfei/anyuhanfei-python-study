'''
获取金色财经头条新闻

每隔一段时间获取一次

CREATE TABLE `xy_blocks_msg` (
  `id` int(32) NOT NULL AUTO_INCREMENT,
  `news_id` int(11) DEFAULT NULL COMMENT '原站点id，对比去重用',
  `bm_date` date DEFAULT NULL COMMENT '发布日期',
  `bm_title` varchar(128) DEFAULT NULL COMMENT '标题',
  `pic_addr` varchar(256) DEFAULT NULL COMMENT '图片url地址',
  `page_views` varchar(32) DEFAULT NULL COMMENT '阅读量',
  `username` varchar(50) DEFAULT NULL COMMENT '用户',
  `abstracts` varchar(512) DEFAULT NULL COMMENT '摘要',
  `context` varchar(256) DEFAULT NULL COMMENT '详情url地址',
  `content` text COMMENT '详情内容',
  `issue_time` datetime DEFAULT NULL COMMENT '发布时间',
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `titleUS` varchar(255) DEFAULT NULL COMMENT '英文标题',
  `contentUS` text COMMENT '英文内容',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `bm_date` (`bm_date`,`bm_title`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='区块链快讯';
'''

import requests
import json
import pymysql
import re
import time

MYSQL = pymysql.connect(
    host='rm-j6cczhj6xrd54119tdo.mysql.rds.aliyuncs.com',
    port=3306,
    user='wanbi',
    password='eplyQ18IutHCA356',
    db='wanbi_exchange',
    charset='utf8'
)
CURSOR = MYSQL.cursor()

replace_the_word_one = '区块链快讯'  # 替换 金色财经
replace_the_word_two = '区块链'  # 替换 金色

# 执行间隔
get_time = 1000

news_list_api_url = 'https://api.jinse.com/v6/www/information/list?catelogue_key=www&limit=5&information_id=0&flag=down&version=9.9.9&_source=www'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

cookies = {
    'userId': 'eyJpdiI6InBuQ3VZWmVURWQ4WEZYYXpZYWNMZnc9PSIsInZhbHVlIjoiRWhiVUtpQUJseUVXZnVFNUVzbitSbWNIYWU1RDNLMVNxd29uQmNROWFwT3ZObEUzWHpYRmFMZjdwQmd3Tmh6SW5uYXczcEs5UW9DVzllYnRsUVFIdUE9PSIsIm1hYyI6IjIzMTE5YTFjMTRkZWNkNmI2ZGM5MTA3ZDZmMmEzZmQ2ZDcwMTEyMmRhN2NjOWZhMjAzMDgzNjUwODIzNjM0YjMifQ%3D%3D',
    'is_refresh': 'eyJpdiI6InVZNXFcL0d0c0wyWEQwT1lrbXpCdmt3PT0iLCJ2YWx1ZSI6IjM1WmVtYXFVNDBoWmVsd0NhZ3Faenc9PSIsIm1hYyI6IjFmMjMxN2FmZmNjMDY1MTNkYTZiZTUwNGI0ZTAxZDQ0ODFhODk5MWZiNzdiMjY1MjA2MGU3YjU0Y2IxOTBmOTQifQ%3D%3D',
    'Hm_lvt_3b668291b682e6dc69686a3e2445e11d': '1578366666',
    'Hm_lpvt_3b668291b682e6dc69686a3e2445e11d': '1578373983'}


def comparison_id(news_id):
    '''查询当前id在服务器中是否存在'''
    sql = 'select * from xy_blocks_msg where news_id=%s' % (news_id)
    MYSQL.ping(reconnect=True)
    res = CURSOR.execute(sql)
    if res == 0:
        return True
    else:
        return False


def get_content(url, headers={}, cookies={}):
    '''获取文章详情'''
    res = requests.get(url, headers=headers, cookies=cookies)
    content = res.content.decode()
    regular_rule = "content:'(.*?)',authorId"
    list_res = re.findall(regular_rule, content)
    if list_res:
        return list_res[0]
    else:
        return ''


def get_data():
    # 请求接口，整理数据格式
    list_api_res = requests.get(news_list_api_url, headers=headers, cookies=cookies)
    list_api_content = json.loads(list_api_res.content.decode())

    # 遍历数据，获取所需信息并添加到数据库
    for i in list_api_content['list']:
        # 对比去重
        if comparison_id(i['id']) is False:
            continue
        # 获取内容
        try:
            content = get_content(i['extra']['topic_url'], headers, cookies)
        except BaseException:
            content = ''
        if content == '':
            continue
        # 拼接sql语句
        sql = "insert into xy_blocks_msg (%s) values (%s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            'news_id, bm_date, bm_title, pic_addr, page_views, username, abstracts, context, content, issue_time',
            i['id'],
            time.strftime('%Y-%m-%d', time.localtime(i['extra']['published_at'])),
            i['title'].replace('金色财经', replace_the_word_one).replace('金色', replace_the_word_two),
            i['extra']['thumbnails_pics'][0],
            str(i['extra']['read_number_yuan']),
            i['extra']['author'].replace('金色财经', replace_the_word_one).replace('金色', replace_the_word_two),
            i['extra']['summary'].replace('金色财经', replace_the_word_one).replace('金色', replace_the_word_two),
            i['extra']['topic_url'],
            content.replace('金色财经', replace_the_word_one).replace('金色', replace_the_word_two),
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(i['extra']['published_at']))
        )
        MYSQL.ping(reconnect=True)
        CURSOR.execute(sql)
        MYSQL.commit()


while True:
    get_data()
    time.sleep(get_time)
