import datetime
import csv

import sys
import pymssql

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
    mssql = MSSQL(server, user, password, database)


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

class MyException(Exception):

    def __init__(self, *args):
        self.args = args


class SqlException(MyException):
    def __init__(self, message='The table is not exist', args=('SqlException',)):
        self.args = args
        self.message = message


class MSSQL:
    def __init__(self, host, user, pwd, db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        self.conn = pymssql.connect(host=self.host, user=self.user, password=self.pwd, database=self.db, charset='utf8')
        cur = self.conn.cursor()
        if not cur:
            return (NameError, "connect db failed")
        else:
            return cur

    # Executing the query returns a list containing a tuple, the element of the list is the row of record,
    # and the element of the tuple is the field of each row of record
    def ExecQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()
        self.conn.close()
        return resList

    def ExecNonQuery(self, sql):
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    initDB()
    isDBExist()
    # getWhiteListAndInsertDB()
    query()
