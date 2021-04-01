import mysql.connector

mydb = mysql.connector.connect(
	host ='localhost',
	user ='root',
	password ='Rithic@2002',
	database ='attendance'
	)
mycursor = mydb.cursor()
Name = input("Enter the name of the user")
Present_or_absent = input("Enter the attendance of the user")
Reg_No = input("Enter the registration number")

sql = "INSERT INTO daily_record(Name,Status,Registration_Number) VALUES(%s,%s,%s)"
val = (Name,Present_or_absent,Reg_No)
mycursor.execute(sql,val)
mydb.commit()