# LeetCode - > 338. Counting Bits 알고리즘
# 인풋으로 n = 2를 부여받으면 이를 자동 이진수 변환하여 n을 0부터 2까지 나열하여 이진수변환한 후 그 안에 포함된 1을 출력
# ex1) Input : n = 2 Output : [0,1,1] 설명부분 : 0 --> 0     1 --> 1        2 --> 10
# ex2) Input : n = 5 Output : [0,1,1,2,1,2] 설명부분 : 0 --> 0   1 --> 1  2 --> 10    3 --> 11    4 --> 100   5 --> 101
# 제한사항 0 <= n <= 10^5 (1000000)

#우선 for문 사용해서 n까지 나열해야함.
#그 후에 형변환을 하던 해서 1의 갯수를 전부 세고 결과값 배열에 append시키는 방향으로 
#빈 배열 필요함. 위 예시에서 0부터 시작하므로 [0]넣고 시작.

class Solution:
    def countBits(self, n: int) -> List[int]:
        nums_of_one = []  #0부터 n까지 반복하도록 for문 설정. 
        for i in range(n+1):
           nums_of_one.append(bin(i).count('1'))    #문자열'1'카운트
        
        return nums_of_one