def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return n*0.39

def feet_inch_to_cm(f,i):
    i=i+f*12
    return i*2.54


if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'356cm={cm_to_inch(356)}inch')
    print(f'5 feet 56in={feet_inch_to_cm(5,56)}cm')

