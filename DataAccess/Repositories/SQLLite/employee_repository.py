import sqlite3

from Common.Entities.employee import Employee
from Common.Repositories.iemployee_repository import IEmployeeRepository

class SQLLiteEmployeeRepository(IEmployeeRepository):
    def get_by_username_pasword(self,username:str,password:str)->Employee:
        with sqlite3.connect("CoreBanking.db") as connection:
            cursor = connection.cursor()
            cursor.execute(f"""SELECT id,
                   FirstName,
                   LastName,
                   UsearName,
                   Password,
                   Status
              FROM users
            where UsearName = ?
            and Password = ? """, (username, password))
            row = cursor.fetchone()
            return Employee(row[0],row[1],row[2],row[3],row[4],row[5])
    def insert_into_db(self,employee:Employee):
       with sqlite3.connect("CoreBanking.db") as connection:
           cursor = connection.cursor()
           cursor.execute(f"""INSERT...""")