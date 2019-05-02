from datetime import datetime
class account:
    def __init__(self, first_name,last_name):
    
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan = 0

    def welcome(self):  
        return "dear, {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)

    def deposit(self,amount):
        time=datetime.now()
        object={"time":time,"amount":amount}
        self.deposits.append(object)
        deposit=amount
        self.balance=self.balance+amount
        return "dear, {} {} your account balance is {}".format(self.first_name,self.last_name,amount)
    def withdraw(self,y):
        withdraw=y
        time=datetime.now()
        object={"time":time,"amount":y}
        if y > self.balance:
            self.withdrawals.append(y)
            return "not successful"
        else:
            self.balance=self.balance-y
            return "dear, {} {} you have withdrawn KES {} and your account balance is {}".format(self.first_name,self.last_name,y,self.balance)

    def showbalance(self):
        showbalance=self.balance
        return "dear, {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)
    def  show_deposits(self):
            for h in self.deposits:
                time=h["time"]
                friendly_time=time.strftime("%c")
                amount=h["amount"]
                print("on {} you deposited{}".format(friendly_time,amount))

    def show_withdrawals(self):
            for y in self.withdrawals:
                 time=y["time"]
                 friendly_time=time.strftime("%c")
                 amount=y["amount"]
                 print("on {} you withdrew{}".format(friendly_time,amount))
                       
    
    def give_loan(self,x):
        loan=x
        total=0
        total+=x
        for amount in self.deposit
        amount=amount["amount"]


        if len (self.deposits)>=5 and x<total 1/3* and self.loan==0:
            self.loan=self.loan + amount
            print("hello {} you are qualify for the loan of {}".format(self.name,amount))
        else:
            print("hello {} you dont qualify for the loan".format(self.name))


    def pay_loan(self,amount):
        if self.loan==0:
          print("you dont have an existing loan")
        elif amount <self.loan:
          print("hello {} you have paid some amount of your loan{},your balance remaining is{}".format(self.name, amount,self.loan))


        elif amount==self.loan:
          self.loan=self.loan-amount
          print("you have paid your loan")
         


                
    
