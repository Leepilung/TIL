# Programmers 그래프 - 가장 먼 노드 알고리즘.
# https://programmers.co.kr/learn/courses/30/lessons/49189#
# n = 6 edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]] 의 이중배열 일 때 return = 3이 나오도록 해야함.
# deque 사용.
# for i in edge 사용. graph 3은 6과 연결되어있으므로 3에는 6, 6에는 3추가하는 방식으로 반복
# for문돌아서 나오는 graph는 각 노드가 어떤 노드들과 연결되있는지를 나타냄
# 이제 각 노드를 돌면서 거리를 계산해야함.

def solution(n, edge):
    graph = [[] for i in range(n+1)] # 인덱스는 0, 노드는 1부터시작하기 때문에 n+1
    for i in edge:
        print(i)
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
        print(graph)
    stack = [] #시간복잡도 개선하려면 deque 사용.
    visited=set()   # 중복 허용하지 않기위해서 사용
    stack.append(1) 
    visited.add(1)
    print('visited = ',visited)
    distance=[0 for i in range(n+1)]
    print(distance)
    while stack:
        node = stack.pop(0)  # deque 사용시 popleft()로 바꾸면됨.
        print('node =',node)
        for j in graph[node]:
            print('j =',j)
            if j not in visited:
                visited.add(j)  # 방문한 곳 의미
                print(visited)
                stack.append(j) # 연결된 노드
                print(stack)
                distance[j] = distance[node]+1  # 1을 기점으로 하는 거리 ex) distance[3] = distance[1] +1
                print(distance)
    answer = distance.count(max(distance))
    return answer

solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])

# deque 사용한 시간복잡도 개선시 아래와 같음.

from collections import deque

def solution2(n, edge):
    graph = [[] for i in range(n+1)]
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    queue = []
    visit = set()
    queue.append(1)
    visit.add(1)
    distance = [0 for i in range(n+1)]
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if i not in visit:
                visit.add(i)
                queue.append(i)
                distance[i] = distance[node]+1
    answer = distance.count(max(distance))
    return answer

    