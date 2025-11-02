hage=int(input("Enter the dog's age in human years: "))
if hage<=2:
    dage=hage*10.5
else:
    dage=2*10.5+4*(hage-2)
print(f"The dog's age in dog's years is {dage} years.")