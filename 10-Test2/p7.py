import re
def f(array):
    count=0
    key=r'[a-z\d_]{4,12}'
    for item in array:
        if re.fullmatch(key,item):
            count+=1
    return count

print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
