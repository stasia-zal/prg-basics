countries = [
    {"name": "Poland", "population": 38000000},
    {"name": "Germany", "population": 83000000},
    {"name": "France", "population": 67000000},
    {"name": "Ukraine", "population": 41000000},
    {"name": "Spain", "population": 47000000}
]
print(countries)
for dic in countries:
    for item,value in dic.items():
        print(item,":",value)