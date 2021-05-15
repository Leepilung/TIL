### 범준표 마름모 그리기.


def getOddByIndex(num):
    return 2 * num - 1

def printPyramidLine(num, count):
    print(' ' * (num - count) + '*' * getOddByIndex(count))

def diamond(num):
    for index in range(getOddByIndex(num)):
        count = index + 1; # 12345
        if index >= num:
            count = getOddByIndex(num) - index # 4321
        printPyramidLine(num, count)

while True:
    diamond(int(input("숫자를 입력하시오 : ")))


### 내가만든 마름모 그리기.

def diamond(num):
    for i in range(1, num+1):
        print(' ' * (num-i) + '*' * (i*2-1))
    for i in range(num,1,-1):
        print(' ' * (num-i+1) + '*' * (i*2-3))

diamond(int(input("숫자를 입력하시오 : ")))

#range(start, stop)

#range(1, 11)은 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 숫자를 생성

#인자를 2개 전달하는 경우 첫번째 인자는 시작하는 숫자가 된다.



#range(start, stop, step)

#range(0, 20, 2)

#0, 2, 4, 6, 8, 10, 12, 14, 16, 18

#마지막 인자 step은 숫자의 간격을 나타낸다.