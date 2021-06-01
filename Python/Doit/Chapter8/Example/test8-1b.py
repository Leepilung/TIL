# test7-1a.py와 이어지는 파일.

class LinkedList:
    '연결 리스트 클래스'

    def __init__(self) -> None:
        '초기화'
        self.no = 0            # 노드의 갯수   
        self.head = None       # 머리 노드
        self.current = None    # 주목 노드

    def __len__(self) - > int:
        ' 연결 리스트의 노드 개수를 반환'
        