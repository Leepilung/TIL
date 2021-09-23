# Programmers 그래프 - 가장 먼 노드
# https://programmers.co.kr/learn/courses/30/lessons/49189
# by 범준

graph = {}
def solution(n, edge):
    for [node,to] in edge:
        if not graph.get(node):
            graph[node] = []
        if not graph.get(to):
            graph[to] = []
        graph[node].append(to)
        graph[to].append(node)
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    depth = 1
    queue = [1]
    level = [1]

    while len(queue):
        node = queue.pop(0)
        visited[node] = True
        connected = graph.get(node)
        level.pop(0)
        for target in connected:
            if not visited[target]:
                visited[target] = True
                distance[target] = depth
                queue.append(target)
        if not len(level):
            level = queue.copy()
            depth += 1
    distance.sort(reverse=True)
    ans = 0
    prev = distance[0]
    for d in distance:
        if prev != d:
            break;
        ans += 1
    return ans