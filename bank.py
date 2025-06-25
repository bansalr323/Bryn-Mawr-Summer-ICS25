'''
1) We can create new accounts 
2) We can close accounts 
3) Withdraw money 
4) Deposit money 
5) Transfer money 
'''
def createAccount(name, balance, accts): 
    accts[name] = balance #This is how we added things to dictionaries. 

def closeAccount(name, accts): 
    if name in accts.keys():  
        accts.pop(name) #This is how we removed things from dictionaries.
    else: 
        print("That is not a valid account name.")

def withdraw(name, amount, accts): #Not only performing its functionality, but also returning a boolean value for a (un)sucessful operation. 
    if name in accts.keys(): 
        if amount > accts[name]: 
            print("Amount exceeds account balance") 
            print("Accounts not updated") 
            return False
        else: 
            accts[name] = accts[name] - amount 
            return True
    else: 
        print("That is not a valid account name.") 
        return False
    

def deposit(name, amount, accts):
    if name in accts.keys(): 
        accts[name] = accts[name] + amount
    else: 
        print("That is not a valid account name.")  

def transfer(acct1, acct2, amount, accts): 
    if acct1 in accts.keys() and acct2 in accts.keys(): 
        if withdraw(acct1, amount, accts) == True: 
            deposit(acct2, amount, accts)
    else: 
        print("One of those accounts is not valid.")
        print("Account not updated")

def printAccounts(accts):
    print(" ")
    print("------Accounts------")
    for name in accts: 
        print(f"Account name: {name}     Balance: {accts[name]}")

def main(): 
    accounts = {"John Pork": 500} 
    check = True 
    while check == True: 
        print(" ") 
        print("Wecome to the Bank!")
        print("1. Create Account")
        print("2. Close Account") 
        print("3. Withdraw") 
        print("4. Deposit") 
        print("5. Transfer") 
        print("6. Quit") 
        option = (input("Enter your option from the list above: "))
        if option.isnumeric() == True: 
            if int(option) == 1: 
                printAccounts(accounts) 
                print(" ")
                acctname = input("Enter the name of your account: ").strip()
                balance = float(input("Enter your balance: "))
                createAccount(acctname, balance, accounts)
                printAccounts(accounts) 

            elif int(option) == 2: 
                printAccounts(accounts)
                print(" ")
                acctname = input("Enter the name of the account you wish to close: ").strip()
                closeAccount(acctname, accounts)
                printAccounts(accounts) 

            elif int(option) == 3: 
                printAccounts(accounts) 
                print(" ")
                acctname = input("Enter the account name you wish to withdraw from: ").strip()
                amt = float(input("Enter the amount you wish to withdraw: "))
                withdraw(acctname, amt, accounts)
                printAccounts(accounts) 

            elif int(option) == 4: 
                printAccounts(accounts) 
                print(" ")
                acctname = input("Enter the account name you wish to deposit to: ").strip()
                amt = float(input("Enter the amount you wish to deposit: "))
                deposit(acctname, amt, accounts)
                printAccounts(accounts) 

            elif int(option) == 5: 
                printAccounts(accounts) 
                print(" ")
                acct1 = input("Enter the account name you wish to transfer from: ").strip()
                acct2 = input("Enter the account name you wish to transfer to: ").strip()
                amt = float(input("Enter the amount you would like to transfer: ")) 
                transfer(acct1, acct2, amt, accounts)
                printAccounts(accounts)  
                
            elif int(option) == 6:
                printAccounts(accounts) 
                print(" ")
                print("Thank you for using our bank!")  
                check = False 

        else: 
            print("This is not a valid option. Please try again.") 
main() 