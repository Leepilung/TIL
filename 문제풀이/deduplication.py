#주어진 배열에서 반복되는 숫자를 전부 제거하는 함수를 만들어보세요.
#[1, 1, 2, 2, 4, 4, 4, 1] -> [1, 2, 4, 1]

list = list(map(int, input('리스트를 입력하시오. ex) 1 2 3 4 : ')))
#map, split 쓰면 연달아 입력할 수 있음. 이를 int로 숫자형 ->list로 리스트형으로 변환

def deduplication(num):
    numset = set(num) #중복제거는 set함수 이용.
    print(numset)

deduplication(list)

