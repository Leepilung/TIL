#커서로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:
    '연결 리스트용 노드 클래스(배열 커서 버전)'

    def __init__(self, data = Null, next = Null, dnext = Null):
        '초기화'
        self.data = data    # 데이터
        self.next = next    # 리스트의 뒤쪽 포인터
        self.dnext = dnext  # 프리 리스트의 뒤쪽 포인터

class ArrayLinkedList:
    '연결 리스트 클래스(배열 커서 버전)'

    def __init__(self, capacity : int):
        '초기화'
        self.head = Null    # 머리 노드
        self.current = Null # 주목 노드
        self.max = Null     # 사용중인 꼬리 레코드
        self.deleted = Null # 프리 리스트의 머리 노드
        self.capacity = capacity    # 리스트의 크기
        self.n = [Node()] * self.capacity   # 리스트의 본체
        self.no = 0

    def __len__(self) -> int:
        '연결 리스트의 노드 수를 반환'
        return self.no

    def get_insert_index(self):
        '다음에 삽입할 레코드의 인덱스를 구함'
        if self.deleted == Null:    #삭제 레코드가 존재하지 않는 경우
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max     # 새 레코드 사용
            else:
                return Null         # 크기 초과
    
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext    #  프리 리스트에서 맨 앞 rec을 꺼내기
            return rec
    
    def delete_index(self, idx: int) -> None:
        '레코드 idx를 프리 리스트에 등록'
        if self.deleted == Null:
            self.deleted = idx
            self.n[idx].dnext = Null
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec
        
    def search(self, data: Any) -> int:
        'data와 같이 같은 노드를 검색'
        cnt = 0
        ptr = self.head             # 현재 스캔 중인 노드
        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = self.n[ptr].next
        return Null 