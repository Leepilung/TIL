# LeetCode 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# 정수 배열 nums가 주어지고 nums 배열안에서 가장 큰 합을 가진 하위 배열 출력.
# ex) nums = [-2,1,-3,4,-1,2,1,-5,4] Output = 6 
# 설명 ->  [4,-1,2,1] 부분이 가장 큼.
# ex2) nums = [1] Output = 1 // nums = [5,4,-1,7,8] Output = 23
# dp문제 기본형 참고해서 풀어보기. 빈배열 a 생성.
# a[0] = nums[0] a 배열에는 각 인덱스를 거치며
# for 반복문으로 처음부터 돌면서 계산
# index 1부터 합산하는데 특정인덱스의 값 > 이전 인덱스의 합 일경우 특정인덱스의 값부터 다시 시작.
# 특정 인덱스의 값 이전의 합이 특정 인덱스의 값보다 작을경우(ex index 0~3까지의 합이 4보다 작은경우) 굳이 0~3의 합을 더 해봐야 가장 큰값이 안나오기 때문. 
# max 함수써서 둘중 하나비교해가며 더 큰값 a배열에 가산.

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = [0] * len(nums)
        a[0] = nums[0]
        for i in range(1,len(nums)):
            a[i] = max(nums[i], nums[i] + a[i-1])
        return max(a)