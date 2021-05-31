#프로그래머스 3진법 뒤집기 문제
#https://programmers.co.kr/learn/courses/30/lessons/68935
#10진법 문자열 n 입력받아서 3진법으로 변환. -> 거꾸로 반전시켜야함 
# 리스트 사용해서 반전해봤으나 좀 꼬임. -> 입력받을때부터 거꾸로 받도록 짜기
#45 입력 -> 1200 -> 0021반전 -> 10진법 변환 -> 7 출력되게.(내장함수 사용하기)


def solution(n):
    answer = ''    
    while n >= 1:
        rest = n % 3
        n //= 3
        answer += str(rest)



    answer = int(answer, 3)
    
    return answer