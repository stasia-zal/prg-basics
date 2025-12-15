import csv

pattern='Graphic Designer'
print('GRAPHIC DESIGNERS\nimport=================')
with open('it_company.csv','r',encoding='utf-8') as file:
    content=csv.DictReader(file)
    for row in content:
        if row['Job Title']==pattern:
            print(row['First Name'],row['Last Name'],row['Email'])