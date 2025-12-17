import json

with open('reservations.json','r',encoding='utf-8') as file:
    content=json.load(file)
    reservations=content["reservations"]
        #resul=resul.value()

def roo():
    rooms=0
    for reserv in reservations:
        rooms+=1
    print(rooms,'rooms')

def num_paid():
    paid=0
    for reserv in reservations:
        if reserv['paid']:
            paid+=1
    print(paid,'paid rooms')

def num_unpaid():
    unpaid=0
    for reserv in reservations:
        if not reserv['paid']:
            unpaid+=1
    print(unpaid,'unpaid rooms')

def value_paid():
    total=0
    for reserv in reservations:
        if reserv['paid']:
            total+=reserv["price_per_night"]
    print(total,'total value of paid rooms')

def value_unpaid():
    total=0
    for reserv in reservations:
        if not reserv['paid']:
            total+=reserv["price_per_night"]
    print(total,'total value of unpaid rooms')

roo()
num_paid()
num_unpaid()
value_paid()
value_unpaid()