import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(host='sql6.freemysqlhosting.net',database='sql6458625',user='sql6458625',password='PpFuFC8nPT')
mycursor = mydb.cursor()

sql = "UPDATE users SET email = 'danieldg007@gmail.com' WHERE username = 'Y21A0117'"

mycursor.execute(sql)
mydb.commit()
mycursor.close()
mydb.close()