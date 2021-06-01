# test 8-1 i

def print_current_node(self) -> None:
    '주목 노드를 출력'
    if self.current is None:
        print('주목 노드가 존재하지 않습니다.')
    else:
        print(self.current.data)

def print(self) -> None:
    '모든 노드를 출력'
    ptr = self.head

    while ptr is not None:
        print(ptr.data)
        ptr = ptr.next

# test 8-1 j 이터레이터용 클래스 구현

def __iter__(self) -> LinkedListIterator:
    '이터레이터 반환'
    return LinkedListIterator(self.head)

class LinkedListIterator:
    '클래스 LinkedList의 이터레이터용 클래스'

    def __init__(self, head: None):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data

