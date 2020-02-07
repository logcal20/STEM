#GITHUB Insert into a SQL database.
import MySQLdb

db = MySQLdb.connect(host="localhost", user="logcal20", passwd="password", db="school")
cur = db.cursor(MySQLdb.cursors.DictCursor)
 
name = input("Please enter student's name. ")
age = input("Please enter student's age. ")
gradeLevel = input("Please enter student's grade level. ")

def insertLog(input1, input2, input3):
	sql = f"INSERT INTO students (name, age, gradeLevel) VALUES ('{input1}', '{input2}', '{input3}')"
	cur.execute(sql)
insertLog(name,age,gradeLevel)


cur.close()
db.close()
