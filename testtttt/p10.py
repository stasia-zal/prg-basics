import re

def f(dates):
    pattern=r'[0-9]{2}/[0-9]{2}/[0-9]{4}'
    return re.findall(pattern,dates)




if __name__=='__main__':
    dates='2021-1-3;05/12/2024:1998-12-11,9 maj 2007;;31/03/2021,,1/9/2011'
    print(f(dates))