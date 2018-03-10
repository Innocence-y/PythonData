#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyecharts import Bar
import pymysql
import webbrowser


try:
    conn = pymysql.Connection(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        db="librarysystem"
    )
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("select number from sort;")
    rows = cur.fetchall()
    # rows = numpy.array(rows)
    attr = ["编程", "文学", "金融", "心理学", "医学", "历史", "小说", "军事", "法律", "体育"]
    lists = [[]]
    for row in rows:
        lists[0].append(row["number"])
        # lists[1].append(row["price"])


    print(lists[0])
    # print(lists[1])

    v1 = lists[0]
    # v2 = lists[1]

    print(v1)
    # print(v2)



    bar = Bar("图书借阅数量-柱状图")
    bar.add("数量", attr, v1, mark_line=["average"], mark_point=["max", "min"])
    # bar.add("数量", attr, v2, mark_line=["average"], mark_point=["max", "min"])
    bar.show_config()
    bar.render(r"D:\学习软件\IDEA\IntelliJ IDEA 2017.2.5\IJworkSpace\LibrarySystem\web\html\barNum.html")
finally:
    if conn:
        conn.close()
webbrowser.open(r"D:\学习软件\IDEA\IntelliJ IDEA 2017.2.5\IJworkSpace\LibrarySystem\web\html\barNum.html")