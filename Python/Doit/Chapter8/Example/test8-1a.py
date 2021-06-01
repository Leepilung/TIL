 #포인터로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any, Type

class Node:
    '연결 리스트용 노드 클래스'

    def __init__(self, data: Any  = None, next : Node = None):
        '초기화'
        self.data = data   #데이터
        self.next = next   #뒤쪽 포인터

        