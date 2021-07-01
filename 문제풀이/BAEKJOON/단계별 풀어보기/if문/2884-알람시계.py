# 백준 알고리즘 - if문 - 2884. 알람 시계
# https://www.acmicpc.net/problem/2884
# 알람 문제. 시간 H와 분을 나타내는 M이 주어지고 H(0~23) M(0~59)의 범위를 갖고 24시간 표현을 사용한다.
# 입력값 H M보다 45분일찍 일어나도록 설정해야하는 문제
# * 실수한 점
# elif 부분을 M -45 > 0으로 표기한점(분이 0일떄를 포함안시켰음) + elif로 하기전에 else로 한점(23 40일 때 전부 출력됨)
# 24시간 표현인데 M -45 < 0 인 경우에 H를 11로 설정한 점등이 실수한 부분이다.

while True:
    nums = input().split()
    H = int(nums[0])
    M = int(nums[1])
    
    if 23 >= H >= 0:
        if 59 >= M >= 0:
            break
        else: continue
    else: continue

timeloss = 0
if M - 45 < 0:
    if H == 0:
        H = 23
        M = M +15
        print(str(H)+' '+str(M))
    else:
        H = H -1
        M = M + 15
        print(str(H)+' '+str(M))
elif M - 45 >= 0:
    M = M - 45
    print(str(H)+' '+str(M))