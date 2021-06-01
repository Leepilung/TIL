# test8-1a,b와 이어지는 파일

def search(self, data: Any) -> int:
    'data와 값이 같은 노드를 검색'
    cnt = 0
    ptr = self.head
    while ptr is not None:
        if ptr.data == data:
            self.current = ptr
            return cnt
        cnt += 1
        ptr = ptr.next
    return -1

def __contains__(self, data: Any) -> bool:
    '연결 리스트에 data가 포함되어 있는지 확인'
    return self.search(data) >= 0
    