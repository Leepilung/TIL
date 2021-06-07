phone = {
    1 : [0, 0],   2 : [0, 1],   3 : [0, 2],
    4 : [1, 0],   5 : [1, 1],   6 : [1, 2],
    7 : [2, 0],   8 : [2, 1],   9 : [2, 2],
  '*' : [3, 0],   0 : [3, 1], '#' : [3, 2]
}

left_s = phone[4]
right_s = phone[3]
now = phone[5]
print(phone[1]) #벨류값 출력됨. 0> (0,0)


left_distance = abs(left_s[0] - now[0]) + abs(left_s[1] - now[1])
print(left_distance)
right_distance = abs(right_s[0] - now[0]) + abs(right_s[1] - now[1])
print(right_distance)