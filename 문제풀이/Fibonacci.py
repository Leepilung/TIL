#피보나치 수열 완성본


def fib(n):
    a = 0
    b = 1
    for index in range(n):
        a, b = b, a + b
        print(a+b, end=" ")
        index += 1
        
        if index%10 ==0:
            print("")

fib(int(input("숫자를 입력하시오")))
