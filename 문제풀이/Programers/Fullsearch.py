#주어진 답배열에서 수포자 1,2,3의 답안 패턴을 비교하여 최다 득점자를 출력하는 함수.
#공동일경우 오름차순 배열.
#각 수포자 배열 존재. 점수를 기준으로 줄세움. 수포자중 수포자1이 가장높으면 1출력
#2,3이 공동이면 2,3출력.
#초기 버전 테스트케이스 3개만 통과후 에러남. 
#1차 디버깅 범위 각각 * 200, 125, 100 -> 절반만 통과. 테스트케이스 더 큰경우
#제한 조건이 최대 10000문제 였으므로 10000에 맞춰서 수정-> 테스트 케이스 올 통과.
def solution(answers):
    answer = []
    point = [0] * 3
    loser1 = [1,2,3,4,5] * 2000
    loser2 = [2,1,2,3,2,4,2,5] * 1250
    loser3 = [3,3,1,1,2,2,4,4,5,5] * 1000
   
    for i in range(0, len(answers)):
        if answers[i] == loser1[i]:
            point[0] +=1
        if answers[i] == loser2[i]:
            point[1] +=1
        if answers[i] == loser3[i]:
            point[2] +=1

    winner = max(point)    

    for j in range(0,3):
        if point[j] == winner:
            answer.append(j+1)
    
    return answer
