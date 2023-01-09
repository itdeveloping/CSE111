from datetime import datetime


""""

If the subtotal is $50 or greater and today is Tuesday or , your program must subtract 10% from the subtotal. Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.

"""

subtotal=float(input("Please enter the subtotal: "))
# get current datetime
dt = datetime.now()

# get weekday name
day=dt.strftime('%A')
applydiscount=False
if day in ("Tuesday","Wednesday"):
    if subtotal>=50:
        applydiscount=True

if applydiscount==True:
    print(f"Today you have a discount because today is {day} and your amount is more than $50")
    discount=subtotal*0.1
    print(f"Discount amount: {discount:.2f}")
    tax=(subtotal-discount)*.06
    print (f"Sales tax amount: {tax:.2f}")
    total=subtotal-discount+tax
    print (f"Total: {total:.2f}")
else:
    tax=subtotal*.06
    print (f"Sales tax amount: {tax:.2f}")
    total=subtotal+tax
    print (f"Total: {total:.2f}")  

print("")
