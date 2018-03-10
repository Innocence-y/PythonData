#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymysql
import xlrd
#打开excel
data = xlrd.open_workbook('d:\\3.xlsx')
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
    sql = 'insert into sex(sex, number) values("%s", "%d")' % \
          (row[0], row[1])
    print(sql)
    try:
        # 执行sql语句
        cursor.execute(sql)
        print("execute")
        # 提交到数据库执行
        conn.commit()
        print("success")
    except Exception as e:
        print("exception")
        print(e)
        conn.rollback()
    # 关闭数据库连接
    conn.close()