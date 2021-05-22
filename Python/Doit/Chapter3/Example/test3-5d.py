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