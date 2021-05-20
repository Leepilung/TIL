#입력받은 숫자가 소수인지 아닌지 판단하는 함수


def isPrimeNumber(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0: return False 
    return True 
num = int(input('소수로 판단할 숫자를 입력하시오. : '))

isPrimeNumber(num)
if isPrimeNumber(num) == True : print('소수입니다.')
else: print('소수가 아닙니다. ')