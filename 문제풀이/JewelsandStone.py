#Jewels and Stone 알고리즘
#문자열이 주어지면 보석속에 있는 문자열이 돌에 얼마나있는지를 계산해야함.
#ex) Jewels = "aA" Stone = "aAAbbbbb" 일경우
#Jewels = aA를 a와 A로 나눠야하고 각각의 문자가 stone에 얼마있는지를 계산해야함
#임의의 변수 선언하여 리스트 이용해서 jewels를 나눈다 -> 변수 = list(Jewels)
#이러면 jewels가 쪼개져서 쪼개진 원소들이 남고.
#stone에 있는 변수들을 for문으로 쪼개서 이 원소들이 jewels를 쪼갠 거에 있을경우
#초기값 = 0 인 변수에 하나씩 가산.


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sepjewels = list(jewels)    #[a,A]
        getjewel = 0

        for i in stones:
            if i in sepjewels:
                getjewel += 1
        return getjewel