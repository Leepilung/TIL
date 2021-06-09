# LeetCode 97. Interleaving String
# https://leetcode.com/problems/interleaving-string/
# 풀이 by 범준 
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.map = {}
        result = self.check(s1, 0, s2, 0, s3, 0)
        return result

    def check(self, s1, s1Index, s2, s2Index, s3, s3Index):
        if s3Index == len(s3):
            if s1Index == len(s1) and s2Index == len(s2):
                return True
            else:
                return False
 
        key = f'{s1Index}{s2Index}{s3Index}'    # key형태로 결과값 조사한 인덱스 정리해준것.
        if key in self.map.keys():  #key가 self.map 안에 있는경우
            return self.map.get(key)    #self.map에서 key값의 value값 불러옴.
        result = False  # result 기본값 False
        ch = s3[s3Index]
        if s1Index < len(s1) and s1[s1Index] == ch: # s1에 있는 문자열이랑 ch랑 동일하면서 s1인덱스가 s1의 크기보다 작으면
            result = result or self.check(s1, s1Index + 1, s2, s2Index, s3, s3Index + 1)    # 재귀. s1 s3를 비교했으므로 각각 +1
        if s2Index < len(s2) and s2[s2Index] == ch:
            result = result or self.check(s1, s1Index, s2, s2Index + 1, s3, s3Index + 1)    # 재귀 s2랑 s3를 비교했으므로 각각 +1
        self.map[key] = result # 루프.
        return result