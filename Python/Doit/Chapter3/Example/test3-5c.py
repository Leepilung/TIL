# 이해가 필요함. 추가로 공부 필요성 있는 부분.

def search (self, key : Any) -> Any:
    """키가 key인 원소를 검색하여 값을 반환"""
    hash = self.hash_value(key)     #검색하는 키의 해시값에 해당
    p = self.table[hash]            #노드를 주목?

    while p is not None:
        if p.key == key:
            return p.value          #검색 성공
        p = p.next                  #뒤쪽 노드를 주목

    return None                     #검색 실패

def add(self, key:Any, value: Any) -> bool:
    """키가 key이고 값이 valueㅇ인 원소를 추가"""
    hash = self.hash_value(key)     #추가하는 key의 해시값
    p = self.table(hash)            #노드를 주목?

    while p is not None:
        if p.key == key:
            return False            # 추가 실패
        p = p.next                  # 뒤쪽 노드를 주목

    temp = None(Key, value, self.table[hash])
    self.table[hash] = temp         # 노드 추가
    return True                     # 추가 성공
