#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyecharts import Bar
import pymysql

try:
    conn = pymysql.Connection(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        db="librarysystem"
    )
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("select grade from book;")
    rows = cur.fetchall()
    # rows = numpy.array(rows)
    attr = ["编程", "文学", "金融", "心理学", "医学", "历史", "小说", "军事", "法律", "体育"]
    lists = [[]]
    for row in rows:
        lists[0].append(row["grade"])
        # lists[1].append(row["price"])


    print(lists[0])
    # print(lists[1])

    v1 = lists[0]
    # v2 = lists[1]

    print(v1)
    # print(v2)



    bar = Bar("读者评分-柱状图")
    bar.add("评分", attr, v1, mark_line=["average"], mark_point=["max", "min"])
    # bar.add("数量", attr, v2, mark_line=["average"], mark_point=["max", "min"])
    bar.show_config()
    bar.render(r"d:\Graph\BarGrade.html")
finally:
    if conn:
        conn.close()