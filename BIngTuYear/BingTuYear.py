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
    cur.execute("select number from year;")
    rows = cur.fetchall()
    # rows = numpy.array(rows)
    attr = ["大一", "大二", "大三", "大四"]
    lists = [[]]
    for row in rows:
        lists[0].append(row["number"])

    print(lists[0])
    v1 = lists[0]

    print(v1)
    pie = Pie("图书借阅年级统计-饼图")
    pie.add("", attr, v1, is_label_show=True)
    pie.show_config()
    pie.render(r"D:\学习软件\IDEA\IntelliJ IDEA 2017.2.5\IJworkSpace\LibrarySystem\web\html\BingTuYear.html")

finally:
    if conn:
        conn.close()
webbrowser.open(r"D:\学习软件\IDEA\IntelliJ IDEA 2017.2.5\IJworkSpace\LibrarySystem\web\html\BingTuYear.html")
