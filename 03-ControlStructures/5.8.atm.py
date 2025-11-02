###
# ATM (cash machine) simulator
#
import time
a=1 
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    time.sleep(3)
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()



    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice =='4':
        print(f"Your PIN is: {pin}")
    elif choice=='5':
        newpin=input('Enter your new PIN:')
        newpindigit=newpin.isdigit()
        newpinlen=len(newpin)
        if newpindigit:
            if newpinlen !=4:
                print('Your pin must be 4 digits long. please try again')
            else:
                pin=newpin
                print(f'Your pin now is {pin}')
        else:
            print("Your Pin has to consist only of digits. Please try again.")
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
