# Programmers 탐욕법(Greedy) - 조이스틱
# https://programmers.co.kr/learn/courses/30/lessons/42860#
# 조이스틱 위 -> 다음 알파벳, 아래 -> 이전 알파벳(역순으로 작동)
# 커서 우측 이동, 첫위치에서 좌측 이동 시 맨끝으로 이동.
# 그리디로만 풀 수 있는게 아닌 그리디문제
# 특정 테스트 케이스의 경우 값이 전부 달라지는 부분도 있음. 제출은 되는데.. 뭔 개같은 경우인지
# 복습 + 다시풀어보기 필수.
# 알파벳 AAA가 기준임. A에서 변하는 값 + 커서가 이동하는 값(커서는 좌측이나 우측 단방향으로 이동하지 않음. 갔던방향을 다시 가기도함. 2번이상은 변화없는듯.)


def solution(name):
    answer = 0
    n = len(name)

    def alpaToNums(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 출력.
        return num_char[ord(char) - ord('A')]

    for i in name:
        answer += alpaToNums(i)

    move = n - 1

    for idx in range(n):
        next_idx = idx + 1
        while (next_idx <n ) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer