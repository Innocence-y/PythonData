#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 导出数据库到Excel
import xlwt
import pymysql

conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456',
        db='librarysystem',
        charset="utf8"
    )

cursor = conn.cursor()
count = cursor.execute('select * from book')
#重置游标位置
cursor.scroll(1, mode='relative')
#搜取所有结果
results = cursor.fetchall()
#测试代码，print results
#获取MYSQL里的数据字段
fields = cursor.description
#将字段写入到EXCEL新表的第一行
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('book', cell_overwrite_ok=True)
for ifs in range(0, len(fields)):
    sheet.write(0, ifs, fields[ifs][0])
row = 1
col = 0


for row in range(1, len(results)+1):
    for col in range(0, len(fields)):
        sheet.write(row, col, results[row-1][col])
wbk.save('C:/Users/HP\Desktop/outExcel.xls')