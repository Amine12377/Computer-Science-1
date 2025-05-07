#Login system:
attempts = 0 #Number of attempts for password
Login = 0 #Seeing if login is true.
#checking if the information is true:
while attempts < 3:
    username = input("Write your username:") #asking for username
    password = input("Write your password: ") #asking for password
    if username != "Amine" and password != '123':
        print("Wrong information")
        attempts +=1 #adding attempts
    elif username == "Amine" and password == "123":
        print("Login succesfull")
        Login = True #Login is true
        break
if attempts == 3:
    print("too many attempts")
    Login = False #login unsuccesfull

menu = 0 #Choice of menu
balance = float(500) #current balance of user
while Login == True and menu != 4: #He can only access if this variable is true and if the user didnt pick to leave the menu
    print("welcome to the system")
    menu = int(input("choose the following options: \n 1: Check balance \n 2: Deposit money \n 3: Withdraw money \n 4: Exit the system \n")) #choice of menu
    if menu == 1: #Balance checking
        print(f'Your balance is: {balance}.')
    elif menu == 2: #depositing money
        add = float(input("Enter the amount you want to add"))
        if add < 0: # we want positive value
            print("incorrect value")
        else:
            balance += add
    elif menu == 3:
        withdraw = float(input("Enter the amount you want to withdraw: "))
        if withdraw < 0: # we want positive value
            print("incorrect value")
        elif balance < withdraw: #we need to have enough money
            print("insufficient funds")
        else:
            balance -= withdraw
    elif menu < 1 or menu > 4:
        print("wrong value")
    print("BYE BYE")







