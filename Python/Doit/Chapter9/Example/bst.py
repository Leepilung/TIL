# 책 p 385 이진 검색 트리 구현 실습 예제
# test 9-1a ~ 9-1f까지 합친 파일.

from __future__ import annotations
from typing import Any, Type

class Node:
    '이진 검색 트리의 노드'
    def __init__(self, key:Any, value:Any, left:Node = None, right:Node = None):
            '생성자 부분'
            self.key = key
            self.value = value
            self.left = left
            self.right  = right

class BinarySearchTree:
    '이진 검색 트리'

    def __init__(self):
        '초기화'
        self.root = None    # 루트

    def search(self, key: Any) -> Any:
        '키가 key인 노드를 검색'
        p = self.root       # 루트를 주목하는것부터 시작
        while True:
            if p is None:   # 더 진행할 수 없는 경우
                return None # 검색 실패(None 출력함)
            if key == p.key:# key값이 노드 p와 같은 경우
                return p.value
            elif key < p.key:    #key쪽이 더작은 경우
                p = p.left
            else:                #key쪽이 더 큰 경우
                p = p.right
    
    def add(self, key:Any, value:Any) -> bool:
        '키가 key이고 값이 value인 노드를 삽입'

        def add_node(node: Node, key: Any, value:Any) -> None:
            'node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입'
            if key == node.key:
                return False    #key가 이진 검색 트리에 이미 존재하는 경우 실패
            elif key < node.key:
                if node.left is None:   # 왼쪽 자식노드가 없는 경우
                    node.left is Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:           # key값이 주목 노드보다 큰 경우
                if node.right is None:  # 오른쪽 자식 노드가 없는 경우
                    node.right = Node(key, value, None, None)   #노드 추가
                else:   # 있는 경우 주목 노드를 오른쪽 노드로 변경
                    add_node(node.right, key, value)
            return True

        if self.root is None:         #루트가 없는 경우
            self.root = Node(key, value, None, None)   #루트를 주목노드로 변경
            return True
        else:
            return add_node(self.root, key, value)
        
    def remove(self, key:Any) -> bool:
        '키가 key인 노드를 삭제'
        p = self.root       # 스캔중인 노드
        parent = None       # 스캔중인 노드의 부모 노드
        is_left_child = True    # p는 parte의 왼쪽 자식 노드인지 확인

        while True:
            if p is None:   # 더 이상 진행 불가인 경우
                return False    # 해당 키값 존재하지 않음.
        
            if key == p.key:    # key와 노드 p의 키가 같으면
                break           # 검색 성공
            else:
                parent = p      # 가지를 내려가기전에 부모 설정
                if key < p.key: # key쪽이 더 작으면
                    is_left_child = True    # 왼쪽 자식으로 내려간다
                    p = p.left  # 왼쪽 서브트리에서 검색
                else:
                    is_left_child = False #오른쪽 자식으로 내려간다.
                    p = p.right
        
        if p.left is None:  # p에 왼쪽 자식이 없으면
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right   # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴.
            else:
                parent.right = p.right  # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
        elif p.right is None:   # p에 오른쪽 자식이 없으면
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left    # 부모의 왼쪽 포인터가 왼쪽 자식을 가리킴.
            else:
                parent.right = p.left   # 부모의 오른쪽 포인터가 왼쪽 자식을 가리킴
        else:
            parent = p
            left = p.left   # 서브트리 안에서 가장 큰 노드
            is_left_child = True
            while left.right is not None:   # 가장 큰 노드 left를 검색
                parent = left
                left = left.right
                is_left_child = False
            
            p.key = left.key    # left의 키를 p로 이동
            p.value = left.value   # left의 데이터를 p로 이동
            if is_left_child:
                parent.left = left.left     # left 삭제
            else:
                parent.right = left.left    # left 삭제
        return True
        
    def dump(self) -> None:
        '덤프(모든 노드를 키의 오름차순으로 출력)'

        def print_subtree(node:Node):
            'node를 루트로 하는 서브트리의 노드를 키의 오름차순으로 정렬'
            if node is not None:
                print_subtree(node.left)        # 왼쪽 서브트리를 오름차순으로 정렬
                print(f'{node.key} {node.value}')   # node를 출력
                print_subtree(node.right)       # 오른쪽 서브트리를 오름차순으로 정렬
        
        print_subtree(self.root)
    
    def min_key(self) -> Any:
        '가장 작은 키'
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left
            return p.key
        
    def max_key(self) -> Any:
        '가장 큰 키'
        if self.root is None:
            return None
        p = self.root
        while p.right is not None:
            p = p.right
        return p.key