
"""
File: tire_volume.py
Author: Oscar Rodriguez

Purpose: Prove that you can write a Python program that gets input from a user, 
performs arithmetic, and displays results for the user to see.


The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. The second number is the aspect ratio. 
The third number is the diameter in inches of the wheel that the tire fits. 
The volume of space inside a tire can be approximated with this formula:

v = 
π w2 aw a + 2,540 d
10,000,000,000
v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""
# Import the datetime class from the datetime
from datetime import datetime

#import math library
import math

# Get the size of a car tire
w=float(input("Enter the width of the tire in mm (ex 205): "))
a=float(input("Enter the aspect ratio of the tire (ex 60):"))
d=float(input("Enter the diameter of the wheel in inches (ex 15):"))

pricetext=""
answer=""
phone=""
prices=[[235,65,17,150.99],[245,55,18,113.93],[235, 65, 16, 109.35],[195, 65, 15, 60.99]]
for price in prices:
    if price[0]==w and price[1]==a and price[2]==d:
        print(f"The price of this tire is: ${price[3]}")
        pricetext=", $"+str(price[3])

        # Calculate 
        while answer!="yes" and answer!="no":
            answer=input("Do you want to buy this tire (yes/no)?").lower()
            if answer=="yes":
                phone=input("What is your phone number? ")
                phone=", "+phone

v=(math.pi*w**2*a*(w*a+2540*d))/10000000000

#print (f"The approximate volume is {v:.2f} liters")

# Call the now() method to get the current date and time as a datetime object from the computer's operating system.
current_date_and_time = datetime.now()

with open("volumes.txt", "at") as textfile:
    # Code to do something with each line goes here
    print(f"{current_date_and_time:%Y-%m-%d}, {w:.0f}, {a:.0f}, {d:.0f}, {v:.2f}{pricetext}{phone}", file=textfile)
    print("This data has been append to the file volumes.txt")

print("Thank you for using our systems!")