def f(cars, order):
    if order == 1:
        return sorted(cars, key=lambda car: list(car.keys())[0])
    elif order == 2:
        return sorted(cars, key=lambda car: list(car.values())[0], reverse=True)
    

cars = [{"KR333": 138}, {"WL555": 497}, {"DB444": 341}, {"MC222": 412}]
print(f(cars,1))
print(f(cars,2))

