"""[실습]
1. account class 작성
2. 인스턴스 변수 - type(S|F),account, balance, interestRate
2-1 SavingAccount(Account), FundAccount(Account)
3. accountInfo()- 계좌정보를 출력하는 함수
4. deposit(amount) - 매개변수로들어온 amount를 balance에 입금
5. withDraw(amount) - 매개변수로들어온 amount를 balance에 출금
5-1) 단 잔고가 부족할 경우 출금안하고 "잔액이 부족합니다" 출력
6. abstract printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 2자리 까지 출력
--printInterestRate()오버라이딩
savingaccount = 기본 이자율에 만기시 이자율 0.1
fundaccount = 기본 이자율에 잔액이 10만원이상이면 10%, 기본 이자율에 잔액이 50만원이상이면 15%, 기본 이자율에 잔액이 100만원이상이면 20%

"""


class Account:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def accountInfo(self):
        print("계좌 {}, 잔액 {}".format(self.account, self.balance))

    def deposit(self, amount):
        self.balance += amount
    def withDraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("잔고부족")

class Saving_Account(Account):
    def __init__(self, printInteresRate):
        self.interestRate = interestRate
        super().__init__(account, balance)




class Fund_Account(Account):
    def __init__(self, printInteresRate):
        self.interestRate = interestRate
        super().__init__(account, balance)







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