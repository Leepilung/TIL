# LeetCode Path with Maximum Gold
# Related Topic - BackTracking
# https://leetcode.com/problems/path-with-maximum-gold/
# 2중 배열 grid가 주어지고 배열안의 숫자는 그 칸의 금매장량을 의미한다.
# 0이 아닌 칸으로 이동 할 수 없으며 한번 이동한 칸으로는 다시 갈 수 없다.
# 이 때 금매장량이 최대치가 되는 경로의 금 매장량의 합을 출력하도록 해야함.
# 보기와 같은 경우 최대치는 9 -> 8 -> 7 의 경로가 해당되므로 출력은 24가 나와야한다.
# 재귀를 사용해야함 -> 처음 구성은 재귀함수 구성하고 재귀함수가 돌았던 부분을 딕셔너리에 기록하고 딕셔너리에 있을 경우 못가는
# 재귀함수로 짜봤으나 재귀함수를 아래부분에 짰더니 매개변수 참조에 있어서 에러가 발생함. 
# Type Error int object subscriptable 에러가 발생. def 함수 위로 올리고 조건을 아예 바꿔서 새로짬
# y와 x가 0보다 크고 len(grid) or len(grid[0])보다 작은 경우를 만족 and 0값이 아닐때 현재 골드값을 지속적으로 가산
# 그리고 마지막에 재귀를 끝났을때 토탈골드와 현재골드중 큰값 계산하는 방향으로 짰음
# 엄청 오래걸림. 재귀는 아직 미숙한듯. 디버깅도 힘들고 
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # grid = [[0,6,0],
        #         [5,8,7],
        #         [0,9,0]]
        def count(y,x,gold):
            if len(grid) > y >= 0:
                if len(grid[0]) > x >= 0:
                    if grid[y][x] > 0:
                        cur_gold = grid[y][x]
                        grid[y][x] = 0
                        count(y+1,x,cur_gold+gold)
                        count(y-1,x,cur_gold+gold)
                        count(y,x+1,cur_gold+gold)
                        count(y,x-1,cur_gold+gold)
                        self.totalGold =max(self.totalGold, cur_gold+gold)
                        grid[y][x] = cur_gold

        self.totalGold = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != 0:
                    count(y,x,0)

        return self.totalGold
``