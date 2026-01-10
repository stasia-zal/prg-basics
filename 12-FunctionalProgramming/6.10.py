import matplotlib.pyplot as plt

data={"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

cities=list(map(lambda x:x,data.keys()))

temp=list(map(lambda x:x,data.values()))

plt.bar(cities, temp)
plt.title("Temperatures recorded in cities")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.show()