
# #Que 1
# def que01():
#     with open("../data/special_words.txt", "r", encoding = "utf8"):
#         lines = file.readline().split()
#         lines = [i.strip(",.") for i in lines]
#         print(lines)
#         for word in lines:
#             if "c" in word:
#                 print(word)
# #caller
# que01()
#
# #que2
# #cnt_words.txt파일로부터 줄 단위로 읽어서 단어의 길이가
# #10 이하인 단어 출력하고 카운팅
# def que02():
#     cnt = 0
#     with open("../data/special_words.txt", "r", encoding = "utf8"):
#         lines = file.readline().split()
#         lines = [i.strip(",.") for i in lines]
#         print(lines)
#         for word in lines:
#             if len(word) < 3:
#                 cnt += 1
#                 print(word)
#     print("10이하인 단어의 갯수 :{}".format(cnt))
#
#
#Que 3
def que03():
    dong = input("동 입력하세요. 예시)개포:")
    # print("dong -", dong)
    try:
        with open("../data/zipcode.txt", "r", encoding = "utf-8") as file:
            line = file.readline()
            while line:
                addr_lst = line.split("\t")
                if addr_lst[3].startswith(dong):
                    print(addr_lst)
                line = file.readline()
    except Exception as e:
        print(str(e))
#caller
que03()




#zipcode.txt
#input()함수를 이용햇 ㅓ동 이름을 입력받아
#해당 동 주소 출력
#hint - \t
#startswith()함수
#예외처리리#