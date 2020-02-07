#GITHUB Connect to a SQL database and read out the data

import MySQLdb

db = MySQLdb.connect(host="192.168.0.224", user="logcal20", passwd="password", db="school")
cur = db.cursor(MySQLdb.cursors.DictCursor)
 
name = input("Please enter student's name. ")
age = input("Please enter student's age. ")
gradeLevel = input("Please enter student's grade level. ")

def createLOG ( input1, input2, input3):
	intro = f"My name is {name}. I am in grade {gradeLevel} and {age} years  old."
	print (intro)

new = createLOG(name, age, gradeLevel)

def insertLog(input1, input2, input3):
	sql = f"INSERT INTO students (name, age, gradeLevel) VALUES ('{input1}', '{input2}', '{input3}')"
	cur.execute(sql)
insertLog(name,age,gradeLevel)


	
sql = "SELECT * FROM students"
cur.execute(sql)

rows = cur.fetchall()
for row in rows:
	print("My name is "+row['name']+". I am in grade "+str(row['gradeLevel'])+ " and " +str(row['age']) +" years  old.")
	print(type(name))


def func121(num1):
	year = 2019
	num2 = year - int(num1)
	num3 = "The year you where born was " + str(num2)
	return num3 

newFUNC12 = func121(age)
print(newFUNC12)

cur.close()
db.close()
