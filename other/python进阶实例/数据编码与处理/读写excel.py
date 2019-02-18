'''
    读写excel文件
'''
# 使用第三方库xlrd和xlwt，这两个库分别用于读和写
# pip install xlrd xlwt

import xlrd

book = xlrd.open_workbook('dome.xlsx')
book.sheets()  # 返回对象
sheet = book.sheet_by_index(0)  # 返回整个表
sheet.nrows  # 返回行数
sheet.ncols  # 返回列数

# 单个数据
cell = sheet.cell(0, 0)  # 返回坐标对应的内容的对象
cell.value()  # 返回这个的内容
# 整行（列基本相同，col）
sheet.row(1)  # 返回列表，是sell对象
sheet.row_values(1)  # 返回列表，只有数据

import xlwt

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet('sheet1')  # 添加一个表
wsheet.write()