dis=int(input('Enter distance in km: '))
hour=int(input('Enter number of travel hours: '))
min=int(input('Enter number of travel minutes: '))
def avg_speed(distance,hours,minutes):
    res=distance/(hours+minutes/60)
    return res
print(f'Average speed: {avg_speed(dis,hour,min):.1f} km/h ')