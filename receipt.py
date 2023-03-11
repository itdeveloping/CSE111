import csv
import random

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime


def main():

    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    filename="products.csv"
    key_column_index=0

    Dictionary=read_dictionary(filename,key_column_index)

    try:
        filename="request.csv"

        with open(filename, "rt") as CVSFile:
            print("Rodriguez enterprise!")
            print("")
            NameIndex=1
            PriceIndex=2
            Items = 0
            Subtotal=0            
            Reader = csv.reader(CVSFile)
            next(Reader)
            try:
                ItemList=[]
                for RowList in Reader:
                    Key = RowList[0]
                    Quantity=RowList[1]           
                    Items+=int(Quantity)
                    Subtotal+=float(Quantity)*float(Dictionary[Key][PriceIndex])
                    if Key in Dictionary:
                        ItemList.append(Dictionary[Key][NameIndex])
                    print(f"{Dictionary[Key][NameIndex]}: {Quantity} @ {Dictionary[Key][PriceIndex]}")
            except:
                print(f"Error: unknown product ID '{Key}' in the request.csv file. This item could not be added to your cart.")
        # get current datetime
        dt = datetime.now()

        # get weekday name
        day=dt.strftime('%A')
        hour=dt.strftime('%H')
        print(f"\nNumber of Items: {Items}")
        print(f"Subtotal: {Subtotal:.2f}")        
        
        ApplyDiscount=False
        if day in ("Tuesday","Wednesday"):
            Discount=Subtotal*0.1
            ApplyDiscount=True
            Subtotal=Subtotal-Discount
            
        if int(hour)<=11:
            Discount=Subtotal*0.1
            ApplyDiscount=True
            Subtotal=Subtotal-Discount
            
        SalesTax=Subtotal*0.06
        Total=Subtotal+SalesTax

        if ApplyDiscount==True:
            print(f"Discount: {Discount:.2f}")
            print(f"Subtotal: {Subtotal:.2f}")

        print(f"Sales Tax: {SalesTax:.2f}")
        print(f"Total: {Total:.2f}")
        print("")
        # Use an f-string to print the current
        # day of the week and the current time.
        PrintCupon(ItemList)
        print("\nThank you for shopping at the Rodriguez enterprise!")
        print(f"{current_date_and_time:%A %I:%M %p - %B %d, %Y}")
        print("Please participate in our Customer Satisfaction Survey at https://www.rodriguezenterprise.com")

    except FileNotFoundError as e:
        print(f"{e}")

def PrintCupon(List):
        
        RandomNumber=random.uniform(0, len(List)-1)
        ItemIndex=round(RandomNumber)
        print("**************")
        print("Congratulations!")
        print(f"You got a cupon for this product: {List[ItemIndex]}")
        print("**************")
        pass

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    Dictionary = {}
    
    with open(filename, "rt") as CVSFile:
        Reader = csv.reader(CVSFile)
        next(Reader)
        for RowList in Reader:
            Key = RowList[key_column_index]
            Dictionary[Key] = RowList
    return Dictionary
    pass

    # Call main to start this program.
if __name__ == "__main__":
    main()