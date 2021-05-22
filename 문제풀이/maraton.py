#마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
# 참가자 그룹, 완성그룹 비교
# 참가자들을 딕테이션으로 키 값으로 입력. 빈 딕테이션 생성 필요.
# p가 딕테이션에 없을경우 벨류값 0부여. 있을경우 +1씩 가산(동명이인)
# 아예 출력 None일경우 () completion에 없는 케이스 이므로 이 경우가 탈락자에 해당
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    answer = ''
    group = {}                          #빈 딕테이션 group 생성
    for member in participant:          # participant를 순서대로 나열
        if member not in group:
            group[member] = 1           #나열했을때 이름이 없으면 1 부여
        else :                                  
            group[member] = group.get(member) +1    #이름이 존재하면 +1씩 가산.(동명이인)
    for winner in completion:
        group[winner] = group.get(winner) -1        #완주자 이름의 키값이 있을경우 -1씩 뺴서 검증
    
    for member in participant:          #이제 다시 멤버를 키로하는 벨류값을 나열했을때
        if group[member] == 1:          #완주자에서 빼고도 이름(키)에 대한 벨류가 1이면
            answer = member             #남아있는 1이 탈락자에 해당.

    return answer

print(solution(participant,completion))