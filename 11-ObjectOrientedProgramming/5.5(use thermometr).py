from thermometer import Therm

def main():
    thermometer=Therm()
    thermometer.turn_on()
    thermometer.measure()
    thermometer.turn_off()

if __name__=='__main__':
    main()