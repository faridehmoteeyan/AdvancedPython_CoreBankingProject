import sqlite3

class UserDataAccess():

    def get_user_username_and_password(self, username,password):
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
and Password = ? """,(username,password))
            row = cursor.fetchone()
            print(row)
