# coding=UTF-8
import os
from tqdm import tqdm
import openpyxl
import sqlite3 as sl
import re
import gc
ILLEGAL_CHARACTERS_RE = re.compile(r'[\000-\010]|[\013-\014]|[\016-\037]')
db3_path = r''#db3文件路径
excel_path = r''#写入excel后存放的路劲
db3 = sl.connect(db3_path)
cur = db3.cursor()
content = cur.execute('SELECT * FROM Content')
des = content.description
titles = [ti[0] for ti in des]
print(titles)
workbook = openpyxl.Workbook()
booksheet = workbook.active
booksheet.append(titles)
n = 0
m = 1
for c in tqdm(content):
    c = [ILLEGAL_CHARACTERS_RE.sub(r'', str(c1)) for c1 in c]
    booksheet.append(c)
    n += 1
    #print(n)
    if n % 250000 == 0:
        print('正在保存{}.xlsx。。。'.format(m))
        workbook.save(excel_path + '\{}.xlsx'.format(m))
        del workbook
        gc.collect()
        workbook = openpyxl.Workbook()
        booksheet = workbook.active
        booksheet.append(titles)
        m += 1
workbook.save(excel_path + '\{}.xlsx'.format(m))
















