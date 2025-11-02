de=int(input('Enter decimal number: '))
be=de
q=1
bi=''
while de!=0:
    if de%2!=0:
        bi='1'+bi
        de=(de-1)/2
    else:
        bi='0'+bi
        de=de/2
print(f'{be}(10) = {bi}(2)')