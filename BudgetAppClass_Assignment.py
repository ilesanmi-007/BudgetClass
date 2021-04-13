# class Transfer():
#     def __init__(self, From_category, To_category):
#         self.From_category = From_category
#         self.To_category = To_category
#
#     def Transfer(self):
#         new = Budget()
#         new.balance()
#         pass

class Budget:
    #balance = [0, 0, 0]
    def __init__(self, categories):
        self.categories = categories
        self.amount = 0

    def deposit(self, amount):
        self.amount = self.amount + amount
        return self.amount

    def Withrawal(self, withdraw):
        self.amount = self.amount - withdraw
        pass

    def balance(self):
        print('your balance for {} is {}'.format(self.categories, self.amount))

    def transfer(self, cash, y):
        '''transfer ammount to'''
        self.cash = cash
        self.amount = self.amount - cash
        zz = y.deposit(cash)
        return zz

somborri_1 = Budget('food')
somborri_2 = Budget('clothing')

print('depositing 500 to obj 1...food')
somborri_1.deposit(500)
somborri_1.balance()
print('withdrawing 200 from obj 1...food')
somborri_1.Withrawal(200)
somborri_1.balance()

print('---' * 20)
print('\n\n\n\n')
print('depositing 300 to obj 2...clothing')
somborri_2.deposit(300)
somborri_2.balance()

somborri_1.transfer(100, somborri_2)
print('hellooooo\n')
somborri_2.balance()
somborri_1.balance() #this worked
