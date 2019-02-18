'''
    给每一行的数据都添加一项坐标
'''

import csv  # pip install csvfile

import geocoding

''' 配置 '''
paths = []  # 文件列表
path_list = 2  # 下标

for path in paths :
    # path = '钱眼网\钱眼网企业资料_电脑互联网.csv'  # 文件名
    print('正在操作%s' % path)
    new_path = '已完成\\' + path
    key = '40fe8f7ca0626fe71fe12bdc54922ded'
    gao_api = geocoding.geocoding(key)

    with open(path, 'r', encoding="utf-8") as csvFile:
        rows = csv.reader(csvFile)
        with open(new_path, 'w', encoding="utf-8") as f:
            writer = csv.writer(f)
            for row in rows:
                if row[path_list] == '企业地址' :
                    row.append("地址坐标")
                    writer.writerow(row)
                else :
                    if len(row) >= (path_list + 1) :
                        g = gao_api.index(row[path_list],1)
                        row.append(g)
                        writer.writerow(row)

