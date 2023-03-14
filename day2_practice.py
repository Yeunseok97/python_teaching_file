# ---list 실습



movie_lst = ['이터널스', '스파이더맨', '매트릭스', '경관의 피', '상치', '스타워즈', '아이언맨']
print('type -', type(movie_lst))
print('data -', movie_lst)

# 문제1
# 영화 '모가디슈' 추가
print('01A -')
movie_lst.append('모가디슈')

print('02A -')
movie_lst.insert(2,'임섭순')

print('03A -')
idx = movie_lst.index('경관의 피')
movie_lst.pop(idx)

print('04A - ')
del movie_lst[3]
del movie_lst[3]

idx1 = movie_lst.index('이터널스')
movie_lst.pop(idx1)



print(movie_lst)





plist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
plist.append(11)
del plist[0::2]
plist.pop(3)
plist.reverse()
plist.sort()
plist.insert(3, 7)
print(plist)


# 1 ~ 99 정수 중 짝수만 튜플에 저장한다면?

even_data = tuple(range(2, 100, 2))
print("type", type(even_data), even_data)

# packing & unpacking
packing = ("a", "b", "c", "d")
x1, x2, *x3, x4 = packing
print(x1, x2, x3, x4)