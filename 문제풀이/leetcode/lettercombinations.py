# LeetCode Letter Combinations of a Phone 알고리즘
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 번호 입력받으면 그번호의 영문자 조합으로 출력될 수 있는 모든 경우의 수 출력
# digits의 최대 길이는 4 ex)2345
# digits[i]의 범위는 2~9까지.
# 복습 필요.

letterMap = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        if not len(digits):
            return []
        self.traverse(0, '', ans, digits)
        return ans
    def traverse(self, index: int, current: str, ans: List[str], digits: str):
        if index == len(digits):
            ans.append(current)
            return
        chars = letterMap.get(digits[index])
        for char in chars:
            self.traverse(index + 1, current + char, ans, digits)