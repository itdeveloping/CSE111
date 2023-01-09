import math
def calculate(items, itemsperbox):
    return math.ceil(items/itemsperbox)


items=int(input("Enter the number of items: "))
itemsperbox=int(input("Enter the number of items per box: "))
totalboxes=calculate(items,itemsperbox)

print (f"For {items} items, packing {itemsperbox} items in each box, you will need {totalboxes} boxes.")
