gr=[3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
pos=list(filter(lambda x:x>2.0,gr))
print(round(sum(pos)/len(pos),2))