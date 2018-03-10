#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import xlrd
#打开excel
data = xlrd.open_workbook('C:/Users/HP/Desktop/outExcel.xls')
#根据名字拿到excel的某个表
table = data.sheet_by_name('Sheet1')
#行数
nrows = table.nrows
for rownum in range(1,nrows):
    row = table.row_values(rownum)
    print(len(row))

    # 打开数据库连接
    conn = pymysql.connect(
            host="localhost",
            user="root",
            passwd="123456",
            db="librarysystem",
            charset="utf8"
    )
    #链接资源
    cursor = conn.cursor()

    # SQL 插入语句
    sql = 'insert into lendinfo (SerialNumber, username, BookId, Time) values("%s", "%s", "%s", "%s")' % \
          (row[0], row[1], row[2], row[3])
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()
        print("success")
    except:
        conn.rollback()
    # 关闭数据库连接
    conn.close()