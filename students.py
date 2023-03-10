import csv


def main():
    Dictionary = {"name": "Oscar", "Address": "Mexico"}
    print(Dictionary["name"])
    print(Dictionary["Address"])
    Dictionary["Phone"] = "8342158421"
    Dictionary['email'] = 'oscar@gmail.com'
    
    for element in Dictionary.items():
        print(f"{element[0]}: {element[1]}")


def read_dictionary(filename, key_column_index):
    pass
    # return ListDictionary

    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """


# Call main to start this program.
if __name__ == "__main__":
    main()
