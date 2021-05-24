def solution(priorities, location):
    answer =0
#우선순위에 갯수가 0이 아닐떄까지 반복해야함
    while len(priorities) != 0:
#priorities[0] = 최상단이  priorities에서 가장클 경우
        if priorities[0] == max(priorities):
#정리하면 priorities[0] == max(priorities)
            answer += 1
#그리고 가장 클경우에 return값 1되야 하므로 answer에 1 가산해야함.
            priorities.pop(0)
            if location == 0:
                return answer
#priorities[0] = max(priorities) 성립하고 loaction = 0이면 answer가 답이므로 출력
#그러나 위의 조건은 성립하고 location이 아니면 -1씩 반복해서 맞춰줌.
            else:
                location -= 1
#print(priorities[0])        -> 2
#print(max(priorities))      -> 3
#print(priorities)           -> [2,1,3,2]
#priorities.append(priorities.pop(0)) -> [1,3,2,2]
#print(priorities)           ->  [1,3,2,2]
#이렇게 되면 priorities의 값이 priorities[0]과 같지 않을 경우 priorities[0]의 
#값을 뽑아다가 맨뒤로 append 시킨다.
        else:
            priorities.append(priorities.pop(0))
            if location = 0:
                location == len(priorities) -1
            else: 
                location -= 1
#priorities의 값을 하나씩 빼서 위의 식이 같을때까지 뒤로 추가해야함.
#priorites.append(priorites.pop(0))
#  이 경우 priorities[2,1,3,2] => [1,3,2,2]
#그리고 다시 반복했을때 priorities[0] =! max(priorities)가 되므로
#priorities.append(priorities.pop(0)) -> priorities[1,3,2,2] -> [3,2,1,1]
#다시 반복할 경우 priorities[0] == max(priorities)가 성립.
#answer 에 +1 가산
#그러나 location은 2이였으므로 반복해서 -1씩 뺴야함.

#에러 발생
#디버그 필요함. else:부분에서 append 했을때 [2,1,3,2] -> [1,3,2,2]가 될경우
#location -1되야함. 초기 3의 인덱스가 2-> 1로 됐기 때문에.
#그러나 location이 0이라면 맨끝으로 돌려야함
# 식으로 바꾸면 len(priorities) -1.로 초기화시켜야함.
#  0에서 -1이 되면 안되므로.
#------
#첫번째 테스트케이스 [2,1,3,2] ,2 는 통과
#두번째 테스트 케이스 [1,1,9,1,1,1] ,0 실패 5가나와야 하는데 1이나옴. 이유는?
#원인을 모르겠음.. 스방.. 원인이 돋대체 뭐지?
print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))
print(solution([1,1,9,1,1],1))