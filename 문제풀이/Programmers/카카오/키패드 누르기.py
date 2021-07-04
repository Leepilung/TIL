# Programmers 2020 카카오 인턴십 - 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256
# 키패드가 주어졌고 왼손 위치와 오른손 위치간의 거리도 계산해야됨
# 가운데 2580 입력시 가까운 손쪽으로 입력 + 같은거리면 사용하는 주 손에 따라 그 손으로 결정
# 키패드 그대로 옮겨서 가상의 원점이 0부터 시작. x,y축 있다고 가정하고 2중배열 작성하기.
# 시작손은 각각 #이랑 *
# 3눌러서 rightfinger 3 = (0,2), 4눌러서 left_finger = currnet = phone[4] = (1,0)
# 5누를 경우 phone[5] = (1,1) 
# 현재 rihgtfinger = phone[3] = (0,2) // leftfinger = phone[4] = (1,0)   
# 그럼 각각의 index 0 과 1을 뺀 각각의 절대값을 합치면 절대적인 거리 구할 수 있음.
# 거리 더 낮은쪽이 가까운쪽이 되므로 해당 경우의 수 입력해주고 같을 경우 조건에 맞추기.

def solution(numbers, hand):
    answer = ''
    phone = {
        1 : (0, 0),   2 : (0, 1),   3 : (0, 2),
        4 : (1, 0),   5 : (1, 1),   6 : (1, 2),
        7 : (2, 0),   8 : (2, 1),   9 : (2, 2),
      '*' : (3, 0),   0 : (3, 1), '#' : (3, 2)
    }
    left_finger =  phone['*']
    right_finger = phone['#']
    
    for i in numbers:
        current = phone[i]
        if i in [1,4,7]:
            answer += 'L'
            left_finger = current

        elif i in[3,6,9]:
            answer += 'R'
            right_finger = current
        
        else: # if i in [2,5,8,0]:
            left_distance = abs(left_finger[0] - current[0]) + abs(left_finger[1] - current[1])
            right_distance = abs(right_finger[0] - current[0]) + abs(right_finger[1] - current[1])

            if left_distance < right_distance:
                answer += 'L'
                left_finger = current
            elif left_distance > right_distance:
                answer += 'R'
                right_finger = current
            else: # right_distance
                if hand == 'left':
                    answer += 'L'
                    left_finger = current
                else:
                    answer += 'R'
                    right_finger = current
    return answer