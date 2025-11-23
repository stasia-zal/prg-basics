arr=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
max=arr[0]
for i in range(len(arr)-1):
    if len(arr[i])>len(max):
        max=arr[i]
print(max)