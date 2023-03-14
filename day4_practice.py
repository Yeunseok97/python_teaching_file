'''input()함수를 이용해서 연도와 월을 입력받아
해당년도가 윤년일 경우 2월달의 마지막은 29
평년일경우 2월의 마지막일은 28
출력형식 : xxxx년 x월 마지막일은 xx일입니다.'''



# ld = 0
# y = int(input("연도를 입력하세요 : "))
# m = int(input("월을 입력하세요 : "))
#
# if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
#     ld = 31
# elif m == 4 or m == 6 or m == 9 or m == 11:
#     ld = 30
# else:
#     if (y%4 == 0 and y%100 != 0) or y%400 == 0:
#         ld = 29
#     else:
#         ld = 28
# print("%d년 %d월 마지막일은 %d일입니다."%(y,m,ld))

''''''''''''''''''''''''''''''''''''''''''''''''''''''

# ld = 0
# y = int(input("연도를 입력하세요"))
# m = int(input("월을 입력하세요"))
#
# year_month = [31,28,31,30,31,30,31,31,30,31,30,31]
# lyear_month = [31,29,31,30,31,30,31,31,30,31,30,31]
#
# if (y%4 == 0 and y%100 != 0) or y%400 == 0:
#     print("{}년{}월 마지막일은{}이다".format(y, m, lyear_month[m-1]))
# else:
#     print("{}년{}월 마지막일은{}이다".format(y, m, year_month[m-1]))

''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 중첩구문

# year = int(input("연도를 입력하세요"))
# month = int(input("월을 입력하세요"))
# lst31 = [1,3,5,7,8,10,12]
# if month != 2:
#     if month in lst31:
#         print("{}년{}월 마지막일은31".format(year,month))
#     else:
#         print("{}년{}월 마지막일은30".format(year, month))
# else:
#     if (year%4 == 0 and year%100 != 0) or year%400 == 0:
#         print("{}년{}월 마지막일은29".format(year, month))
#     else:
#         print("{}년{}월 마지막일은28".format(year, month))
#
#


#while 루프 실습 10고개

# from random import randint
#
# answer = randint(1,100)
# print("answer",answer)
#
# tries = 1
# while tries <10:
#
#     tries +=1
#
# print("정답{}, 시도횟수 {}".format(answer,tries))

''''''''''''''''''''''''''''''''''''''''''''''''''''''
# from random import randint
#
# answer = randint(1,100)
#
# tries = 0
# user_answer = 0
# while tries<10:
#     user_answer = int(input("맞춰보세요"))
#     if answer < user_answer:
#         print("숫자가 큽니다 맞춰보세요")
#         tries += 1
#     elif answer > user_answer:
#         print("숫자가 작습니다 맞춰보세요")
#         tries += 1
#     else:
#         print("정답입니다")
#         break
# print("정답{}, 시도횟수{}".format(answer, tries))



#올림픽은 4년개최
#2022, 2050년 사이의 올림픽이 개최되는 년도를 출력
# 한 줄에 5개의 년도씩 출력

# cnt = 0
# for i in range(2000,2051,4):
#     cnt +=1
#     if cnt%5 ==0:
#         print(i, end = "\n")
#     else:
#         print(i, end ="\t")
#
# print()
#
# lst = []
# tmpLst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in tmpLst:
#     if i % 2 == 0:
#         lst.append(i**2)
# print("sqr lst - ", lst)
#
#
# lst = [i**2 for i in tmpLst if i%2 ==0]
# print("sqrt com -",lst)


# 세 글자 이상 문자만 출력
tmpLst = ["I", "am", "studying", "PYTHON","!!!"]
# lst = [i for i in tmpLst if len(i) >=3]
# lst = []
# for i in tmpLst:
#     if len(i)>=3:
#         lst.append(i)
# print("3 over", lst)

# lst = []
# for i in tmpLst:
#     if i.isupper():
#         lst.append(i)

# lst =[i for i in tmpLst if i.isupper()]

#확장자를 제외하고 파일 이름만 출력하고 싶다.


lst = []
tmpLst = ["greeting.py",
          "ex01.py",
          "intro.hwp",
          "bigdata.doc",
          "machine_learning.jupyter"]

for data in tmpLst:
    lst.append[a][0]
print(lst)


for idx in range(len(tmpLst)):
    print(tmpLst[idx].split(".")[0])