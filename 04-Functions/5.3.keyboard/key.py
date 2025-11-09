###
# Functions to read any data type from the keyboard
#
def input_string(message):
    string=input(message)
    return str(string)

def input_integer(message):
    integ=input(message)
    return int(integ)

def input_real(message):
    real=input(message)
    return float(real)

def input_boolean(message):
    boollean=input(message)
    if boollean=='y':
        boollean=True
    elif boollean=='n':
        boollean=False
    return bool(boollean)

