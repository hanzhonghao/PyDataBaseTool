import datetime
import csv

from DBTool import DB_helper
server = "127.0.0.1"
user = "hanzhonghao"
password = "hkhn5261RL"
database = "uuid"

filename = 'C:/Users/zhonghao.han/Desktop/test.csv'

BlackListed = 0
WhiteListed = 1
EntryDate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def initDB():
    global mssql
    mssql = DB_helper.MSSQL(server, user, password, database)

def query():
    rows = mssql.ExecQuery('select top (10) NMAID,UserID from AppNMDPAuthenticateUserPermissionList')
    print(rows)

def insert(NMAID,UserID):
    mssql.ExecNonQuery("insert into AppNMDPAuthenticateUserPermissionList(NMAID, UserID, BlackListed, WhiteListed, EntryDate) values ('%s','%s','%d','%d','%s')" % (NMAID,UserID, BlackListed, WhiteListed, EntryDate))

def getWhiteListAndInsertDB():
    with open(filename) as f:
        reader = csv.reader(f)
        #Line Numbers start with line 2
        next(reader)
        i=0
        for row in reader:
            i = i + 1
            NMAID=row[0]
            UserID=row[1]
            print(' ')
            print('NMAID : '+NMAID + '     UserID : '+UserID )
            insert(NMAID,UserID)
            print('Insert DB successful !  Insert ',i,' times' )
    f.close()

if __name__ == '__main__':
    initDB()
    getWhiteListAndInsertDB()
    # query()
