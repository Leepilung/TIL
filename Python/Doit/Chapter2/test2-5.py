# 튜플, 문자열, 문자열 리스트의 최댓값 구하기


from max import max_of

t = (10 , 20 , 3.14159, 30, 2, 1)
s = "string"
a = ['BTS', 'ABCD', 'Kyochon']

print(f'{t}의 최댓값은 {max_of(t)}입니다.')
print(f'{s}의 최댓값은 {max_of(s)}입니다.')
print(f'{a}의 최댓값은 {max_of(a)}입니다.')
