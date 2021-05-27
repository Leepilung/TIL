#고정 길이 스택 클래스 Fixed stack. test 4-1a~c까지 총 합본.

from typing import Any

class FixedStack:
    '고정 길이 스택 클래스문'

    class Empty(Exception):
        '비어있는 FixedStack에 푸시할때 보내는 예외 처리 클래스문'
        pass

    class Full(Exception):
        '가득찬 FixedStack에 푸시할때 보내는 예외 처리 클래스문'
        pass

    def __init__(self, capacity: int = 256) -> None:
        '스택 초기화 하는 함수'
        self.stk = [None]*capacity  # 스택의 본체 크기. 내용물이 None인 배열을 capacity만큼 생성
        self.capacity = capacity    # 스택의 크기를 나타냄
        self.ptr = 0                # 스택 포인터 (시작부분이기 때문에 0으로 초기화)

    def __len__(self) -> int:
        ' 스택에 쌓여있는 데이터 갯수를 반환하는 함수'
        return self.ptr

    def is_empty(self) -> bool:
        '스택이 비어있는지를 판단하는 함수'
        return self.ptr <= 0        # 포인터(ptr)이 0보다 작거나 같으면 무조건 0이므로 스택이 비어있음을 나타냄. 
                                    # 스택이 비어있으면 True, 아니면 False 출력
    def is_full(self) -> bool:
        '스택이 가득차있는 지를 판단하는 함수'
        return self.ptr >= self.capacity    #스택이 가득차있으면 True, 아니면 False 출력
                                            #ptr이 capacity보다 크거나 같으면 가득차있다는 의미.

    def push(self, value: Any) -> None:
        '스택에 value를 푸시(데이터를 넣음)'
        if self.is_full():                  #스택이 가득찬 경우 (is_full에 해당하는 경우)
            raise FixedStack.Full           #full 클래스 raise시킨다.
        self.stk[self.ptr] = value          # self.ptr의 초기값은 0
        self.ptr += 1                       # self.ptr에 가산. 다음 인덱스로 넘어가야 하기 때문

    def pop(self) -> Any:
        '스택에서 데이터를 팝(꼭대기 데이터를 꺼내는 함수)'
        if self.is_empty():                 #스택이 비어있는 경우(is_empty에 해당하는 경우)
            raise FixedStack.Empty          #empty 클래스 raise시킨다.
        self.ptr -= 1                       #스택이 비어있지 않은경우 ptr의 값 -1시키고
        return self.stk[self.ptr]           #stk[ptr]에 저장된 값 반환

    def peek(self) -> Any:
        '스택에서 데이터를 피크(꼭대기 뎅디터를 들여다 봄)'
        if self.is_empty():                 # 스택이 비어있는 경우 볼 원소가 없으므로
            raise FixedStack.Empty          #empty 클래스를 raise 시킨다.
        self.ptr -= 1                       #스택이 비어있지 않은경우 ptr의 값 -1시키고
        return self.stk[self.ptr-1]         #꼭대기 원소의 인덱스값보다 ptr의 값이 1만큼 더 크기때문에 -1해줘야함

    def clear(self) -> None:
        '스택의 모든 데이터를 삭제'
        self.ptr = 0                        # 스택포인터의 값 ptr = 0으로 하면 끝난다.

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