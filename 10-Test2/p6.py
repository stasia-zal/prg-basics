import json
def f(years, course, average_grade):
    count=0
    with open('data.json','r',encoding='utf-8') as file:
        data=json.load(file)
    for student in data:
        if int(student['year'])>=years:
            if student['course']==course:
                if int(student['average'])>=average_grade:
                    count+=1
    return count