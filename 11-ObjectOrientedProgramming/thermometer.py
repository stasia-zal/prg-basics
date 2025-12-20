import random

class Therm:
    def __init__(self):
        self.temperature=0.0
        self.is_on=False
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def measure(self):
        if self.is_on:
            self.temperature=random.randint(340,420)/10
            status=''
            if self.temperature>37 and self.temperature<41:
                status='fever'
            elif self.temperature>=41:
                status='CRITICAL TEMPERATURE!!'
            print(f'Temperature: {self.temperature} {status}')
        else:
            print('Thermometer is off!')