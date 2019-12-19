'''
说曹操，曹操到导航网站爬虫

获取导航中的网址和网址名称，保存到指定 json 文件中

思路：先加载 json 文件，再爬取目标信息，先整理出信息数据，一一对比已保存的 json 文件，若存在则跳过，不存在则添加

分析：
网站信息都包含在  <script id="__NEXT_DATA__" type="application/json"></script>  中
'''
import requests
import re
import os
import json

# 准备工作
url = "https://caocao.boxopened.com/"

headers = {}
# 访问
url_res = requests.get(url, timeout=10)
content = url_res.content.decode('utf-8')
# 获取信息
findall_content = re.findall('<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', content)
if len(findall_content) <= 0:
    print('未获取到指定信息')
    os._exit()
# 整理数据
json_content = json.loads(findall_content[0])
need_content = {}
for i in json_content['props']['pageProps']['sites']:
    need_content.update({i['name']: i['url']})
# 获取旧数据
with open('url.json', 'r', encoding="utf-8") as f:
    old_content = f.read()
old_content = json.loads(old_content)
# 整合数据
for key, value in old_content.items():
    if need_content.get(key) is None:
        need_content.update({key: value})
# 存储数据
with open('url.json', 'w+', encoding="utf-8") as f:
    json.dump(need_content, f, ensure_ascii=False, indent=4)
