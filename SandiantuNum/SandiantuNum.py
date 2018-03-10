#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyecharts import Scatter
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
    cur.execute("select  number  from sort;")
    rows = cur.fetchall()
    # rows = numpy.array(rows)
    attr = ["编程", "文学", "金融", "心理学", "医学", "历史", "小说", "军事", "法律", "体育"]
    lists = [[], []]
    for row in rows:
        lists[0].append(row["number"])
        lists[1].append(row["number"])
    print(lists[0])
    print(lists[1])

    v1 = lists[0]
    v2 = lists[1]

    print(v1)
    print(v2)

    scatter = Scatter("图书借阅-散点图")
    # scatter.add("图书", v1, v2)
    # scatter.add("图书", v1[::-1], v2)
    scatter.add("借阅", v1, v2)
    scatter.show_config()
    scatter.render(r"D:\学习软件\IDEA\IntelliJ IDEA 2017.2.5\IJworkSpace\LibrarySystem\web\html\SanDiantuNum.html")

finally:
    if conn:
        conn.close()
webbrowser.open(r"D:\学习软件\IDEA\IntelliJ IDEA 2017.2.5\IJworkSpace\LibrarySystem\web\html\SanDiantuNum.html")