# Programmers level2 - 124 나라의 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12899 
# 124 나라에선 숫자가 다음과 같이 표기된다. 1 - 1 // 2 - 2 // 3 - 4 // 4 - 11 // 5 - 12 // 6 - 14
# 3진법 베이스. 3진법과 다르게 3 = 0(자리올림때 자리올림이 되지않고 0대신 4출력.)
# 3의 배수인 경우에만 자리수 문제 해결하기 위해 0을 3으로, n -1해줌.
def solution(n):
    answer = ''
    num = n

    while num >= 1:
        rest = num % 3
        num //= 3
        if rest == 0:
            rest = 4
            num = num -1
        answer += str(rest)
    
    return answer[::-1]

# Programmers 문자열 이용한 다른 풀이.

def solution2(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer