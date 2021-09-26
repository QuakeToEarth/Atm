class Atm():
    def __init__(self, balance, pin, name):
        self.balance = balance
        self.pin = pin
        self.name = name

    def withdraw(self):
        a = int(input('Enter the amount you want to withdraw : '))
        if (a> self.balance):
            print("We arn't rich, sorry we can't fufill your money needs :(")
        else:
            self.balance = self.balance - a
            print("The remaining balence you have in your account is : " + str (self.balance))
    def deposit(self):
        depo = int(input("How much money do you want to deposit :"))
        self.balance = self.balance + depo
        print("The new balance is " + str (self.balance))
    def check(self):
        print('The cureent amount you own is :'+ str (self.balance))



customer1 = Atm(2910, 2007, 'Mayre')
customer1.check()
customer1.withdraw()
customer1.deposit()