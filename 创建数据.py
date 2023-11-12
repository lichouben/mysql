import pymysql
from pymysql import cursors

while True:
    num = input("price:")
    if num.upper() == 'Q':
        break
    # 连接数据库
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='yy2039070', charset='utf8',db='a1')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


    # 2.发送命令
    sql ="insert into tb2(salary) values(%s)"
    cursor.execute(sql,[num])

    # sql ="insert into tb2(salary) values(%(n1)s)"
    # cursor.execute(sql, {"n1":"5.33"})

    conn.commit()


# 关闭
cursor.close()
conn.close()