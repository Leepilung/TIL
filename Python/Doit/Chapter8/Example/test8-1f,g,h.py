# test8-1d,e에 이어지는 파일

# test 8-1f remove_first()함수
def remove_first(self) -> None:
    '머리 노드 삭제'
    if self.head is not None:       #리스트가 비어있는 경우
        self.head = self.current = self.head.next
    self.no = -1

# test 8-1g remove_last()함수
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
# test 8-1h remove()함수
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

