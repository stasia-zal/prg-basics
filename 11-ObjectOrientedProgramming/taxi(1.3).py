class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f'---------------------------')
        print(f'Distance:  {self.distance} km')
        print(f'Rate:  {self.rate_per_km} pln per km')
        print(f'Fare:  {self.fare} pln')


def main():
    # your program
    ride=TaxiRide(4)
    ride.calculate_fare(15)
    ride.print_receipt()
    print()
    print('------------------')
    ride=TaxiRide(10)
    ride.calculate_fare(2)
    ride.print_receipt()


if __name__ == "__main__":
    main()
