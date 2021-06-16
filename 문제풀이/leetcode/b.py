#

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palindrome = set()
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                print(i)
                print(j)
                word = s[i:j+1]
                print('word =',word)
                print('palin =',palindrome)
                if word in palindrome:
                    n += 1
                else:
                    pal_word = self.Palindrome(word)
                    print(pal_word)
                    if pal_word:
                        palindrome.add(pal_word)
                        n +=1
                print(palindrome)
                print('중간 n3 = ', n)
                print('----')
        return print('최종값 = ',n)

    def Palindrome(self, s):
        result = True
        start = 0
        end = len(s) -1
        while start < end:
            if s[start] != s[end]:
                result = False
                break
            start += 1
            end -= 1
        return result

Solution().countSubstrings('aaa')