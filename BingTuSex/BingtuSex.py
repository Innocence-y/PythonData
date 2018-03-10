#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyecharts import Pie
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
    cur.execute("select number from sex;")
    rows = cur.fetchall()
    # rows = numpy.array(rows)
    attr = ["男", "女"]
    lists = [[]]
    for row in rows:
        lists[0].append(row["number"])
        # lists[1].append(row["woman"])

    print(lists[0])
    # print(lists[1])
    v1 = lists[0]
    # v2 = lists[1]

    print(v1)
    # print(v2)
    pie = Pie("图书借阅-饼图")
    pie.add("", attr, v1, is_label_show=True)
    # pie.add("", attr, v2, is_label_show=True)
    pie.show_config()
    pie.render(r"D:\学习软件\IDEA\IntelliJ IDEA 2017.2.5\IJworkSpace\LibrarySystem\web\html\BingTuSex.html")

finally:
    if conn:
        conn.close()

webbrowser.open(r"D:\学习软件\IDEA\IntelliJ IDEA 2017.2.5\IJworkSpace\LibrarySystem\web\html\BingTuSex.html")