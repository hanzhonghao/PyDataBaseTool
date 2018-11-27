import pyodbc
server = 'jdbc:sqlserver://ZIBJ904\\SQLEXPRESS'
database = 'uuid'
username = 'hanzhonghao'
password = 'hkhn5261RL'
cnxn = pyodbc.connect('DRIVER={SQL Server}',SERVER='jdbc:sqlserver://127.0.0.1',PORT=1443,DATABASE='NVCZodiac_mtl',UID='sa',PWD='hkhn5261')
cursor = cnxn.cursor()

print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO Employees (Name, Location) VALUES (?,?);"
with cursor.execute(tsql,'Jake','United States'):
    print ('Successfuly Inserted!')


#Update Query
print ('Updating Location for Nikita')
tsql = "UPDATE Employees SET Location = ? WHERE Name = ?"
with cursor.execute(tsql,'Sweden','Nikita'):
    print ('Successfuly Updated!')


#Delete Query
print ('Deleting user Jared')
tsql = "DELETE FROM Employees WHERE Name = ?"
with cursor.execute(tsql,'Jared'):
    print ('Successfuly Deleted!')


#Select Query
print ('Reading data from table')
tsql = "SELECT Name, Location FROM Employees;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()