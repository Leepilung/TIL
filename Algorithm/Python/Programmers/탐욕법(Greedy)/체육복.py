# Programmers 탐욕법(Greedy) - 체육복
# https://programmers.co.kr/learn/courses/30/lessons/42862#
# n은 전체 학생수 // lost는 체육복을 잃어버린 학생의 번호가 담긴 배열 // reserve는 여벌의 체육복이 있는 학생의 배열
# 체육복 여벌이 있는경우 자기번호 바로 앞,뒤 +-1의 번호에 체육볼 빌려줄 수 있음.
# 자기 자신이 잃어버린 목록에 있으나 여벌의 체육복이 있는경우 누구에게도 빌려줄 수 없음.
# for문 사용시 자기 자신을 즉시 지울경우 for문의 길이가 짧아져 for문 반복이 완벽하게 종료되지 않음. -> copy()로 같은 개체 만듦
# 지가 잃어버리고 여분이 있는 경우를 배열에서 아예 제거함.(복사해서 참조, 제거는 본분으로 진행)
# 그렇게 하면 이제 앞,뒤에 빌려줄 수 있는 경우만 참조해서 구하면됨.
# level 1이라더니 테스트케이스때문에 애먹은 문제. 결국 IDE로 일부분 전개과정 테스트 진행하였음(for문)

def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    lo_copy = lost.copy()
    re_copy = reserve.copy()
    # n 전체학생수 // lost 도난당한 학생들의 번호  // reserve 여벌옷이 있는 학생들
    for i in lo_copy:
        if i in re_copy:
            reserve.remove(i)
            lost.remove(i)
        else:
            continue
            
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer += 1
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer += 1
            
    return n - len(lost) + answer