x=float(input('x= '))
y=float(input('y= '))
if x>0:
    if y>0:
        q='first'
    else:
        q='fourth' 
elif y>0:
    q='second'
elif y<0:
    q='third'
else:
    q='start'
print(f'Point P({x},{y}) is in the {q} quadrant of the coordinate system')