import pymysql

# 连接数据库
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='yy2039070', charset='utf8',db='a1')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 2.发送命令
cursor.execute("select * from tb2 where id > %s",[2,])
data_list = cursor.fetchall()
for row in data_list:
    print(row)



cursor.close()
conn.close()