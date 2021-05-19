#리스트에서 임의의 원솟값을 업데이트하기

def change(lst, idx, val):
    """list[idx]의 값을 val로 업데이트"""
    lst[idx] = val
    #함수 선언. lst[idx] = val lst의 [idx]번의 인수를 val로 바꾼다는 의미
x = [11, 22, 33, 44, 55]
print('x =', x)

index = int(input('업데이트할 인덱스를 선택하세요. : '))
value = int(input('새로운 값을 입력하세요. : '))

change(x, index, value)
#x라는 리스트에서 바꿔야 하므로 lst값은 위에서 전역설정한 리스트 x로 고정
print(f'x = {x}')


 