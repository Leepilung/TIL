# LeetCode - Contanier With Most Water 알고리즘
# https://leetcode.com/problems/container-with-most-water/
# 음이 아닌 정수 a1,a2..~~ n개가 주어짐.
# 수직선은 (i,ai)와 (i,0)에 있도록 그려지고 x축의 길이와 함께 컨테이너에 물을 가장 많이 넣을수 있는 두 선을 찾아야함.
# x축의 길이는 맨 끝선의 인덱스 - 좌측선의 인덱스
# y축 길이는 좌측선 우측선 둘중 더 작은쪽
# height = [1,8,6,2,5,4,8,3,7] Output = 49  // height = [1,1] Output = 1
# area값은 반복문 돌면서 비교하면서 가장 큰값 갱신해야 하므로 max(area, ~~~)형태.

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftline = 0
        rightline = len(height) -1
        area = 0
        while leftline < rightline:
            area = max(area, (rightline - leftline) * min(height(leftline),height[rightline]))
            if height[leftline] <= height[rightline]:
                leftline += 1
            else:
                rightline -= 1
        return area