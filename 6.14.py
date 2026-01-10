bottle_data=[508,500,512,499,492,511,503,476,501,509]
capacity=500
tolerance=2

bottle_correct=list(filter(lambda x: capacity*(1-tolerance/100)<x<capacity*(1+tolerance/100),bottle_data))
bottle_incorrecltly=1-len(bottle_correct)/len(bottle_data)

print(f'Bottle capacity:{capacity}ml')
print(f'Filling tolerance:{tolerance}%')
print(f'Filled bottles: {bottle_data}')
print(f'Incorrectly filled: {round(bottle_incorrecltly*100)}%')