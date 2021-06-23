# LeetCode 90. Subsets 2 알고리즘
# Related Topic - Array , Backtracking
# https://leetcode.com/problems/subsets-ii/
# 정수 배열 nums가 주어지면 nums로 조합할 수 있는 모든 경우의 수를 하위 배열로 출력해야 하는 문제
# ex) nums [1,2,2]이면 Output = [[],[1],[1,2],[1,2,2],[2],[2,2]] 이 출력되야함.
# 내장함수 이용시 스택형태로 입력이 안되므로 사용 불가. 순열의 경우도 동일.
# 재귀함수 사용 -> 처음에 원하는 값까지 출력이 다됐으나 뒤에서 나오지 말아야할 값중복되서 출력됨.
# loop 함수부분에 if문으로 걸렀으나 테스트케이스 통과못함 -> nums 배열 sort() 하니 해결
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        stack = []
        nums.sort()
        self.loop(nums, [], stack)
        return stack

    def loop(self, nums, cur, stack):
        if cur not in stack:
            stack.append(cur)
        for i in range(len(nums)):
            self.loop(nums[i+1:],cur + [nums[i]], stack)

