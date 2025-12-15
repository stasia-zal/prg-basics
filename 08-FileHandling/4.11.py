with open('integ_power.txt','w',encoding='utf-8') as file:
    for i in range(1,101):
        file.write(f'{i},{i*i},{i*i*i}\n')
print(f'All details have been written to integ_power.txt')