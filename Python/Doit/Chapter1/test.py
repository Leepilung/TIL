##전역 변수와 함수 내의 지역변수의 객체 식별번호 출력

x = 33 #전역 변수(함수 내부, 외부에서 사용 가능)

def putid():
    y = 33
    print(f'id(y) = {id(y)}')

print(f'id(33) = {id(33)}')
print(f'id(x) = {id(x)}')
putid()

