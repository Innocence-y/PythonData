
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pyecharts import Line

import pymysql
import webbrowser

# 将数据库数据在网页上以条形图格式显示出来

host = "localhost"
port = 3306
user = "root"
passwd = "mysql"
charset = "utf8"
dbname = "test"
conn = None

try:
    conn = pymysql.Connection(
        host="localhost",
        port=3306,
        user="root",
        passwd="123456",
        db="librarysystem"
    )
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("select number  from sort;")
    rows = cur.fetchall()
    # rows = numpy.array(rows)
    attr = ["编程", "文学", "金融", "心理学", "医学", "历史", "小说", "军事", "法律", "体育"]
    lists = [[]]
    for row in rows:
        lists[0].append(row["number"])


    print(lists[0])

    v1 = lists[0]

    print(v1)

    line = Line("图书借阅-折线图-面积图")
    line.add("借阅", attr, v1, is_fill=True, area_color="#3A5FCD", line_opacity=0.3, area_opacity=0.4, is_smooth=True)
    line.show_config()
    line.render(r"D:\学习软件\IDEA\IntelliJ IDEA 2017.2.5\IJworkSpace\LibrarySystem\web\html\ZheXianMianJiTu.html")
finally:
    if conn:
        conn.close()
webbrowser.open(r"D:\学习软件\IDEA\IntelliJ IDEA 2017.2.5\IJworkSpace\LibrarySystem\web\html\ZheXianMianJiTu.html")