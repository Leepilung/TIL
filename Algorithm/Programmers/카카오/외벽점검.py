# Programmers 2020 KAKAO BLIND RECRUITMENT - 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062
# 완전히 동그란 모양이고 외벽의 총 둘레는 n미터 외벽 몇몇 지점은 추위가 심할 경우 손상될 수 있는 취약 지점이 있음.
# 공사 도중 취약 지점이 손상되지 않았는지 확인하기 위해 주기적으로 친구를 보내서 점검하기로 함.
# 점검시간은 1시간으로 제한, 친구들이 1시간동안 이동할 수 있는 거리는 제각각 다름. 
# 편의상 레스토랑의 정북 방향 지점은 0. 취약 지점의 위치는 정북 방향 지점으로부터 시계방향으로 떨어진 거리를 나타냄. 
# 친구들은 출발 지점부터 시계 OR 반시계 방향으로 외벽 따라 이동.
# 외벽 길이 n 취약지점 위치 담긴 배열 weak, 친구가 1시간동안 이동할 수있는 거리 배열 dist
# 취약지점을 점검하기 위해 보내야하는 친구 수의 최소값을 return 하도록 짜야함.
# 1 <= n <= 200 // 1 <= len(weak) <= 15 // weak는 오름차순 정렬. 0이상 n-1이하의 정수
# 1 <= len(dist) <= 8 // dist는 1이상 100이하의 자연수
# 친구 모두 투입해도 취약 지점 점검 불가 시 -1 return
# ex) n = 12 // weak = [1, 5, 6, 10] // dist = [1,2,3,4] -> result = 2
# ex2) n = 12 // weak = [1,3,4,9,10] // dist [3,5,7] -> result = 1

# ex 1의 경우 dist 4로  10m지점 출발 시계방향 1m위치까지 점검.
# weak의 최적 해 배열찾는 함수 짜야함. 시간순으로 24시까지 표현하도록구성.
# [1, 5, 6, 10]	[1, 2, 3, 4]	
# [1, 5, 6, 10, 13 ,17, 18, 22] -> weak + 12(n)+weak
# ex 1의 경우 10~1 거리 3 5~6거리 dist 1
# ex 2의 경우 반시계로 계산하면 4m 지점에서 반시계로 하면 한방에 끝. 4~0 0~9 = 4+ 3 in dist = 1
# 10~13, 17~18 1.
# 1,5 -> dist안에 있음. 56 있음 6 10 있음 
n = 12
weak = [1, 5, 6, 10]	
dist = [1, 2, 3, 4]

dict={}
count = 0
real_weak = weak + [i+n for i in weak]
visit = [0]*len(real_weak)
print(real_weak)
print(visit)
for i in range(len(real_weak)):
    for j in range(len(real_weak)):
        weak_distance = real_weak[j] - real_weak[i]
        if i == j:
            continue
        if weak_distance not in dist:
            continue
        else:
            print(f'i={i},j={j}',weak_distance)
            dict[weak_distance] =(i,j)

print(dict)

print(visit)
def solution(n, weak, dist):
    answer = 0
    return answer

