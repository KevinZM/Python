# coding=utf-8
import re
import sys
import urllib

import MySQLdb


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def Schedule(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print '>'+'%.2f%%' % per,'\b\b'
    if per == 100:
        print "*" * 10, "下载完成!", "*" * 10


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, './images/%s.jpg' % x, Schedule)
        print x + 1
        x += 1


html = getHtml("http://tieba.baidu.com/p/2438181810")
# getImg(html)


try:
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='rootroot',
        db='test',
    )
    cur = conn.cursor()
    print "建立数据库连接!"
    # cur.execute("CREATE TABLE Images(id INT PRIMARY KEY AUTO_INCREMENT,Data MEDIUMBLOB);")
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x, Schedule)
        fp = open("./%s.jpg" % x)
        img = fp.read()
        print x + 1
        cur.execute("insert into Images SET data  = '%s'" % MySQLdb.escape_string(img))
        print "插入%s条数据" % (x + 1)
        fp.close()
        x += 1

    cur.close()
    conn.commit()
    conn.close()
    print "关闭数据库连接!"
except MySQLdb.Error, e:
    print "Error %d %s" % (e.args[0], e.args[1])
    sys.exit(1)

try:
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='rootroot',
        db='test',
    )
    cur = conn.cursor()
    # cur.execute("CREATE TABLE Images(id INT PRIMARY KEY AUTO_INCREMENT,Data MEDIUMBLOB);")
    print "建立数据库连接!"
    a = cur.execute("SELECT data FROM Images")
    print "查询数据库表中数据条数!"
    print a
    cur.execute("SELECT data FROM Images")
    print "选取数据库数据!"
    x = 0
    for i in range(a):
        d = cur.fetchone()[0]
        fp = open("/Users/zhangmin/Desktop/py/%s.jpg" % i, "wb")
        fp.write(d)
        print "写入硬盘!"
        fp.close()

    cur.close()
    conn.close()
    print "关闭数据库连接!"
except MySQLdb.Error, e:
    print "Error %d %s" % (e.args[0], e.args[1])
    sys.exit(1)
