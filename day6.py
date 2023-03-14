"""
oop(객체지향 프로그래밍)
- class(변수 + 함수) - 객체(instance) 생성할 수 있다.

-- 클래스에 정의된 (변수와 함수)구성요소는 클래스의 소유가 아닌
-- 인스턴스의 소유로 봐야한다.

-- initialize(초기화 함수, 생성자)
-- magic function
- object vs instance
- object - 명사적(변수), 동사적(함수)
- 함수 < 클래스 < 모듈(클래스(변수 + 함수)) < 패키지
- self <- 인스턴스를 대표하는 키워드
"""

# 강사의 정보를 저장하려고 한다.
# 여러명의 강사의 정보를 저장한다면?
# [{}, {}, {}]

tea_name = "ljs"
tea_subject = "python"
tea_mail = "jslim9413@naver.com"

def printTea():
    print(tea_name, tea_subject, tea_mail)


class Teacher:
    # 변수 + 함수
    cls_var = 3.5

    def doing(self):
        print("인스턴스 소유의 함수입니다.")

printTea()
# doing 함수를 호출하기 위해서는
#1. 클래스로부터 인스턴스 생성이 필요
#2. instance.함수()
tea = Teacher() # 인스턴스를 생성하는 코드임

print("instance address -", tea)
print("instance function - ", end = "")
tea.doing()
print("instance variable - ", tea.cls_var)


class Person:
    # 인스턴스 소유가 아닌 클래스 소유의 변수로 본다.
    # 모든 인스턴스가 공유하는 변수

    cls_var = 3.5
    # initializer(magic function)
    # 객체 생성시 자동으로 호출되는 함수
    # 명시적으로 호출이 불가
    def __init__(self, name, subject, email):
        self.name    = name
        self.subject = subject
        self.email   = email

    def perInfo(self):
        return "이름 {}, 과목 {}, 메일{}".format(self.name, self.subject, self.email)

    def isScholarShip(self, grade):
        #클래스 소유의 변수는 클래스.변수로 해야함.
        if grade >= Person.cls_var:
            return True
        else:
            return False

per01 = Person("oys", "python", "oyskaka")
Person.cls_var = 4.5
per02 = Person("oys1", "python", "oyskaka")
per03 = Person("oys2", "python", "oyskaka")
per04 = Person("oys3", "python", "oyskaka")

lst = list()
lst.append(per01)
lst.append(per02)
lst.append(per03)
lst.append(per04)

print("정보출력")
for instance in lst:
    print(instance.name)
    print(instance.subject)
    print(instance.email)
    print(instance.cls_var)
    # print(instance.perInfo())
    print(instance.isScholarShip(4.5))
    print(Person.cls_var)
print()


class Employee:
    raise_rate = 1.5
    def __init__(self, userName, userSalary):
        print("초기화 함수 자동 호출")
        self.userName = userName
        self.userSalary = userSalary

    def getSalary(self):
        return "{}님의 급여는{}입니다.".format(self.userName,self.userSalary)

    def increaseSalary(self):
        self.userSalary = self.userSalary * Employee.raise_rate


empObj01 = Employee("oys",100)
empObj02 = Employee("oys1",200)
empObj03 = Employee("oys2",300)

print(empObj01.getSalary())
print(empObj02.getSalary())
print(empObj03.getSalary())

print("급여인상")
empObj01.increaseSalary()
empObj02.increaseSalary()
empObj03.increaseSalary()
print(empObj01.getSalary())
print(empObj02.getSalary())
print(empObj03.getSalary())

#인상률 직접변경
print("급여 인상률 변경 -")
empObj01.increaseSalary()
empObj02.increaseSalary()
empObj03.increaseSalary()
print(empObj01.getSalary())
print(empObj02.getSalary())
print(empObj03.getSalary())

# oop (은닉화, 상속, 다형성, 추상화)


"""

"""