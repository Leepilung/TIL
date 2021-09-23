# Programmers 정렬 level1 -  K번째수 
# https://programmers.co.kr/learn/courses/30/lessons/42748
# 레벨 1문제 답게 기초적인 난이도. 매우 쉬움.

def solution(array, commands):
    answer = []
    for i ,j, k in commands:
        a = array[i-1:j]
        a.sort()
        answer.append(a[k-1])

        
    return answer