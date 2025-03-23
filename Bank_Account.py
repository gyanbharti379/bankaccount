import random
def generate_account_number():
            return random.randint(1000000000,9999999999)

class BankAccount:
    customer_lst = []
    s1="*"*70
    cu_acc_num = 0
    
    def __init__(self):
          
          self.account_holder_name = None
          self.balance = 0
          self.account_number = 0

    def create_account(self,account_holder,initial_balance):
        self.account_holder_name = account_holder
        self.balance = initial_balance
        self.account_number = generate_account_number()
        self.customer_lst.append(self)
        print("your account number is: ",self.account_number)
        print("account holder name is: ",self.account_holder_name)
        print("account balance is: \u20B9",self.balance)    

    def all_customers():
        print(f"{BankAccount.s1}\nAll customers are:\n{BankAccount.s1}")
        for index,customer in enumerate(BankAccount.customer_lst):
            print(f"{index+1}. account holder name is: {customer.account_holder_name} and account number is: {customer.account_number}")
        print(BankAccount.s1)

    def find_customer():
        print(f"{BankAccount.s1}\nFind Customer\n{BankAccount.cu_acc_num}\n{BankAccount.s1}")
        if BankAccount.cu_acc_num == 0:
            account_number = int(input("Enter your account number: "))
            for customer in BankAccount.customer_lst:
                        if customer.account_number == account_number:
                                    BankAccount.cu_acc_num = customer.account_number
                                    return customer
            return None 
        else:
            for customer in BankAccount.customer_lst:
                        if customer.account_number == BankAccount.cu_acc_num:
                                    BankAccount.cu_acc_num = customer.account_number
                                    return customer
            return None
        
    def check_balance(self):
        print(f"{BankAccount.s1}\nCheck Balance\n{BankAccount.s1}")
        print(f"your account holder name is: {self.account_holder_name} and balance is: \u20B9{self.balance}")    
      
    def deposit(self,amount):
        self.balance += amount
        print(f"{BankAccount.s1}\nAmount Deposit\n{BankAccount.s1}")
        print(f"amount deposit is: \u20B9{amount} and new balance is: \u20B9{self.balance}")
         
    
    def withdrawal(self,amount):
        if self.balance < amount:
            print("insufficient balance to withdraw")
            return
        self.balance -= amount
        print(f"{BankAccount.s1}\nAmount Withdraw\n{BankAccount.s1}")
        print(f"amount withdraw is: \u20B9{amount} and new balance is: \u20B9{self.balance}")
       
    
    def fund_transfer(self,amount,customer2):
        print(f"{BankAccount.s1}\nAmount Transfer\n{BankAccount.s1}") 
        if self.balance >= amount:
            self.balance -= amount
            customer2.balance += amount
            print(f"amount transfer is \u20B9{amount} to account number is {customer2.account_number}")
            print(f"and your new balance is yours: \u20B9{self.balance}")
            print(f"and {customer2.account_holder_name}'s new balance is: \u20B9{customer2.balance}")
        else:
            print("insufficient balance to transfer")   
        
         
while True:
    print(f"{BankAccount.s1}\nWelcome to the bank!\n{BankAccount.s1}")
    print("1. Create Account\n2. Check Balance\n3. Deposit\n4. Withdrawal\n5. Fund Transfer\n6. Exit")
   
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter your name: ")
        balance = float(input("Enter your initial balance: "))
        ba = BankAccount()
        ba.create_account(name,balance)
        BankAccount.cu_acc_num = ba.account_number
       
    elif choice == 2:
        customer = BankAccount.find_customer()
        if customer is not None:
                    customer.check_balance()
        else:
            print("Account number is invalid")           
        
    elif choice == 3:
         customer = BankAccount.find_customer()
         if customer is not None:
                amount = float(input("Enter the amount to deposit: "))
                customer.deposit(amount)
         else:
            print("Account number is invalid")          
    elif choice == 4:
         customer = BankAccount.find_customer()
         if customer is not None:
                amount = float(input("Enter the amount to withdraw: "))
                customer.withdrawal(amount)
         else:
            print("Account number is invalid")          
    elif choice == 5:
        customer = BankAccount.find_customer()
        if customer is not None:
                amount = float(input("Enter the amount to transfer: "))
                account_number = int(input("Enter the account number to transfer: "))
                for customer2 in BankAccount.customer_lst:
                        if customer2.account_number == account_number:
                                     customer.fund_transfer(amount,customer2)
                                   
        else:
            print("Account number is invalid")           
    elif choice == 6:
        print("Thank you for using the bank!")
        break
    
# a1 = BankAccount("Gyan Bharti",20000)
# a2 = BankAccount("Mohan",20000)
# a1.deposit(10000)
# a2.withdrawal(5000)
# a1.fund_transfer(5000,a2.account_number)
# a1.check_balance()
# a2.check_balance()
# BankAccount.all_customers()



        
        