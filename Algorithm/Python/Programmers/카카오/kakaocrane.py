# 2차원 배열 5x5형태에서 moves -> 1,5,3,5,1,2,1,4면 2차원 배열에서 각 열에 위치하는 값을 뽑아감.
# board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
# moves = [1, 5, 3, 5, 1, 2, 1, 4]      return = 4
# moves를 해석하면 1열에서 하나뽑고 5열에서 하나뽑고 3열에서 하나뽑고 5열,1열,2열,1열,4열 순


def solution(board, moves):
    answer = 0
    bucket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                bucket.append((board[j][i-1]))
                board[j][i-1] = 0
                break
            else:
                continue

        if bucket >= 2 and bucket[-1] == bucket [-2]:
            bucket.pop(-1)
            bucket.pop(-1)
            answer +=2
    return answer
