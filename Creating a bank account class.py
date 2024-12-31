import os

os.system('cls')

class Deposit:
    def __init__(self, name, amount = 0):
        self.owner = name
        self.amount = amount

    def __str__(self):
        return f'Owner : {self.owner} | amount : {self.amount}'
    
    def __repr__(self):
        # return f'Deposit(name={self.owner} , amount={self.amount})'
        return f'{self.__class__.__name__}(name={self.owner} , amount={self.amount})'

    def __add__(self, other):
        name = f'{self.owner}+{other.owner}' 
        amount = self.amount + other.amount
        return Deposit(name, amount)
    
    def __iadd__(self, other):
        self.amount += other.amount
        other.amount = 0
        return self
    
    def __eq__(self, other):
        return self.amount == other.amount
    
    def transfer(self, other, amount):
        if self.amount < amount:
            print('Not enough money.')
            return
        
        self.amount -= amount
        other.amount += amount

    def deposit(self, amount):
        if amount <= 0:
            print('Deposit amount should be positive.')
            return
        
        self.amount += amount

    def withdraw(self, amount):
        if amount <= 0:
            print('Amount amount should be positive.')
            return
        
        if self.amount < amount:
            print('Not enough money.')
            return
        
        self.amount -= amount



samira_dep = Deposit('samira', 1000)
arezoo_dep = Deposit('Arezoo', 2500)
narges_dep = Deposit('Narges')
arezoo_dep.deposit(200)

# print(samira_dep)
# print(repr(arezoo_dep))
# print(samira_dep + arezoo_dep)
# samira_dep += arezoo_dep
print(samira_dep)
print(arezoo_dep)
print('*'*20)
# print(samira_dep == Deposit('', 1200))
samira_dep.transfer(arezoo_dep, 200)
print(samira_dep)
print(arezoo_dep)
print('*'*20)

arezoo_dep.transfer(narges_dep, 300)
print(samira_dep)
print(arezoo_dep)
print(narges_dep)
print('*'*20)

print(repr(narges_dep))
print('*'*20)

# print('\n'.join(dir(Deposit)))
