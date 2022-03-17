# Programmers 정렬 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746
# 다른 풀이 찾는데 실패.
# key=lambda x : '조건' 사용 명확하게 기억해두기
# x*3을 하는 이유 = x*3을 해야 x = [221,2,10]의 경우 x*3을 해버리면
# [221221221, 222, 101010] 이렇게 된다. 이걸 정렬로 나열하면 101010, 221221221, 222 순으로 나열되나
# x*2를 하면 x*2기준일때 [221221, 22, 1010] 이 되므로 1010, 22, 221221 이순서로 22보다 221이 더큰순서로 
# 인식되어 정렬되기 때문. 제한사항이 ~1000까지 인걸 기억하자.

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    print(numbers)
    return str(int(''.join(numbers)))
