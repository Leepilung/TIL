#주어진 배열에서 반복되는 숫자를 전부 제거하는 함수를 만들어보세요.
#A[start] == A[i] -> len(A)
#start = 0 -> start < len(A)
# start = 0 A =[1,2,2,4,4,4,1] -> start = 0 LEN(A) = 7 start = 0 < len 6
# start = 0 A[0] != A[1] -> else -> start += 1 start =1 
# start = 1 A[1] == A[2] -> DLEA[2] A = [1,2,4,4,4,1] - start = 1 LEN(A) =6 start = 1 < len 5
# start = 1 A[1] != A[2] -> else -> start +=1 start =2
# start = 2 A[2] == A[3] -> DLE A[3] A = [1,2,4,4,1] -> start = 2 LEN(A) = 5 start = 2 < len 4
# start = 2 A[2] == A[3] -> DLE A[3] A = [1,2,4,1] -> start = 2 LEN(A) = 4 start = 2 < len 3
# start = 2 A[2] != A[3] -> else -> start +=1 start =3 start 3 <= len(3)
# start = 3 A[3] != A[4] -> else -> start +=1 start =4
A = [1, 1, 2, 2, 4, 4, 4, 1]

def duplication(A):
    start = 0
    while start < len(A)-1:
        if A[start] == A[start +1]:
            del A[start+1]
        else:
            start += 1
    return len(A)

print(duplication(A))