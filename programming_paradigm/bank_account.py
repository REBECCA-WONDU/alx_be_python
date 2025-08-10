class BankAccount:
    """A simple bank account class that handles deposits, withdrawals, and balance checks."""
    
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance.
        
        Args:
            initial_balance (float): The starting balance (default 0)
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): The amount to deposit
        """
        self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.
        
        Args:
            amount (float): The amount to withdraw
            
        Returns:
            bool: True if withdrawal succeeded, False if insufficient funds
        """
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True
    
    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")