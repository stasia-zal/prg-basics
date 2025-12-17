import csv
def f(value):
    count=0
    with open('data.csv','r',encoding='utf-8') as file:
        content=list(csv.DictReader(file))
    for dic in content:
        if int(dic['Salary'])>=value:
            count+=1
    return count