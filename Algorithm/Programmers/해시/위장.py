# Programmers 코딩테스트 연습 #해시 - 위장 알고리즘
# https://programmers.co.kr/learn/courses/30/lessons/42578#
# 해시 사용 알고리즘. level2 문제
# colthes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]] 이 주어지면
# 스파이가 이를 활용한 의상 조합의 개수를 리턴한다. 위의 예제의 경우 return값 5
# 1. yellow_hat 2. blue_sunglasses 3. green_turban 4. yellow_hat + blue_sunglasses 5. green_turban + blue_sunglasses
# 3개일 경우 5개의 경우의 수.
# clothes = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]] // return = 3
# 1. crow_mask 2. blue_sunglasses 3. smoky_makeup
# dictionary로 옷가지의 타입의 개수를 계산.('face'나 'eyewear' 같은 )
# 없으면 1값. 있으면 1값에 +1씩 가산. 조합해서 입는 경우의 수는 count = 1로 놓고
# 각각의 종류의 벨류값에 +1한것을 가산. 
# 옷을 전부 안입는 경우도 있으므로 마지막에 -1가산.

def solution(clothes):
    closet = {}
    count = 1
    for i in clothes:
        if i[1] in closet: 
            closet[i[1]] += 1
        else: closet[i[1]] = 1
    print(closet)

    for i in closet.values():
        print('i',i)
        count *= (i+1)
    return count -1