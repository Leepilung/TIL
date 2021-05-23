#prices = {1, 2, 3, 2, 3, 1} return {5, 4, 1, 2, 1, 0}
#prices = [1, 2, 3, 2, 3]	return	[4, 3, 1, 1, 0]
#1초시점 -> 끝까지 가격안내려감. 2초시점 -> 
#1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
#2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
#3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
#4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
#5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
#시간순 배열할 시 1초일때 주식가격은 1 떨어지지 않은 시간은 4가 출력된다.


def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    for p in range(n):
        #시간순으로 0부터 5까지 나열된다고 가정해보자.(1~6초)
        while stack and prices[stack[-1]] > prices[p]:
            #stack이 빈칸이 아니고 prices[top] > prices[p]
            top = stack.pop()
            answer[top] = p - top
        stack.append(p)

    while stack:
        top = stack.pop()
        answer[top] = p - 1 - top

    return answer

