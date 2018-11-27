import pymssql
conn = pymssql.connect(host='127.0.0.1',user='hanzhonghao',
                       password='hkhn5261RL',database='uuid',
                      charset="utf8")
#查看连接是否成功
print(conn)
cursor = conn.cursor()
sql = 'select top (1000) UUID,NMAID from UUIDTab1 '
cursor.execute(sql)
#用一个rs变量获取数据
rs = cursor.fetchall()
print(rs)



# def main():
#     # CreateTable()
#
#     conn.close()
#
# if __name__ == '__main__':
#     main()