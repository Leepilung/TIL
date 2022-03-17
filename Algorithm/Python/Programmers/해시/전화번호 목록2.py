# Programmers 해시 - 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577#
# 해시 이용해서 풀기

def solution(phone_book):
    hashMap = {}
    for i in phone_book:
        hashMap[i] = 1
    for i in phone_book:
        temp = ''
        for j in i:
            temp += j
            print(temp)
            if temp in hashMap:
                if temp != i:
                    return False
    return True


solution(["12","123","1235","567","88"])
# phone_book = ["12","123","1235","567","88"] 일때
def solution2(phone_book):
    for i in phone_book:
        temp = ''
        for j in i:
            temp += j
            print(temp)
# 이중 for문  출력값 1 , 12 // 1 , 12 , 123 // 1 , 12 , 123 , 1235 // 5 , 56 , 567 // 8 , 88 이런식으로 출력됨.