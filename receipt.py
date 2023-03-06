import csv

def main():
    filename="products.csv"
    key_column_index=0
    Dictionary=read_dictionary(filename,key_column_index)
    #print(Dictionary)
    ProductNumber=Dictionary['P020'][0]
    ProductName=Dictionary['P020'][1]
    ProductPrice=Dictionary['P020'][2]

    #print(f"{ProductNumber} {ProductName} {ProductPrice}")

    filename="request.csv"
    NameIndex=1
    PriceIndex=2
    with open(filename, "rt") as CVSFile:
        Reader = csv.reader(CVSFile)
        next(Reader)
        for RowList in Reader:
            Key = RowList[0]
            Quantity=RowList[1]
            print(f"{Dictionary[Key][NameIndex]}: {Quantity} @ {Dictionary[Key][PriceIndex]}")
            
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