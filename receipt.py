
"""
File: receipt.py
Author: Oscar Rodriguez

Purpose: Prove that you can write a Python program that handles exceptions, including FileNotFoundError, PermissionError, and KeyError.

"""
# Import libraries

import csv
import random
from datetime import datetime


def main():

    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    #define a variable for Filename
    Filename="products.csv"

    #define column index and call the Dictionary function
    KeyColumnIndex=0
    Dictionary=read_dictionary(Filename,KeyColumnIndex)

    #Manage exceptions for File not found
    try:
        Filename="request.csv"

        with open(Filename, "rt") as CVSFile:
            print("Rodriguez enterprise!")
            print("")
            NameIndex=1
            PriceIndex=2
            Items = 0
            Subtotal=0            
            Reader = csv.reader(CVSFile)
            next(Reader)
            #Manage exception for Value error
            try:
                #Create a list of items to use for print a coupon
                ItemList=[]
                
                #Loop for reading the file
                for RowList in Reader:
                    Key = RowList[0]
                    Quantity=RowList[1]           
                    Items+=int(Quantity)
                    Subtotal+=float(Quantity)*float(Dictionary[Key][PriceIndex])
                    #if item found is added to the list of items
                    if Key in Dictionary:
                        ItemList.append(Dictionary[Key][NameIndex])
                    #print the name if item, quantity and price
                    print(f"{Dictionary[Key][NameIndex]}: {Quantity} @ {Dictionary[Key][PriceIndex]}")
            #if KeyError print a message
            except:
                print(f"Error: unknown product ID '{Key}' in the request.csv file. This item could not be added to your cart.")

        # get current datetime
        dt = datetime.now()
        # get weekday name
        day=dt.strftime('%A')
        hour=dt.strftime('%H')

        #print the shopping summary
        print(f"\nNumber of Items: {Items}")
        print(f"Subtotal: {Subtotal:.2f}")        
        
        #chech if discount applies
        ApplyDiscount=False
        if day in ("Tuesday","Wednesday"):
            Discount=Subtotal*0.1
            ApplyDiscount=True
            Subtotal=Subtotal-Discount
            
        if int(hour)<=11:
            Discount=Subtotal*0.1
            ApplyDiscount=True
            Subtotal=Subtotal-Discount
        
        #calculate tax and total
        SalesTax=Subtotal*0.06
        Total=Subtotal+SalesTax

        if ApplyDiscount==True:
            print(f"Discount: {Discount:.2f}")
            print(f"Subtotal: {Subtotal:.2f}")

        #print tax and total
        print(f"Sales Tax: {SalesTax:.2f}")
        print(f"Total: {Total:.2f}")
        print("")
        #call the function PrintCupon
        PrintCupon(ItemList)
        #final message, time and invitation for a survey
        print("\nThank you for shopping at the Rodriguez enterprise!")
        print(f"{current_date_and_time:%A %I:%M %p - %B %d, %Y}")
        print("Please participate in our Customer Satisfaction Survey at https://www.rodriguezenterprise.com")
    #if file not found print an error message
    except FileNotFoundError as e:
        print(f"{e}")

def PrintCupon(List):
        #use random built-in function to select and item
        RandomNumber=random.uniform(0, len(List)-1)
        ItemIndex=round(RandomNumber)

        #print coupon
        print("**************")
        print("Congratulations!")
        print(f"You got a cupon for this product: {List[ItemIndex]}")
        print("**************")
        pass

def read_dictionary(Filename, KeyColumnIndex):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        Filename: the name of the CSV file to read.
        KeyColumnIndex: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    Dictionary = {}
    
    with open(Filename, "rt") as CVSFile:
        Reader = csv.reader(CVSFile)
        next(Reader)
        for RowList in Reader:
            Key = RowList[KeyColumnIndex]
            Dictionary[Key] = RowList
    return Dictionary
    pass

    # Call main to start this program.
if __name__ == "__main__":
    main()