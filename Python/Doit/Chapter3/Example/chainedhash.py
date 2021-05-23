# hash 3-5 a~d까지 총합본.

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시 구성하는 노드"""

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        """초기화"""
        self.key = key          #키
        self.value = value      #값
        self.next = next        # 뒤쪽 노드를 참조

class Chainedhash:
    """체인법으로 해시 클래스 구현"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity                # 해시 테이블의 크기를 지정
        self.table = [None] * self.capacity     # 해시 테이블(리스트)을 선언

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key,int):                 # key가 int형인 경우 해당.
                return key % self.capacity
        return(int(hashlib.sha256(str(key).endcode()).hexdigest(), 16) % self.capacity)     # 표준 라이브러리 사용 예
        #haslib에서 sha256을 사용하여 바이트 문자열의 해시값을 구하는 해시 알고리즘 생성자를 생성한다.
        # 그 뒤에 hashlib.sah256에 바이트 문자열의 인수를 전달해야 하므로 key를 str형 문자열로 변환한 뒤, 그 문자열을 encode() 함수에 전달
        # hexdigest()함수는 sha 256 알고리즘에서 해시값을 16진수 문자열로 꺼낸다.
        # int()함수 : hexdigest()함수로 꺼낸 문자열을 16진수 문자열로 하는 int형으로 변환한다.
 
    def search(self, key : Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)     #검색하는 키의 해시값에 해당
        p = self.table[hash]            #노드를 주목?

        while p is not None:
            if p.key == key:
                return p.value          #검색 성공
            p = p.next                  #뒤쪽 노드를 주목

        return None                     #검색 실패

    def add(self, key:Any, value: Any) -> bool:
        """키가 key이고 값이 value인 원소를 추가"""
        hash = self.hash_value(key)     #추가하는 key의 해시값
        p = self.table[hash]            #노드를 주목?

        while p is not None:
            if p.key == key:
                return False            # 추가 실패
            p = p.next                  # 뒤쪽 노드를 주목

        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp         # 노드 추가
        return True                     # 추가 성공

    def remove(self, key: Any) -> bool:
        """키가 key인 원소를 삭제"""
        hash = self.hash_value(key)     #삭제할 key의 해시값
        p = self.table[hash]            #노드를 주목
        pp = None                       #바로 앞의 노드를 주목

        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return TimeoutError     #key 삭제 성공
            pp = p
            p = p.next                  #뒤쪽 노드를 주목
        return False                    #삭제 실패(key가 존재하지 않는경우)

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]       
            print(i, end='')
            while p is not None:
                print(f' ->{p.key}({p.value})',end = '')
                p = p.next
            print()

