# Programmers 2018 KAKAO BLIND RECRUITMENT - N진수 게임
# https://programmers.co.kr/learn/courses/30/lessons/17687

# N 진수 게임
# 숫자를 0부터 시작해서 차례대로 말한다. 첫 번째 0, 두번째 1, ~~열번째 9
# 10이상의 숫자 한 자리씩 끊어서 말함. 열 한번째 = 10의자리 1, 열두번째 0 이런식 0,1,2,3,4,5,6,7,8,9,1,0,1,1,1,2 이런식
# 이진수의 경우 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1 이런식.
# 진법 n 구해야할 숫자 갯수 t, 게임참가 인원 m, 튜브 순서 p

# n = 2 t =4 m =2 p =1 이면 2진법, 구해야할숫자 4개, 인원2명, 순서 1번째. -> 0(튜브) 1(상대) 1(튜브), 0(상대), 1(튜브), 1(상대), 1(튜브), 0(상대)
# 여기서 튜브꺼 0,1,1,1,만 출력,

tmp = '0123456789ABCDEF'
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    stack = []
    numlist = list(range(0,m*t))
    for i in numlist:
        stack.append(convert(i,n))

    stack = ''.join(stack)
    stack = list(stack)

    for j in range(p-1,m*t,m):
        answer += stack[j]

    return answer