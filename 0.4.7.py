accounts = []


def create_account(name, balance):
    accounts.append([name, balance])
    return f'Аккаунт с именем {name} создан с балансом {balance}'


def transaction(accounts):
    trans = input()
    for account in accounts:
        if 'снять' in trans:
            print('Введите сумму для вывода')
            summa = int(input())
            account[1] = int(account[1]) - summa
        elif 'положить' in trans:
            print('Введите сумму для вывода')
            summa = int(input())
            account[1] = int(account[1]) + summa
        else:
            print('Нет такой функции')
            continue


def check_balance(account):
    for account in accounts:
        if account[0] == account:
            print(f'Текущий баланс счета {account_name}: {account[1]}.')
            return
    print('Счет не найден')


print(create_account('Vlad', '5000'))
print(transaction(accounts))
print(check_balance(account))