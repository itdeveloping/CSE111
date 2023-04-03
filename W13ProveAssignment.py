"""" File: W13ProveAssignment.py
Author: Oscar Rodriguez

Purpose: Prove that you can write a significant Python project that solves a real-world problem and is well organized with functions.

 """

from datetime import datetime
import csv, os, mysql.connector
from mysql.connector import errorcode


cnx=True
cursor=True

def dbConnect(user_, password_, host_, database_):
    try:
        cnx = mysql.connector.connect(user=user_, password=password_,
                                host=host_,
                                database=database_)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        elif err:
            print(err)
        else:
            print("Connection success!")
    return cnx, cnx.cursor()
   

def dbSelect(cursor, query):
    os.system('cls')
   
    #cursor.execute(query, (hire_start, hire_end))
    cursor.execute(query)
    LoansQuantity=0
    LoansAmount=0
    print("Loans information from database:")
    print(f"Id: Loan type:  Date:        Amount ($): ")
    for (id,loan, loan_date, amount) in cursor:
        print(f"{id: <3} {loan: <11} {loan_date}   $ {amount:.2f}")
        LoansQuantity+=1
        LoansAmount+=amount
    LoansAverage=LoansAmount/LoansQuantity
    print(f"Total loans quantity: {LoansQuantity}")
    print(f"Total loans amount: $ {LoansAmount:.2f}")
    print(f"Total loans average: $ {LoansAverage:.2f}")
    input("\nHit <enter> to continue...")
    os.system('cls')

def dbUpdate(cnx,LoanType, LoanDate, Amount,Id):

    curB = cnx.cursor(buffered=True)
    UpdateId = ("update loan set loan=%s, loan_date=%s, amount=%s where id=%s")
    curB.execute(UpdateId, ( LoanType, LoanDate, Amount, Id))    
    print (f"The loan id[{Id}] was updated!\n")
    print("---------")

    # Commit the changes
    cnx.commit()


def dbInsert(cnx,LoanType,LoanDate,Amount):

    curB = cnx.cursor(buffered=True)
    insert_new_row = ("insert into loan (loan, loan_date, amount) values (%s, %s, %s)")
    curB.execute(insert_new_row, ( LoanType, LoanDate, Amount))

    # Commit the changes
    cnx.commit()
    input("\nYour data have been saved. Hit <enter> to continue...")

def dbDelete(cnx,Id):
    curB = cnx.cursor(buffered=True)
    DeleteId = (f"delete from loan where id={Id}")
    curB.execute(DeleteId)

    # Commit the changes
    cnx.commit()
    print(f"The loan id: [{Id}] was deleted!. Hit <enter> to continue...")

def dbCheckId(cnx,Id):
    curB = cnx.cursor(buffered=True)
    curB.execute(
        "SELECT * FROM loan WHERE id = %s",
        (Id,)
    )
    # gets the number of rows affected by the command executed
    row_count = curB.rowcount
    if row_count == 0:
        return False
    else:
        return True
    
def dbToFile(cursor, query,FileName):
    os.system('cls')
    # open the file in the write mode
    f = open(FileName+'.csv', 'w', newline='')

    # create the csv writer
    writer = csv.writer(f)
    row=['Id:','Loan:','Date:','Amount:']
    writer.writerow(row)
   
    #cursor.execute(query, (hire_start, hire_end))
    cursor.execute(query)

    for (id,loan, loan_date, amount) in cursor:
        row=id,loan,loan_date,amount
        writer.writerow(row)
    # close the file
    f.close()
    print(f"The data from database was transfered to file {FileName}.csv")
    input("\nHit <enter> to continue...")
    os.system('cls')
    # write a row to the csv file


def dbClose(cnx, cursor):
    if cnx and cursor:
        cursor.close()
        cnx.close()
    print("Database connection is closed!")
    print("Thank you for using our systems!")

def OptionsFromFile(filename):
    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)
        for row in reader:

            print(f"{row[0]} {row[1]}")
    print("----------")

def OptionsMenu():
    os.system('cls')
    cnx, cursor=dbConnect('dbuser', 'ABCD1234#','127.0.0.1','dbloan')
    print("You are already connect to database!\n")    
    OptionsFromFile("OptionsMenu.csv")
    try:
        option=int(input("Select an option [1-6]: "))
    except:
        os.system('cls')
        print(f"------------ Error: Please select a valid option!") 
        option=10
    while option!=6:
        if option==1:
            dbSelect(cursor,"select * from loan order by id")
        elif option==2:
            os.system('cls')
            print("Insert a new record. Please type the following information:\n")
            LoanType=input("Type the name of the loan: ")
            Amount=float(input("Type the amount of the loan: "))
            LoanDate=datetime.now()
            dbInsert(cnx, LoanType, LoanDate, Amount)
            os.system('cls')
        elif option==3:
            os.system('cls')
            Id=int(input("Type the loan id to delete: "))
            if dbCheckId(cnx,Id)==True:
                dbDelete(cnx,Id)
            else:
                print("---------")
                print (f"The loan id:[{Id}] does not exist. Please try again!")
                print("---------")                
        elif option==4:
            os.system('cls')
            Id=int(input("Type the loan id to update: "))
            if dbCheckId(cnx,Id)==True:
                print("---------")
                print(f"Loan id: [{Id}] found, please type the following information:")
                LoanType=input("Type the name of the loan: ")
                Amount=float(input("Type the amount of the loan: "))
                LoanDate=datetime.now()
                dbUpdate(cnx,LoanType, LoanDate, Amount, Id)
            else:
                print("---------")
                print (f"The loan id:[{Id}] does not exist. Please try again!")
                print("---------")
        elif option==5:
            FileName=input("Type the name of the file for transfering data: ")
            dbToFile(cursor,"select * from loan order by id",FileName)
        else:
            os.system('cls')           
        try:

            OptionsFromFile("OptionsMenu.csv")
            option=int(input("Select an option [1-6]: "))
        except:
            input("------------ Error: Please select a valid option [1-6]! Hit <enter> to continue...") 
            os.system('cls')
               
             
    dbClose(cnx,cursor)

def main():
  OptionsMenu()
  
  #dbInsert(cnx,'New2','2023-03-03',8500)
  #dbSelect(cursor,"select * from loans")

  pass

if __name__ == "__main__":
    main()
