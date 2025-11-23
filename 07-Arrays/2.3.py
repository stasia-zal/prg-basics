# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95]    # Week 4
]

total_food=0
# Calculates expenses
# Use loop statements
def total_exp(list,i):
    total=0
    a=0
    for column in range(len(list[0])):
        total+=list[a][i]
        a+=1
    return total

def total_week(list,week):
    total=0
    a=0
    for column in range(len(list[0])):
        total+=list[week][a]
        a+=1
    return total

...

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', total_exp(monthly_expenses,0))
print('Transport:',total_exp(monthly_expenses,1))
print('Utilities:',total_exp(monthly_expenses,2))
print('Week 1:',total_week(monthly_expenses,0))
print('Week 2:',total_week(monthly_expenses,1))
print('Week 3:',total_week(monthly_expenses,2))
print('Week 4:',total_week(monthly_expenses,3))
print('---------------')
print('TOTAL:',total_week(monthly_expenses,0)+total_week(monthly_expenses,1)+total_week(monthly_expenses,2)+total_week(monthly_expenses,3))