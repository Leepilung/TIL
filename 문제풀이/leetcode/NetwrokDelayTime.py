# LeetCode 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/
# 다익스트라 알고리즘
# 깡으로 다푸는 알고리즘 by 범준

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        node = defaultdict(list)
        delay = [999] * (n + 1)
        
        for start, end, time in times:
            node[start].append((start, end, time))
        
        delay[0] = 0
        delay[k] = 0
        
        queue = []
        for path in node[k]:
            queue.append(path)
            
        while queue:
            s, e, t= queue.pop(0)
            delay[e] = min(delay[e], delay[s] + t)
            for start, end, time in node[e]:
                if delay[end] > delay[start] + time:
                    queue.append((start, end, time))
        largest = max(delay)
        
        return largest if largest != 999 else -1

# 우선순위 큐 사용 알고리즘
import collections
import heapq

class Solution2(object):
    def networkDelayTime2(self, times, N, K):
        graph = collections.defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))
        pq = [(0, K)]
        dist = {}
        while pq:
            delay, node = heapq.heappop(pq)
            
            if node in dist: continue
            dist[node] = delay
            for neighbor, delay2 in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (delay+delay2, neighbor))

        return max(dist.values()) if len(dist) == N else -1

# 큐 사용 2
from typing import List
class Solution3:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for u, v, w in times:
            if u not in graph.keys():
                graph[u] = [(v, w)]
            else:
                graph[u].append((v, w))

        min_heap = [(0, k)] 
        costs = {}

        while len(min_heap) != 0:
            cost, node = heapq.heappop(min_heap)   
            if node in costs.keys():  
                continue
            costs[node] = cost
            if node not in graph.keys():
                continue
            for neighbor, c in graph[node]:
                if neighbor not in costs.keys():
                    heapq.heappush(min_heap, (cost + c, neighbor))
        
        if len(costs) == n:
            return max(costs.values())
        else:
            return -1