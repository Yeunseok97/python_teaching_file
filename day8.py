"""

예외처리
매직함수, 데코레이터, 제너레이터, 일급함수,
파일 입출력
"""

# print("programming start -")
# print("* 50")
# age = int(input("나이를 숫자로 입력해주세요:"))
# print(" your age is ", age , "years old")
# print("* 50")
# print("programming end - ")


"""
예외처리
try:
    예외가 발생 할 가능성이 있는 코드를 정의하는 곳
    A
    B
except A:
    발생한 예외를 잡기위한 객체를 정의하고 처리하는 곳
except B:
    발생한 예외를 잡기위한 객체를 정의하고 처리하는 곳
else:
    예외가 발생되지 않을 때 실행되는 곳  
finally:
    예외발생 여부와 상관없이 실행되는 곳
"""
# function define - worker
# def smpInput():
#     try:
#         age = int(input("나이 숫자로입력:"))
#     except ValueError as e: #(exception으로 쓰면 모든 에러타입가능)
#         print(str(e))
#         smpInput()
#     else:
#         print("your age is'", age, "years old")
#     finally:
#         print("**예외발생여부와 상관없이 무조건 수행")


# #caller
# smpInput()
# print("programming end -")
"""
"""

# def exceptionFunc(lst):
#     try:
#         for e in lst:
#             print("raw -",e)
#             sqrt = e**2
#             print("squared -", sqrt)
#     except TypeError as i:
#         pass
#     finally:
#         print("function end --")


def exceptionFunc(lst):
    for e in lst:
        try:
            print("raw -",e)
            sqrt = e**2
            print("squared -", sqrt)
        except TypeError as i:
            pass

# #caller
# usrlst = [10, 20, 25, "num", 40, 50]
# exceptionFunc(usrlst)

#사용자 정의 예외클래스를 만들 수 있다.



# class UserNegativeDivisionError(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#
# def positiveDivide(x, y):
#     if(y<0):
#         raise UserNegativeDivisionError("음수로 나눌 수 없습니다.")
#     else:
#         return x/y
#
# try:
#     result = positiveDivide(10, -2)
#     print("call positive func - ", result)
# except UserNegativeDivisionError as e:
#     print(e.msg)
# except ZeroDivisionError as e:
#     print(e.args[0])
# print("programming end- ")


#magic function
#__xxxx__()


# class MagicClass(object):
#     def __init__(self):
#         print("객체 생성시 호출")
#     def __del__(self):
#         print("객체 삭제시 호출")
#     def __str__(self):
#         return "이제는 주소값이 아니라 문자열이 출력"
# obj = MagicClass()
# print(obj)


#일급함수, first class
# 변수에 함수를 저장할 수 있다.
# 함수를 다른 함수의 인자로 전달할 수 있다.

def userAdd(x, y):
    return x + y
print("add -", userAdd(10, 20))
print("function address -", userAdd)
f = userAdd
print("f -add -",f(10,20))

def userMinus(x,y):
    return x - y

#함수를 다른 함수의 인자로 전달

def userOperation(func, arg):
    return func(arg[0], arg[1])


data = (10, 22)
result = userOperation(userAdd, data)
print("add -", result)

#함수의 리턴값으로 다른 함수를 사용할 수 있다.
#closure
def outer(x):
    tmp = x
    def inner(y):
        return tmp + y

    return inner

#caller
result = outer(5)
print("result - ", result(10))

# generator (반복문)
# -장점 : 빠른 수행속도, 적은 메모리 사용으로 인한 성능 향상

def loopFunc(lst):
    result = []
    for tmp in lst:
        result.append(tmp**2)
    return result

#caller
data = [1,2,3,4,5]
result = loopFunc(data)
print("result -", result)


def generatorFunc(lst):
    for tmp in lst:
        yield tmp **2
result = generatorFunc(data)
print("generator type",type(result))
# print("next - ", next(result))
# print("next - ", next(result))
# print("next - ", next(result))
# print("next - ", next(result))
# print("next - ", next(result))
for i in result:
    print(i)

lst = [tmp**2 for tmp in data]
print("list comprehension-", lst)
generator = (tmp**2 for tmp in data)
print("type-", generator)

for i in generator:
    print(i)
print("end for~")
print("generator -", list(generator))
print()


#파일 입출력
#순수 파이썬기반 입출력, pandas 기반 입출력
"""
텍스트파일
-open(file = xxxx, mode = r|w|a")
-with open() ~ as file :

"""
def readTxt(path, mode):
    try:
        file = open(path, mode, encoding= "utf-8")
        print("file type -", type(file), file)
        print("read -", file.read())
    except Exception as e:
        print(str(e))
    else:
        print("read -\n", file.read())
    finally:
        if file != None :
            file.close()

#caller
readTxt("../data/greeting.txt", "r")

#출력
def writeTxt(path, mode):
    file = open(path, mode, encoding = "utf-8")
    file.write("\nhello~, oys")
    file.close()

writeTxt("../data/test.txt","a")





def with_open_file(path, mode, e):
    with open(path, mode, encoding = e) as file:
        # print(file.readlines()), type(file.read())
        # print("readlines type-",type(file.readlines()))
        # print("readline type -", type(file.readline()))
        # for line in file:
        #     print(line.strip("\n"))
        #readline()
        line = None
        while line != "":
            line = file.readLine()
            print(line.strip("\n"))
        #readlines()
        lst = file.readlines()
        for s in lst:
            print(s.strip("\n"))

# caller
with_open_file("../data/greeting.txt", "r", "utf-8")

# line = None
# print("None casting -", bool(line))