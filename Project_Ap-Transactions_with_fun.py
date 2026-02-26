balance = 0
transactions = []
password = "@omi"

def check_password():
    attempts = 3
    while attempts > 0:
        passw = input("Enter your password to access the transaction system: ")
        if passw == password:
            print("Access granted.")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect password. {attempts} attempt(s) remaining.")
            else:
                print("Access denied. Exiting the system.")
                return False

def deposit():
    global balance
    amount = float(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        transactions.append(f"Deposited: Rs.{amount:.2f}")
        print(f"Rs.{amount:.2f} deposited successfully.")
    else:
        print("Invalid amount. Please enter a positive number.")

def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: "))
    if 0 < amount <= balance:
        balance -= amount
        transactions.append(f"Withdrew: Rs.{amount:.2f}")
        print(f"Rs.{amount:.2f} withdrawn successfully.")
    else:
        print("Invalid amount or insufficient balance.")

def check_balance():
    print(f"Current balance: Rs.{balance:.2f}")

def view_transactions():
    if transactions:
        print("Transaction History:")
        for t in transactions:
            print(t)
    else:
        print("No transactions yet.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transactions")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            deposit()
        elif choice == '2':
            withdraw()
        elif choice == '3':
            check_balance()
        elif choice == '4':
            view_transactions()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice.")

if check_password():
    menu()
