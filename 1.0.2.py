class BankAccountсо:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, plus_balance):
        self.balance += plus_balance
        return f'Кладем деньги: {self.balance}' '\n'

    def withdraw(self, minus_balance):
        self.balance -= minus_balance
        return f'Забираем деньги: {minus_balance}'

    def get_balance(self):
        return f'Текущий баланс: {self.balance}'


banker = BankAccountсо('Vanek', 0)

print(banker.deposit(100), banker.withdraw(45))
print(banker.get_balance())
