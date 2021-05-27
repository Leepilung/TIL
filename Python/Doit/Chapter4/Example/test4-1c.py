def find(self, value:Any) -> Any:
    '스택에서 value를 찾아 인덱스를 반환(없으면 -1을 반환한다)'
    for i in range(self.ptr -1, -1, -1):    #ex) self.ptr = 7이면 (6,-1,-1) 6부터 -1까지 -1의 간격으로 검색
        if self.stk[i] == value:            # 6 5 4 3 2 1 0 이런순으로 검색함.
            return i                        #검색 성공시 i값 출력
        return -1                           #검색 실패시 -1출력

def count(self, value: Any) -> bool:
    '스택에 있는 value의 개수를 반환'
    c = 0
    for i in range(self.ptr):       #예를 들어 스택 = [19,25,37,53,25,17] 이라면
        if self.stk[i] == value:    #25라는 value를 검색할 시 self.stk[i] == value 일때마다
            c += 1                  #c 에 1씩 가산되므로 c 의 값은 2가 나온다.
        return c

def __contains__(self, value:Any) -> bool:
    '스택에 value값이 포함되있는지 판단'
    return self.count(value)        # count 함수를 불러와서 값이 있는경우 True, 아니면 False를 출력

def dump(self) -> None:
    '덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)'
    if self.is_empty():             #스택이 빈경우 
        print('스택이 비어있습니다.')
    else:
        print(self.stk[:self.ptr])      #self.ptr까지 출력.