# LeetCode 336. Palindrome Pairs
# https://leetcode.com/problems/palindrome-pairs/
# 고유 단어 목록이 들어있는 리스트가 주어지면 두 인덱스 쌍 (i,j) or (j,i)를 반환할 때 두 단어의 결합이 리턴되도록 해야함.
# ex) words = ["abcd","dcba","lls","s","sssll"] Output = [[0,1],[1,0],[3,2],[2,4]]
# ["dcbaabcd","abcddcba","slls","llssssll"] 와 같이 나옴.
# Time Limit 에러. hash 테이블 사용해야 할듯. 
# words에 있는 단어들을 키로, i값을 벨류로 하는 for문 생성.
# for i~ for j 이중 for문 사용. word1은 :j까지 word2는 j:부터 표기.
# word[i]의 단어를 단어의 개수만큼 하나하나 word1으로 표기했을 때
# word1[::-1] 이 dict안에 있고(word1과 대칭이여야 조합가능)
# dict[word1[::-1]] != i -> 0,0같은 형태는 나올 수 없기 때문에 != i 사용
# word2 == word2[::-1]:의 경우 print해서 하나하나 과정을 살펴보면 word2->word1으로 표기가 끝난경우
# 남아있어야 하는 문자열이 없어야함.
# 그다음 if j!= 0 의 경우 j는 문자열의 길이만큼 나열하는데 j = 0일 경우에는
# word2가 전체를 나열중이라 word1과 비교해서 조합되는 수를 찾을 수가 없음.
# word[2::-1]이 dict에 있는경우 -> 예시에서 i2 j2의 경우 해당.
# 이 경우 s는 dict[3]에 해당되고 이 때 word1 == word1[::-1]이면
# s와 조합시 좌우대칭Palindrome 성립. 그러므로 answer에 [dict[word2[::-1]],i] 추가.
from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        dict = {}
        answer = []

        for i in range(len(words)):
            dict[words[i]] = i

        for i in range(len(words)):
            for j in range(len(words[i])+1):

                word1 = words[i][:j]
                word2 = words[i][j:]

                if word1[::-1] in dict:
                    if dict[word1[::-1]] != i:
                        if word2 == word2[::-1]:
                            answer.append([i,dict[word1[::-1]]])

                if j != 0:
                    if word2[::-1] in dict:
                        if dict[word2[::-1]] != i:
                            if word1 == word1[::-1]:
                                answer.append([dict[word2[::-1]],i])
        return answer


# --------------------------------------------------
# 디버깅 + 전개과정 확인 및 수정 코드


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