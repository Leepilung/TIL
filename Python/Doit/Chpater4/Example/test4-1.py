#고정 길이 스택 클래스 Fixed stack. 입력하면서 이해해보기

from typing import Any

class FixedStack:
    '고정 길이 스택 클래스문'

    class Empty(Exception):
        '비어있는 FixedStack에 푸시할때 보내는 예외 처리 클래스문'
        pass

    class Full(Exception):
        '가득찬 FixedStack에 푸시할때 보내는 예외 처리 클래스문'
        pass

    def __init__(self, capacity: int = 256) -> None:
        '스택 초기화 하는 함수'
        self.stk = [None]*capacity  # 스택의 본체 크기. 내용물이 None인 배열을 capacity만큼 생성
        self.capacity = capacity    # 스택의 크기를 나타냄
        self.ptr = 0                # 스택 포인터 (시작부분이기 때문에 0으로 초기화)

    def __len__(self) -> int:
        ' 스택에 쌓여있는 데이터 갯수를 반환하는 함수'
        return sefl.ptr

    def is_empty(self) -> bool:
        '스택이 비어있는지를 판단하는 함수'
        return self.ptr <= 0        # 포인터(ptr)이 0보다 작거나 같으면 무조건 0이므로 스택이 비어있음을 나타냄. 
                                    # 스택이 비어있으면 True, 아니면 False 출력
    def is_full(self) -> bool:
        '스택이 가득차있는 지를 판단하는 함수'
        return self.ptr >= self.capacity    #스택이 가득차있으면 True, 아니면 False 출력
                                            #ptr이 capacity보다 크거나 같으면 가득차있다는 의미.

