# Programmers 해시 - 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577#
# 접근법 감을 못잡고 시작해서 해맴.
# 폰북의 번호가 다른번호의 접두일경우 false, 아니면 true 출력
# sort함수로 phone_book 정렬하면 접두어가 같은 경우 바로 뒤에 정렬됨.
# 풀이 해매서 꽤 걸림. 1시간 42분

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) -1):
        if len(phone_book[i]) <= len(phone_book[i+1]):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
                break
    return answer