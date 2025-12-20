# tv_show.py file
# main program
from tv import TV

def main():
    # object creation and usage
    tv=TV()
    tv.show_status()
    tv.turn_on()
    tv.show_status()
    tv.show_channels()
    tv.set_channels('TVP1, TVP2, Polsat,Новий канал, TVN, Filmbox, Discovery, 1+1, СТБ,ПлюсПлюс, ТЕТ')
    tv.show_channels()
    tv.channel(8)
    tv.show_status()
    tv.channel(4)
    tv.show_status()
    tv.turn_off()
    tv.show_status()
    tv.increase_volume()
    tv.increase_volume()
    tv.show_status()
    tv.decrease_volume()
    tv.show_status()


if __name__ == "__main__":
    main() 