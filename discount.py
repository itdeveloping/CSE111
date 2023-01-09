from datetime import datetime

# get current datetime
dt = datetime.now()

# get weekday name
day=dt.strftime('%A')
if day=="Sunday" or day=="Monday":
    print("Today is a discount")
