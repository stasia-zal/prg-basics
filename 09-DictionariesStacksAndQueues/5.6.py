basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}

person={}
def put_from(dic):
    for key,value in dic.items():
        person[key]=value

put_from(basic_data)
put_from(advanced_data)

for key,value in person.items():
    print(key,':',value)