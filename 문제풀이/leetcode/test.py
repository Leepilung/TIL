

words = ["abcd","dcba","lls","s","sssll"]
dict = {}
answer = []

for i in range(len(words)):
    dict[words[i]] = i
    print('dict =',dict)

for i in range(len(words)):
    for j in range(len(words[i])+1):
        print('i',i)
        print('j',j)
        word1 = words[i][:j]
        word2 = words[i][j:]
        print('word1 = ',word1)
        print('word2 = ',word2)
        print('word1[::-1] = ',word1[::-1])
        print('word2[::-1] =',word2[::-1])
        if word1[::-1] in dict:
            if dict[word1[::-1]] != i:
                if word2 == word2[::-1]:
                    answer.append([i,dict[word1[::-1]]])

        if j != 0:
            if word2[::-1] in dict:
                if dict[word2[::-1]] != i:
                    if word1 == word1[::-1]:
                        answer.append([dict[word2[::-1]],i])
        print(answer)
        print('----')