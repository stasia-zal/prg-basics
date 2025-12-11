class TV:
    def __init__(self):
        self.is_on=False
        self.channel_no=1
        self.channels=[]
        self.volume=0
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
    def channel(self,new_channel_no):
        self.channel_no=new_channel_no
    def set_channels(self,channels_list):
        self.channels = [ch.strip() for ch in channels_list.split(',')]
    def show_channels(self):
        print('Channel list:')
        count=1
        for item in self.channels:
            print(str(count)+'.',item)
            count+=1
        print()
    def show_status(self):
        print(f'Tv is on: {self.is_on}')
        if self.is_on:
            if self.channels:
                print(f'Current channel {self.channel_no} ({self.channels[self.channel_no-1]})')
