# LeetCode 137. Single Number II
# https://leetcode.com/problems/single-number-ii/
# 정수로된 배열 array가 주어지고 모든 요소는 단 1개의 원소를 제외하고 3번 나타나는데  이 때 저 제외된 원소를 나타내야함.
# ex) nums = [2,2,3,2] Output = 3 // nums = [0,1,0,1,0,1,99] Output = 99
# 무조건 선형 검색 해야하는듯.
# 키 밸류(딕셔너리) 사용하기. for문으로 나열. 없으면 i를 키로해서 벨류값 1로 넣고, 존재할경우 벨류값에 1씩 가산.
# 끝난다음에 딕셔너리for문돌려서 벨류값이 1인 경우 출력하도록 구성.

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}

        for i in nums:
            if i not in count:
                count[i] = 1
            elif i in count:
                count[i] += 1

        for i in count:
            if count.get(i) == 1:
                return i
