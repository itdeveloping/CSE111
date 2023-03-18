
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='174.136.28.103:3306',
                                         database='autosuf1_misfinanzas',
                                         user='autosuf1_dbuser',
                                         password='Abril072010')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

'''
response = requests.get('https://api.github.com')

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
Label = tk.Label(text="Name")
entry = tk.Entry()
Label.pack()
entry.pack()
greeting.pack()
window.mainloop()
'''