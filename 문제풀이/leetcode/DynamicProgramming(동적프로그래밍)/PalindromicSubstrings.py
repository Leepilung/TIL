# LeetCode 647. Palindromic Substrings
# https://leetcode.com/problems/palindromic-substrings/
# 문자열 s가 주어지고, 문자열 s에 포함된 Palindromic 하위 문자열의 수를 반환해야한다.
# ex) abc -> 'a', 'b', 'c' Output = 3 // s = 'aaa' -> 'a', 'a', 'a', 'aa', 'aa', 'aaa' 3개 반환.
# for i in range(len(s)), for j in range(i+1,len(s)) -> 하면 aaa 기준 01 02 12 이렇게 검색한다.
# 어차피 문자열 1개 단위는 무조건 카운트하고 들어감. Palindrome인 경우 set()에서 중복없이 카운트.
# Time Limit Exceed. 시간초과뜸.
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palindrome = set()
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                word = s[i:j+1]
                if word in palindrome:
                    n += 1
                else:
                    pal_word = self.Palindrome(word)
                    if pal_word:
                        palindrome.add(pal_word)
                        n +=1

    def Palindrome(self, s):
        start = 0
        end = len(s) -1
        result = True
        while start < end:
            if s[start] != s[end]:
                result = False
                break
            start += 1
            end -= 1
        return result
    



Solution().countSubstrings('aaa')