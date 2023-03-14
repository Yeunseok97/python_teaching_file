#단어의 빈도수를 구하기
# {"love": 2. "word" : 2, "cat" : 1}
word_vec = ["love", "word", "love", "cat", "word"]
print("len - ", len(word_vec))
a={}


#case1
a={}
for word in word_vec:
    a[word] = a.get(word, 0) + 1
print("case 01-", a)

#case2
a={}
for word in word_vec:
    a[word] = word_vec.count(word)
print("case 02-", a)

#case3
a={}
for word in word_vec:
    if word in a :
        a[word] += 1
    else:
        a[word] = 1
print("case 03", a)

#case04
a= dict(
    love = word_vec.count("love"),
    word = word_vec.count("word"),
    cat = word_vec.count("cat"),
)
print("case 04 a- ", a)

#case 05
#set, zip

print("set-", set(word_vec))
print("comprehension -", [word_vec.count(i) for i in set(word_vec)])
result = dict(zip(set(word_vec), [word_vec.count(i) for i in set(word_vec)]))
print("case05 ", result)

