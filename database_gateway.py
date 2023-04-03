import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(user='dbuser', password='ABCD1234#',
                              host='127.0.0.1',
                              database='loans')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print("Connection success!")
  #cnx.close()

import datetime
import mysql.connector

#cnx = mysql.connector.connect(user='scott', database='employees')
cursor = cnx.cursor()

query = ("select * from loans")

#hire_start = datetime.date(1999, 1, 1)
#hire_end = datetime.date(1999, 12, 31)

#cursor.execute(query, (hire_start, hire_end))
cursor.execute(query)

for (id,loan, loan_date, quantity) in cursor:
  print(f"Id: {id}, Loan type: {loan}, Date: {loan_date}, Quantity:  ${quantity}")

curB = cnx.cursor(buffered=True)

insert_new_row = (
  "INSERT INTO loans (loan, loan_date, quantity) "
  "VALUES (%s, %s, %s)")
curB.execute(insert_new_row,
               ('ExtraOrdinary', '2023-03-30', 8500))

  # Commit the changes
cnx.commit()

query = ("select * from loans order by loan")

cursor.execute(query)

for (id,loan, loan_date, quantity) in cursor:
  print(f"Id: {id}, Loan type: {loan}, Date: {loan_date}, Quantity:  ${quantity}")

cursor.close()
cnx.close()