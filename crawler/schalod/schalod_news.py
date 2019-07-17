import requests
from lxml import etree, html
from html.parser import HTMLParser
import pymysql


db = pymysql.connect("127.0.0.1", "root", "root", "schalod")
cursor = db.cursor()


def get_html_text(url):
    url_obj = requests.get(url)
    if url_obj.status_code != 200:
        return {'status': 2, 'data': '', 'msg': '执行失败'}
    return {'status': 1, 'data': url_obj.text, 'msg': '执行成功'}


def get_content(cursor, url):
    print('下载：%s' % (url))
    judge_url_sql = "SELECT * FROM news WHERE url='%s'" % (url)
    cursor.execute(judge_url_sql)
    if cursor.fetchall() != ():
        return
    res = get_html_text(url)
    text = etree.HTML(res['data'])
    # 上下页链接
    last_news_url_tuple = text.xpath('/html/body/div[8]/div[2]/div[4]/a[1]/@href')
    next_news_url_tuple = text.xpath('/html/body/div[8]/div[2]/div[4]/a[2]/@href')
    last_news_url = "http://www.schalod.com%s" % (last_news_url_tuple[0] if len(last_news_url_tuple) > 0 else '')
    next_news_url = "http://www.schalod.com%s" % (next_news_url_tuple[0] if len(next_news_url_tuple) > 0 else '')
    # 标题
    title = text.xpath('/html/body/div[8]/div[2]/div[1]/h1/text()')[0]
    # 日期
    insert_time = text.xpath('/html/body/div[8]/div[2]/div[1]/p/span[1]/text()')[0]
    # 内容
    content = HTMLParser().unescape(html.tostring(text.xpath('/html/body/div[8]/div[2]/div[2]')[0]).decode())
    add_sql = "INSERT INTO news (url, title, insert_time, content) value ('%s', '%s', '%s', '%s')" % (url, title, insert_time, content)
    try:
        cursor.execute(add_sql)
        db.commit()
        print('下载成功')
    except BaseException:
        db.rollback()
        print('下载失败')
    if last_news_url != 'http://www.schalod.com':
        get_content(cursor, last_news_url)
    if next_news_url != 'http://www.schalod.com':
        get_content(cursor, last_news_url)


# 新闻首页，随便找一个新闻文章进入
news_url = "http://www.schalod.com/news/"
news_url_res = get_html_text(news_url)
news_index_text = etree.HTML(news_url_res['data'])

# 新闻详情，获取当前内容和上下页链接
news_content_url = "http://www.schalod.com%s" % (news_index_text.xpath('//*[@id="section-focus-pic"]/div[1]/ul/li[1]/a/@href')[0])
get_content(cursor, news_content_url)

db.close()


'''
CREATE TABLE `news` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `insert_time` varchar(40) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `content` text COLLATE utf8mb4_general_ci,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=230 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
'''
