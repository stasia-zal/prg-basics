nums=[]
for i in range (1,21):
    nums.append(i)
print(*list(filter(lambda x:x%2==0 or x%3==0,nums)))