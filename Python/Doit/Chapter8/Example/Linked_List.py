
from __future__ import annotations
from typing import Any, Type

class Node:
    '연결 리스트용 노드 클래스'

    def __init__(self, data: Any  = None, next : Node = None):
        '초기화'
        self.data = data   #데이터
        self.next = next   #뒤쪽 포인터

class LinkedList:
    '연결 리스트 클래스'

    def __init__(self) -> None:
        '초기화'
        self.no = 0            # 노드의 갯수   
        self.head = None       # 머리 노드
        self.current = None    # 주목 노드

    def __len__(self) -> int:
        ' 연결 리스트의 노드 개수를 반환'
    
    
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
        
    def add_first(self, data : Any) -> None:
        '맨 앞에 노드를 삽입'
        ptr = self.head     #삽입하기 전의 머리 노드
        self.head = self.current = Node(data, ptr)
        self.no += 1

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
            
    def remove_first(self) -> None:
        '머리 노드 삭제'
        if self.head is not None:       #리스트가 비어있는 경우
            self.head = self.current = self.head.next
        self.no = -1
        
    def remove_last(self):
        '꼬리 노드 삭제'
        if self.head is not None:          
            if self.head.next is not None:  # 노드가 1개뿐이라면
                self.remove_first()         # 머리 노드 삭제 함수 실행
            else:
                ptr = self.head             # 스캔중인 노드 포인트
                pre = self.head             # 스캔중인 노드의 앞쪽 노드

                while ptr.next is not None: # ptr.next가 None이면 반복문 중지.
                    pre = ptr
                    ptr = ptr.next
                pre.next = None             # 끝에서 2번째 노드의 포인터부분에 None값 입력
                self.current = pre          # 그렇게 되면 그 뒤의 노드는 참조되지 않으므로 현재값을 pre로 지정
                self.no -= 1                # 노드가 한개 지워진 셈이므로 no값 -1 가산

    def remove(self, p: Node) -> None:
        '노드 p를 삭제'
        if self.head is not None:
            if p is self.head:              # p가 머리노드 일 경우
                self.remove_first()         # 머리 노드 삭제 함수 불러옴
            else:
                ptr = self.head

                while ptr.next is not p:    # ptr.next가 p일때 까지 반복
                    ptr = ptr.next
                    if ptr is None:
                        return              # ptr은 리스트에 존재하지 않는 경우
                ptr.next = p.next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        '주목 노드를 삭제'
        self.remove(self.current)

    def claer(self) -> None:
        '전체 노드를 삭제'
        while self.head is not None:    # 전체가 비어 있을 때까지 반복
            self.remove_first()         # 머리 노드 삭제 함수 실행
        self.current = None             
        self.no = 0

    def next(self) -> bool:
        '주목 노드를 뒤로 한칸 이동'
        if self.current is None or self.current.next is None:
            return False                # 이동이 불가능한 경우 False 출력
        self.current = self.current.next# 이동이 가능한 경우
        return True                     # True 출력

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

