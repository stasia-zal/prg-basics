def f(binary_number):
    a=True
    for i in str(binary_number):
        if not i=='0' and not i=='1':
            a= False
    return a