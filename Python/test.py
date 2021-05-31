board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]  
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
    
    if bucket[-1] == bucket[-2]:
        bucket.pop(-1)
        bucket.pop(-1)
        answer +=2

    print(bucket)

 