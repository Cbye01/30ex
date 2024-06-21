
import logging
class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            logging.basicConfig(filename='transactions.log', level=logging.INFO, format='%(asctime)s - %(message)s')
        return cls._instance

    def log(self, message):
        logging.info(message)

class BankAccount:
    def __init__(self, accountNumber, balance=0):
        self.accountNumber = accountNumber
        self.balance = balance
        self.logger = Logger()  

    def deposit(self, amount):
        self.balance += amount
        self.logger.log(f'Deposit: +{amount}. New balance: {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.logger.log(f'Withdrawal: -{amount}. New balance: {self.balance}')
account1 = BankAccount('12345', 1000)
account1.deposit(500)
account1.withdraw(200)
try:
    account1.withdraw(1500)  
except ValueError as e:
    print(f"Failed to withdraw: {e}")


