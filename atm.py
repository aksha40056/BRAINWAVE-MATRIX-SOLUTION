class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.pin = "1234"

    def authenticate(self, pin):
        if pin == self.pin:
            return True
        else:
            return False

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful. New balance: {self.balance}"

def main():
    atm = ATM(balance=80000)

    print("Welcome to the ATM")
    pin = input("Enter your PIN: ")

    if atm.authenticate(pin):
        while True:
            print("\nMenu:")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(f"Your balance is: {atm.check_balance()}")
            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                print(atm.withdraw(amount))
            elif choice == "3":
                amount = float(input("Enter the amount to deposit: "))
                print(atm.deposit(amount))
            elif choice == "4":
                print("Thank you for using the ATM")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid PIN. Please try again.")

if __name__ == "__main__":
    main()