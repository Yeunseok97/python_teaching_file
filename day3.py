'''
파이썬 딕셔너리
범용적으로 가장 많이 사용
[{key:value},{}]
선언 : {key : value}, dict()}
순서 X, key중복 허용하지않음.(수정, 삭제가능)
'''


tmpDict = {"name" : "oys",
           "phone" : "01011111111",
           "birth" : "970323"}
print("type -",type(tmpDict),tmpDict)

# in 연산자 key값 중복확인
print("name" in tmpDict)

tmpDict = {
    "메로나" : [300,20],
    "비비빅" : [400,20],
    "죠스바" : [100,50]
}
# 키의 밸류값을 꺼내는방법

print("메로나의 가격은{}".format(tmpDict["메로나"][0]))
print("비비빅의 개수는{}".format(tmpDict["비비빅"][1]))

#새로운 데이터 수정 (중복된 키가 들어오면 데이터의 수정이 발생)
tmpDict["메로나"] = [400,10]
print(tmpDict)

#메로나 가격인상
melon = tmpDict["메로나"]
melon[0] = melon[0]*1.1
print(tmpDict)

tmpDict1 = {
    "name": "김철수",
    "city": "anyang",
    "age" :  26,
    "grade" : "a=",
    "status" : True
}
#수정
tmpDict1["name"] = "김오티"
print("data-", tmpDict1["name"])

#튜플형식으로 리스트에 담아서 딕셔너리사용
tmpDict1 = dict([
    ("city", "seoul"), ("age", 60)
])
print("type -",type(tmpDict1),tmpDict1)
print("------------------")


tmpdict3 = dict(
city = "seoul",
age = 50)
print("type -", type(tmpdict3),tmpdict3)

print("key를 이용한 값 출력-", tmpdict3["city"])
print("key를 이용한 값 출력 - ", tmpdict3.get("age"))

tmpdict3["name"] = "ddd"
print("data-", tmpdict3)
#위 아래 구문은 같다.
tmpdict3.update({"name":"asdf"})
print("data-", tmpdict3)


#zip()
#case 4



keys = ("apple", "pear", "peach")
values = (1000, 1500, 2000)
zipDict = dict(zip(keys, values))
print("type - ", type(zipDict), zipDict)




keys = ("apple", "pear", "peach")
values = (1000, 1500, 2000)
zipDict = {}
for idx in range(len(keys)):
    zipDict[keys[idx]] = values[idx]

print("type -", type(zipDict), zipDict)


#dict - keys(), values(), items()

for key in zipDict.keys():
    print("{}".format(key, zipDict.get(key)))

for value in zipDict.values():
    print(value)

for key, value in zipDict.items():
    print("{}:{}".format(key, value))

#pop
print("pop -",zipDict.pop("apple"))
print("data -",zipDict)

#전체삭제
zipDict.clear()
print("clear-", zipDict)



'''set 집합의 자료
- 선언 : {}, set()
- 순서 X, 중복 X
- i, s X'''

tmpSet = {1,2,3,3,3,3,3,"asdf"}
tmpSet = set([1,2,3,3,3,3,3,"asdf"])
print("type-",type(tmpSet),tmpSet)

print("dir - ", dir(tmpSet))

tmpT = tuple(tmpSet)
print("type- ", type(tmpT), tmpT)
tmpL = list(tmpSet)
print("type - ",type(tmpL), tmpL)

gender = ["남","남","여","남","여","남","여","남"]
sgender = set(gender)
print("중복제거", sgender)


set01 = set("asdf")
print(set01)

set02 = set([1,2,3,4,5])
set03 = set([3,4,5,6,7])

print("intersection-",set02.intersection(set03))
print("union-",set02.union(set03))
print("difference-",set02.difference(set03))
set02.add(6)
print("add-",set02)

#대량으로 넣을 때 update
set02.update([7,8])
print("update-",set02)

set02.remove(6)
print("remove -", set02)

set02.clear()
print("clear - ", set02)




'''
boolean type
- True | False
- 논리 연산자(not, and, or)
- 비교 연산자(~, &, |)
- "", [], (), {}, 0, None -> False
'''
print("boolean -", bool(-1))
print("boolean -", type([]), bool([]))

trueFlag = True
falseFlag = False
print("T and T- ", trueFlag & trueFlag)
print("T and T- ", falseFlag and trueFlag)
print("T and T- ", trueFlag and falseFlag)
print("T and T- ", falseFlag and falseFlag)

print("T or T- ", trueFlag | trueFlag)
print("T or T- ", trueFlag or falseFlag)
print("T or T- ", falseFlag or trueFlag)
print("T or T- ", falseFlag or falseFlag)

print("not- ", not trueFlag)
print("int - ", int(falseFlag))

"""
날짜(특정 패키지 모듈로 가져와야함.)
"""
from datetime import date, datetime, timedelta

today = date.today()
print("type-", type(today), today)
print(today.year, today.month, today.day)

day_time = datetime.today()
print("type -", type(day_time), day_time)
print(day_time.hour, day_time.minute, day_time.second, day_time.microsecond)

today = date.today()

#relativedelta -> year, month
#pip install python-dateutil
# conda install python-dateutil

'''today= date.today()
day= timedelta(days=-1)
print("하루전 날짜-", type(today), type(day), today+day'''

#날짜타입을 문자열 포맷으로 지정할 수 있다.
#strftime(날짜 -> 문자), strptime(문자 -> 날짜_
'''mydate= datetime(2019,12,25)
print("type -', type(mydate), mydate)
print("format -", mydate.strftime("%m-%d-%y"))
print("forma.t -", type(mydate.strftime("%m-%d-%y")), mydate.strftime("%m-%d-%y:))'''
'''print("문자 -> 날짜 -", type(datetime.strptime(str, %y-%m-%d)))'''

'''사용자 입력'''

name = input("enter your name:")
age = int(input("enter your age:"))
height = float(input("enter your height:"))
marriage = bool(input("enter your marriage :"))
print("input name - ", type(name), name)
print("input age - ", type(age), age)
print("input height - ", type(height), height)
print("input marriage - ", type(marriage), marriage)
print("end--------------")



