# for 반복문으로 처음부터 돌면서 계산
# index 1부터 합산하는데 특정인덱스의 값 > 이전 인덱스의 합 일경우 특정인덱스의 값부터 다시 시작.
# 특정 인덱스의 값 이전의 합이 특정 인덱스의 값보다 작을경우(ex index 0~3까지의 합이 4보다 작은경우) 굳이 0~3의 합을 더 해봐야 가장 큰값이 안나오기 때문. 
# max 함수써서 둘중 하나비교해가며 더 큰값 a배열에 가산.
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = [0] * len(nums)
        print('a의 초기 배열 =',a)
        a[0] = nums[0]
        for i in range(1,len(nums)):
            a[i] = max(nums[i], nums[i] + a[i-1])
            print(a)
        return print(max(a))

Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
#for문 직접 검증해보기
#-2부터 시작.
#a[0] = nums[0]-> -2. a[0] = -2 for i in range 1~9. 1~8까지 출력.
#a[1] = max(nums[1], nums[1] + a[1-1 = 0]) -> a[1] = max(1, 1 + -2 = -1) a[1] = 1
#a[2] = max(nums[2], nums[2] + a[1]) -> a[2] = max(-3,-3+1 = -2) a[2] = -2
#a[3] = max(nums[3], nums[3] + a[2]) -> a[3] = max(4,4+(-2) = 2) -> a[3] = 4 
#a[4] = max(nums[4], nums[4] + a[3]) -> a[4] = max(-1,-1+4 = 3) -> a[4] = 3
#a[5] = max(nums[5], nums[5] + a[4]) -> a[5] = max(2,2+3 =5 ) -> a[5] = 5
#a[6] = max(nums[6], nums[6] + a[5]) -> a[6] = max(1,1+5 = 6) -> a[6] = 6 -> 예시에서의 최대값

