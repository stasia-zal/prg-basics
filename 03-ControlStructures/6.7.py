age=int(input("Enter your age: "))
if age<13:
    group="child"
elif age<=19:
    group="teen"
elif age<=64:
    group="adult"
elif age<122:
    group="senior"  
else:
    group="dead"
print(f"You are {age} years old, you are {group}")
