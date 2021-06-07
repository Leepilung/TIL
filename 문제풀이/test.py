# 눌렀을때 각 손과 2580 버튼의 거리값을 계산해야됨. 예시처럼. 2차원배열 써야될거같은데
# 여기서 거리값을 뭐로 계산해야되냐.. 각각의 인덱스를 빼는방식으로 계산? -> 절대값 써야되는데 거리가 나오나? 아닌거같은데 
# 핸드폰 번호 1번 기점으로 2중 배열로 좌표 딕셔너리로 설정. x.y처럼
# 왼손 오른손의 시작지점이 각각 *와 #에서 시작.
# 1,4,7 누르면 결에 L입력, 왼손이 누른 버튼으로 이동.
# 반대로 3,6,9 누르면 결과에 R입력, 오른손 누른버튼으로 이동해야됨.
# 2,5,8,0 누를 경우가 문제. 2,5,8,0 눌렀을 경우, 거리 계산 해줘야하는데
# 뭐로해주냐.. 예시를 기준으로 잡으면 1 눌러서 left_finger (0,0)
# 3눌러서 rightfinger 3 = (0,2), 4눌러서 left_finger = currnet = phone[4] = (1,0)
# 5누를 경우 phone[5] = (1,1) 
# 현재 rihgtfinger = phone[3] = (0,2) // leftfinger = phone[4] = (1,0)   
# 그럼 각각의 index 0 과 1을 뺀 각각의 절대값을 합치면 절대적인 거리 구할 수 있음.
# 거리 더 낮은쪽이 가까운쪽이 되므로 해당 경우의 수 입력해주고 같을 경우 조건에 맞추기.
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
result = "LRLLLRLLRRL"

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
            else: # right_distance == left_distance
                if hand == 'left':
                    answer += 'L'
                    left_finger = current
                else:
                    answer += 'R'
                    right_finger = current
    return answer
