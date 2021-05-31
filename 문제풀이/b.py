#3진법 로직 변환(10진법을 N진법으로 변환)

num = 45
answer = ''


while num >= 1:
    rest = num % 3
    num //= 3
    answer += str(rest)



answer = int(answer, 3)

