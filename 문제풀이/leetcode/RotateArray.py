# LeetCode 189. Rotate Array
# https://leetcode.com/problems/rotate-array/submissions/
# nums 길이가 7일떄 k 가 3이면 길이 3만큼 움직여야함. 
# nums = [1,2,3,4,5,6,7] k =3 -> Output = [5,6,7,1,2,3,4]
# nums = [1,2] k = 3 Output = [2,1] 되야함.
# 조건문 + while문 이용 -> 테스트케이스 통과 못함. k 규칙성 찾아야함
# nums = 7일떄 k= 3  k = k % len(nums) -> 3 % 7 =  3
# nums = 2일때 k= 3 k 1번 움직여야함. 3 % 2 = 1. [1,2]에서 한번움직이면 [2,1].
# 통과 실패. 인덱스 나눠서 지정하는 방법도 통과 못함 -> 이유는? nums[:] 전체범위라고 지정을 안해줬기 떄문에 통과를 못함. 

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[len(nums)-k:]+nums[:len(nums)-k]