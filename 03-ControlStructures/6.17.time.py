import sys


eu=input("Enter time (24-hour format): ")
if len(eu)<5:
    print(f"Time in 12-hour format: {eu}am")
    sys.exit() 
hour=int(eu[0:2])
print(hour)
min=int(eu[3:5])
print(hour,min)
if hour>11:
    hour-=12
    print(f"Time in 12-hour format: {hour}:{min}pm")
else:
    print(f"Time in 12-hour format: {eu}am")