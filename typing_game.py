import time
import random
w = ["cat", "dog", "fox", "mouse", "frog", "lion", "sweetpotato", "potato", "grape"]
n = 1
input("[타자게임] 준비되면 엔터키 입력")


start = time.time()
q = random.choice(w)

while ( n <= 5):
    print("*문제",n)
    print(q)
    x = input()
    if q == x:
        print("통과")
        n += 1
        q = random.choice(w)
    else:
        print("오타 다시도전")
end = time.time()
et = (end - start)%1
print("타자시간은" ,et, "초입니다")