class ATMMachine:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"${amount} deposited successfully. New balance is: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully. New balance is: ${self.balance}")

    def start(self):
        while True:
            print("\nWelcome to the ATM Machine")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Please choose an option (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: $"))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: $"))
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    # Initialize ATM with an initial balance of $1000
    atm = ATMMachine(initial_balance=1000)
    atm.start()
