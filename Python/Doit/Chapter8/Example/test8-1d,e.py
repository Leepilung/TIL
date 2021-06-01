# test8-1a,b,c와 이어지는 파일
# test8-1d

def add_first(self, data : Any) -> None:
    '맨 앞에 노드를 삽입'
    ptr = self.head     #삽입하기 전의 머리 노드
    self.head = self.current = Node(data, ptr)
    self.no += 1

# test 8-1e
def add_last(self, data: Any):
    '맨 끝에 노드를 삽입'
    if self.head is None:       #리스트가 비어있는 경우를 의미
        self.add_first(data)
    else:
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = self.current = Node(data, None)
        self.no += 1
        