import datetime
import csv

import sys

from DBTool import DB_helper
from DBTool.CustomException import SqlException

# DB connect config
server = "127.0.0.1"
user = "hanzhonghao"
password = "hkhn5261RL"
database = "uuid"

#DB Table config
DBTableName = 'AppNMDPAuthenticateUserPermissionList'

# .csv file pathconfig
filename = 'C:/Users/zhonghao.han/Desktop/test.csv'

#DB default value
BlackListed = 0
WhiteListed = 1
EntryDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def initDB():
    global mssql
    mssql = DB_helper.MSSQL(server, user, password, database)


def query():
    rows = mssql.ExecQuery('select top (100) NMAID, UserID from {}'.format(DBTableName))
    print(' ')
    print('The following content is the result of the query: ')
    print(' ')
    i = 0
    for row in rows:
        i = i + 1
        print('id :', i, '     NMAID : ' + row[0] + '     UserID : ' + row[1])


def insert(NMAID, UserID):
    mssql.ExecNonQuery(
        "insert into {}(NMAID, UserID, BlackListed, WhiteListed, EntryDate) values ('%s','%s','%d','%d','%s')"
        .format(DBTableName) % (NMAID, UserID, BlackListed, WhiteListed, EntryDate))


def getWhiteListAndInsertDB():
    with open(filename) as f:
        reader = csv.reader(f)
        # Line Numbers start with line 2
        next(reader)
        i = 0
        for row in reader:
            i = i + 1
            NMAID = row[0]
            UserID = row[1]
            print(' ')
            print('NMAID : ' + NMAID + '     UserID : ' + UserID)
            insert(NMAID, UserID)
            print('Insert DB successful !  Insert ', i, ' times')
    f.close()


def isDBExist():
    tableName = ''
    try:
        sql = "select * from information_schema.tables where table_schema='dbo' and  table_name = 'AppNMDPAuthenticateUserPermissionList'"
        results = mssql.ExecQuery(sql)
        for result in results:
            tableName = result[2]
        if tableName == '':
            raise SqlException()
    except SqlException as e:
        print('An exception occurs: ')
        print('The exception type is--->', e)
        print('The exception error message is--->', e.message)
        sys.exit(1)
    else:
        print('Ready insert data into DB')


if __name__ == '__main__':
    initDB()
    isDBExist()
    getWhiteListAndInsertDB()
    query()
