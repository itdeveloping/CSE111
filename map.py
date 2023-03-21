import csv
import mysql.connector
import json

class DatabaseGateway:

    def db_connect(self):

        db_con = mysql.connector.connect(
                    host     = "localhost",
                    user     = "dbuser",
                    password = "Abril2010",
                    database = "loans"
                 )

        # db_cursor = db_con.cursor()

        return db_con

    def db_query(self, query_string):

        my_db    = self.db_connect()
        mycursor = my_db.cursor()
        mycursor.execute(query_string)

        columns = mycursor.description
        data  = []

        for row in mycursor.fetchall():

            row_data = {}

            for (column_name, column_value) in enumerate(row):

                row_data[columns[column_name][0]] = column_value

            data.append(row_data)

        json_object = json.dumps(data)

        return json.dumps(json.loads(json_object), indent = 2) 

    def db_execute(self, query_string, data):

        my_db = self.db_connect()
        mycursor = my_db.cursor()
        mycursor.execute(query_string, data)
        my_db.commit()

        self.lastrowid = str(mycursor.lastrowid)

def main():
    NewList=ReadList("products.csv")
    print(NewList)


def ReadList(filename):
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            compound_list.append(row)
    return compound_list
    
if __name__ == "__main__":
    main()