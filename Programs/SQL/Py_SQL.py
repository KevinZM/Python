# -*- coding:utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'rootroot',
    db = 'test',
)

cur = conn.cursor()

#cur.execute("create table student(id INT ,name VARCHAR (20),class VARCHAR (30),age VARCHAR (10))")

cur.execute("insert into student VALUES ('3','Tom','3 grade 2 class','9')")

cur.execute("update student set class = '3 grade 1 class' where name = 'Tom'")

#cur.execute("delete from student where age = '9'")

a = cur.execute("select * from student")
for i in range(a):

    print cur.fetchone()

cur.close()
conn.commit()
conn.close()