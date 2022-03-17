# Programmers level 2 정렬 H-index 알고리즘
# https://programmers.co.kr/learn/courses/30/lessons/42747#
# H-index는 논문 n편 중 h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하로 인용되었다면
# h의 최댓값이 H-index이다.
# 처음 제출시 테스트케이스 9, 16빼고 통과함. 테스트 케이스 9의 경우 [22,42] 2 의 테스트케이스 추가했을 때 
# 디버깅하면 2까지 출력되야 하나 while문 범위를 잘못지정해서 통과를 못했음.
# 테스트 케이스 16의 경우 런타임에러가 떴는데 테스트케이스 16의 경우는 [0,0,0] 0일 때가 해당됨.
# 프로그래머스 사이트로만 풀어봤음. 테스트케이스가 빈약하게 주어지고 틀려도 뭐가틀렸는지 도통 알려주질 않아서 디버깅하는데 애먹음.

 

def solution(citations):
    stack = []
    low = 0
    high = 0
    h_index = 0
    n = len(citations)  # n은 1~1000 // 인용 횟수 h = 0~10000
    citations.sort() # = [0,1,3,5,6]  
    while h_index <= n:
        for i in citations: #- > 0 1 3 5 6
            if h_index >= i:
                low +=1
            if h_index <= i:
                high +=1
        if h_index <= high and h_index >= low:
            stack.append(h_index)
            h_index +=1
            low = 0
            high = 0
        else:
            h_index +=1
            low = 0
            high = 0

    if len(stack) == 0:
        return 0
    else:
        return max(stack)