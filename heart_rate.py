
"""
File: heart_rate.py
Author: Oscar Rodriguez

Purpose: Write a Python program that gets input from a user, uses variables, performs arithmetic, and displays results for the user to see.

When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

# Get the user's age as a int.
age=int(input("Please enter your age: "))

# Calculate the heart rate, min and max
heart_rate=220-age
min_rate=int(heart_rate*0.65)
max_rate=int(heart_rate*.85)

# Display the results
print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {min_rate} and {max_rate} beats per minute.")