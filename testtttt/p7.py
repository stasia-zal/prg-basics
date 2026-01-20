def f(files):
    count_of_letters=0
    for item in files[0]:
        if item .isdigit():
            break
        else: count_of_letters+=1
    return sorted(files,key=lambda x:int(x[count_of_letters:]))




if __name__=='__main__':
    files = ["copy179", "copy15", "copy3", "copy123", "copy9"]
    print(f(files))
    files2 = ["img11", "img2", "img10"]
    print(f(files2))   #, ["img2", "img10", "img11"]
    files3 = ["x10", "x2", "x5"]
    print(f(files3))       #, ["x2", "x5", "x10"]