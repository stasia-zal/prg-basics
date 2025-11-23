arr=[7,9,2,4,5,6]
num=int(input('Enter the number: '))
count=0
for i in arr:
    if i>num:
        count+=1
print(count)