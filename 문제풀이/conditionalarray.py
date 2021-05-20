#주어진 배열에서 홀수는 모두 오른쪽, 짝수는 모두 왼쪽으로 정렬하는 함수를 만들어보세요.
# [1, 2, 3, 4] -> [2, 4, 1, 3]

def conditionalarray(A):
        add1, add2 = [], []
        for i in A:
            if i % 2 == 0:
                add1.append(i)
            else:
                add2.append(i)
        return add1+add2

a = conditionalarray([1,2,3,4])
print(a)