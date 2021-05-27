#4-1a에 이어지는 내용, 예제 해석해보기

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
    