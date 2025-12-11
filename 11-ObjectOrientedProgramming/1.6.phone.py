class Phone():
    def __init__(self,battery,volume,is_locked):
        self.battery=battery
        self.volume=volume
        self.is_locked=is_locked
        
    def charge(self,amount):
        self.battery=min(100, self.battery+amount)
        print(f"Charging... Battery is now {self.battery}%")
    
    def lock(self):
        self.is_locked=True
        print("The phone is now unlocked.")

    def unlock(self):
        self.is_locked=False
        print("The phone is now unlocked.")

    def increase_v(self,amount):
        self.volume=min(100, self.volume + amount)
        print(f"Volume increased to {self.volume}")

    def decrease_v(self,amount):
        self.volume=max(0, self.volume - amount)
        print(f"Volume decreased to {self.volume}")

    def show_status(self):
        print("\n--- PHONE STATUS ---")
        print(f"Battery: {self.battery_level}%")
        print(f"Volume: {self.volume}")
        print(f"Locked: {self.is_locked}")
        print("--------------------")


def main():
    my_phone=Phone(35,2,True)
    my_phone.unlock()
    my_phone.increase_v(20)
    my_phone.charge(40)
    my_phone.lock()


if __name__ =="__main__":
    main()
        