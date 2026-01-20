def f(x,y,d):
    for nums in range(x,y+1):
        if str(d) in str(nums):
            return True
    return False


print(f(10,15,"14"))
print(f(100,120,"11"))
print(f(205,210,"04"))