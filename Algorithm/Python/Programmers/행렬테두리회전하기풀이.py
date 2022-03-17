# Programeers 2021 Dev-Matching: 웹 백엔드 개발 - 행렬 테두리 회전하기
# https://programmers.co.kr/learn/courses/30/lessons/77485
# 다른 풀이 by 범준
smallest = 0
tmp = -1
def solution(rows, columns, queries):
    tmp = [0] * columns     # tmp = cloumns 만큼 생성
    box = [tmp.copy() for _ in range(rows)]   # box는 이중배열로 [[0]*columns]을 rows만큼 생성한 리스트 
    num = 1
    for i in range(rows):
        for j in range(columns):    # box 00~ 01 02 03~ 순으로 나열
            box[i][j] = num     # num 시작값 1 (예시에서도 값이 1부터 시작함.)을 box에 넣어줌.
            num += 1
    ans = []
    for query in queries:
        rotate(query, box, ans)     # query는 queries의 배열순서로 입력되므로 -> query 첫시작은 예를 들어 [2,2,4,5]
    return ans

def rotate(query, box, ans):    # [2,2,4,5], [num값 입력된 박스배열], 빈 리시트 ans = []
    global smallest         
    global tmp              
    smallest = 9999999999
    tmp = -1
    swapCircle(query[0] - 1, query[1] - 1, "RIGHT", query, box)   # query로 2,2,4,5받으면 [0],[1]은 2,2 인덱스로는 1,1로 시작해야함. query[0] -1 , query[1] -1.시작 direction right.
    ans.append(smallest)    # answer에 smallet를 더해줌

def swapCircle(x, y, direction, query, box):    # 재귀 부분.
    a, b, c, d = [i - 1 for i in query]     # 시작이 x = 1,y = 1, 'RIGHT', query [2,2,4,5], box = 처음 배열. -> a,b,c,d = 1,1,3,4 입력.
    if direction == "RIGHT":        # 디버깅시 print(x,y)
        if y == d:          # y == 4일 때 해당.
            swapCircle(x, y, "DOWN", query, box)    #swapCircle 재귀함수, direction 부분을 "DOWN"으로 바꿈
        else:
            swap((x, y), (x, y + 1), box)       # 변경조건인 if 조건 미충족시 swap함수로 (x,y) 랑 (x,y+1) 변경.
            swapCircle(x, y + 1, direction, query, box) # 재귀함수로 y+1해줌 조건충족할때까지
    if direction == "DOWN":     # 이하 동일.
        if x == c:
            swapCircle(x, y, "LEFT", query, box)
        else:
            swap((x, y), (x + 1, y), box)
            swapCircle(x + 1, y, direction, query, box)
    if direction == "LEFT":
        if y == b:
            swapCircle(x, y, "UP", query, box)
        else:
            swap((x, y), (x, y - 1), box)
            swapCircle(x, y - 1, direction, query, box)
    if direction == "UP":
        if x == a and y == b:
            return
        else:
            swap((x, y), (x - 1, y), box)
            swapCircle(x - 1, y, direction, query, box)

def swap(point1, point2, arr):
    (p1X, p1Y) = point1 #인수로 받은 앞의 (x,y)를 point1, 뒤에 붙는 (x,y+1)을  point2로 놓고 계산
    (p2X, p2Y) = point2
    global smallest
    global tmp
    if tmp == -1:
      tmp = arr[p1X][p1Y]   # tmp에 일시적으로 box배열의 [p1x][p1y]를 인덱스로하는값 넣어줌
    smallest = min(smallest, tmp)   # tmp와 smallest중 작은값 대상으로 
    arr[p2X][p2Y], tmp = tmp, arr[p2X][p2Y], 


solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]])