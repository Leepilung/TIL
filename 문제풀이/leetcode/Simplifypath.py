# LeetCode Simplify Path 알고리즘 
# https://leetcode.com/problems/simplify-path/
# 루트 기준으로 '/'는 최상위라 뒤에 ..붙어도 /만 나와야함. 
# level 사용
# stack에 path를 리스트로 나눠서 넣
# for 문에서는 index를 사용하는 반복문 사용하는거 최대한 자제하기. (본문 수정한 코딩)
# 


class Solution:
    def simplifyPath(self, path: str) -> str:
        level = 0
        stack = []
        path_list = path.split('/')
        
        for path in path_list:
            if path != '' and path not in ['.','..']:
                level +=1
                stack.append('/'+ path )
            if path == '..':
                level -= 1
                if len(stack) != 0:
                    stack.pop(-1)

        if len(stack) == 0:
            stack.append('/')
        
        return ''.join(stack)
