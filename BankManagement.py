import time 
class user :
    def __init__(self,name,age,mobile_no,gender) :
        self.name = name
        self.age = age
        self.mobile = mobile_no
        self.gen = gender
    def PrInt(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Mobile Number : ",self.mobile)
        print("Gender : ",self.gen)
class bankdetails(user):
    def __init__(self, name, age, mobile_no, gender):
        super().__init__(name, age, mobile_no, gender)
        self.balance = 0
    def deposit(self,amo):
        self.amount = amo
        self.balance = self.balance + self.amount
        print(time.ctime(),":" ,amo,"has been deposited to your Bank Account")
        print("Your Available Balance is : ",self.balance)
    def withdraw(self,amo):
        self.amount = amo
        if self.balance < self.amount :
            print(time.ctime(),":" ,"Insuficient Balnce : Sorry")
            print("Available Balance :Rs",self.balance)
        else :
            self.balance = self.balance - self.amount
            print(time.ctime() ,":" ,amo,"has been debited to your Bank Account")
            print("Your Available Balance is : ",self.balance)
    def details(self):
        self.PrInt()
        print("Account Balance : Rs",self.balance)
usr = bankdetails("Shubham",20,"7389162810","M")
usr.deposit(100)
usr.deposit(50)
usr.withdraw(110)
usr.details()