import csv

with open('clothing.csv','r',encoding='utf-8') as file:
    reader=csv.DictReader(file)
    print(','.join(reader.fieldnames))
    for row in reader:
        if float(row['Price']) > 60 and float(row['Stock_Quantity']) < 40:
            print(','.join(row.values()))