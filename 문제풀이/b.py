def binary_search(s, e):
    while True:
        mid = (s + e)// 2
        if (mid ** 2) == N:
            return mid
        elif mid ** 2> N:
            e = mid
        else:
            s = mid

def bin_search(a: Sequence, key: Any) -> int:
    pl = 0                                          # 검색 범위 맨 앞 원소의 인덱스
    pr = len(a) - 1                                 # 검색 범위 맨 끝 원소의 인덱스

    while True:
        pc = (pl + pr) // 2                         #중앙 원소의 인덱스
        if a[pc] == key:
            return pc                               #pc = key값 즉 검색 성공시
        elif a[pc] < key:                           
            pl = pc +1                              # 검색 범위를 뒤쪽 절반으로 좁힘.
        else:
            pl = pc -1                              # 검색 범위를 앞쪽 절반으로 좁힘.
        if pl > pr:
            break
        return -1            


#배열이 [5,6,1,2,3,4]
nums = [5,6,2,3,4,]
start = 0
end = len(nums-1)

start < end 
 mid = start + end //2
start = 0, end = 5
 처음시작 mid = 0+5 // 2 = 2  num[2] = 1, end= nun[5] = 4
 num[mid] < num[end] -> end = mid

    