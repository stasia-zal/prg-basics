
def f(array2D):
    people=0
    for stop in array2D:
        people+=stop[0]-stop[1]
    return people


if __name__=='__main__':
    print(f([[3,0]]))
    print(f([[3,0],[6,1]]))