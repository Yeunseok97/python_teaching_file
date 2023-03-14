"""[실습]
1. account class 작성
2. 인스턴스 변수 - account, balance, interestRate
3. accountInfo()- 계좌정보를 출력하는 함수
4. deposit(amount) - 매개변수로들어온 amount를 balance에 입금
5. withDraw(amount) - 매개변수로들어온 amount를 balance에 출금
5-1) 단 잔고가 부족할 경우 출금안하고 "잔액이 부족합니다" 출력
6. printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 2자리 까지 출력
"""

class Account:
    def __init__(self, account, balance, interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate

    def accountInfo(self):
        print("계좌 {}, 잔액 {}".format(self.account, self.balance))

    def deposit(self, amount):
        self.balance += amount
    def withDraw(self, amount):
        if self.balance >= amount:
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("잔고부족")

    def printInterestRate(self):
        self.balance = self.balance * (1+self.interestRate)
        print('%.2f' % self.balance)


#caller
account = Account("441-2919-1234", 500000, 0.073)
print("계좌정보 출력 -")
account.accountInfo()
account.withDraw(600000)
account.deposit(200000)
account.accountInfo()
account.withDraw(6000000)

print("현재 잔액의 이자를 포함한 금액 - ")
account.printInterestRate()




class Car:

    def __init__(self, name, door, cc, price):
        self.utype = self.__class__.__name__   #타입체크
        self.name= name
        self.door= door
        self.cc = cc
        self.price = price

    def carInfo(self):
        if self.cc >= 5000 :
            self.grade = "대형차"
        elif self.cc >= 3000:
            self.grade = "중형차"
        else:
            self.grade= "준소형차"
        self.display()

    def display(self):
        print("%s는 %d cc이고(%s) 문짝은 %d개 입니다." %(self.name, self.cc, self.grade, self.door))



#caller
myDreamCar = Car("마세라티", 4, 4000, 3.5)
print("utype -", myDreamCar.utype)
myDreamCar.carInfo()


# oop (object oriented programming)
# - 은닉화, 상속, 다형성
# 상속(inheritance), Object(최상위 클래스)
# 부모 - 자식 관계 (is a ~)
#구문형식 : class class_name(부모 클래스):
# A(A~Y), A+(Z)

class Unit(object): #최상위 클래스
    pass

class Marine(Unit):
    pass

class Medic(Unit):
    pass


# 은닉화(encapsulation) - information hidding
# 외부에서 접근하지 못하게 함.
# 직접적으로 변수에 접근할 수 있지만 함수를 통한 간접적인 접근은 허용
# setXXXX(), getXXXX()

class UserDate(object):
    def __init__(self):
        self.year = 2022
        self.month = 2
        self.day = 4

    def setYear(self, year):
        if year <= 0:
            self.__year = 2022
        else:
            self.__year = year

    def getYear(self):
        return self.__year

myDate = UserDate()
myDate.setYear()
print("year -", myDate.getYear())
print("month -", myDate.month)
print("day -", myDate.day)