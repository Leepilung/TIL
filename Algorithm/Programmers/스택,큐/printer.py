#priorities = [2,1,3,2], 중요도는 C D A B 즉 3,2,2,1 순으로 입력. 
#location = 2일 경우 3이 몇번째로 출력되는지 알고싶은 문제. 저 문제에선 가장 큼으로 return = 1
#location은 인덱스.

def solution(priorities, location):
    answer = 0

    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            answer += 1
            priorities.pop(0)
            if location == 0:
                return answer
            else:
                location -= 1
                
        else:
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) -1
            else: 
                location -= 1