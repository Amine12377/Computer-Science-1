#Lists containing all data
income_data = []
expense_data = []

def add_income ():
    #asking user to add desciprion and amount
    description = input("Enter the description of your data: ")
    amount = float(input("Enter the amount of the income: "))
    income_data.append({"description" : description,
                        "amount" : amount}) #Adding the information
    print("Information registered") #message confirmation

def add_expense ():
    #asking user to add description, amount and category
    description = input("Enter the description of your data: ")
    amount = float(input("Enter the amount of the expenses: "))
    category = input("Enter the category: ")
    expense_data.append({"description": description,
                         "amount": amount,
                         "category": category}) #adding the information
    print("Information registered") #message confirmation

def view_summary ():
    #summing all incomes
    total = 0
    for i in income_data:
        total += i["amount"]
    #summing all expenses
    total1 = 0
    for i in expense_data:
        total1 += i["amount"]
    #calculating balance:
    balance = total - total1
    print(f'Your total income is {total}\nYour total expenses are {total1}\nYour balance is {balance}')

def delete_entry ():
    choice = input("Do you want to delete an income or an expense?") #asking user if he wants to delete income or expense
    if choice == "income":
        choice1 = input("Enter the description: ")
        for i in income_data:
            if i["description"] == choice1:
                income_data.remove(i)
                print("information removed")

    if choice == "expense":
        choice2 = input("Enter the description: ")
        for i in expense_data:
            if i["description"] == choice2:
                income_data.remove(i)
                print("information removed")

def modify_entry():
    choice = input("Do you want to modify an income or an expense?") #asking user if he wants to delete income or expense
    if choice == "income":
        choice1 = input("Enter the description: ")
        for i in income_data:
            if i["description"] == choice1:
                i["description"] = input("Enter the new description: ")
                i["amount"] = input("Enter the new amount: ")
                print("information modified")
            else:
                print("not found")

    if choice == "expense":
        choice2 = input("Enter the description: ")
        for i in expense_data:
            if i["description"] == choice2:
                i["description"] = input("Enter the new description: ")
                i["amount"] = input("Enter the new amount: ")
                i["category"] = input("Enter the new category: ")
                print("information modified")
            else:
                print("not found")

def list_entries():
    if not income_data:
        print("You have no income entry")
    else:
        for i in income_data:
            print(i["description"], i["amount"])
    if not expense_data:
        print("You have no expenses")
    else:
        for i in expense_data:
            print(i["description"], i["amount"], i["category"])

def main ():
    option = 0
    while True:
        option = int(input("Enter your option:\n1: Add income\n2: Add expense\n3: View Budget summary\n4: Delete an entry\n5: Modify an entry\n6: List all Entries\n7: Exit\n"))
        if option == 1:
            add_income()
        elif option ==2:
            add_expense()
        elif option ==3:
            view_summary()
        elif option ==4:
            delete_entry()
        elif option ==5:
            modify_entry()
        elif option == 6:
            list_entries()
        elif option ==7:
            break
        else:
            print("wrong number")


main()