import csv

with open('vehicle.txt','r',encoding='utf-8') as file:
    cars=file.read().split()

with open('province.csv','r', encoding='utf-8') as file:
    keyy=list(csv.DictReader(file))

letter_prov={}
counting={}

for row in keyy:
    letter_prov[row['Letter']]=row['Name']

for car in cars:
    first_letter=car[0]
    if first_letter in letter_prov:
        province=letter_prov[first_letter]
        counting[province]=counting.get(province,0)+1


for key in counting:
    print(key,':',counting[key])

if:



'''if car[0] in counting:
        counting[car[0]]+=1
    else:
        counting[car[0]]=1

for key,value in counting.items():
    for row in keyy:
        for v,k in row.items():
            key=k'''