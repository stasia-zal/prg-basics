def ms_to_kmh(ms):
    res=ms*3.6
    return res

n1 = int(input('Enter speed in m/s: '))
print(f'It is {ms_to_kmh(n1)} km/h')