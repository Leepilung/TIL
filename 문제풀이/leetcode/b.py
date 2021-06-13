matrix =[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
index = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 0:
            index.append((i,j))
            print(i)
            print(j)
            
print(index)
print(index[0][0]) # -> 1
print(index[0][1]) # -> 1

print('-------------------------')
while len(index) != 0:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][index[0][1]] = 0
            matrix[index[0][0]][j] = 0
            
    index.pop(0)

print(index)
print(matrix)

print('-----------------------------------')

# 00 01 02      
# 10 11 12       -> 11이 0이면 01 10 12 21 죄다 0이되야함.
# 20 21 22
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix)

rows = set()
column = set()
m = len(matrix)
n = len(matrix[0])
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            rows.add(i)
            column.add(j)
print(rows)
print(column)

for i in list(rows):
    for j in range(n):
        matrix[i][j] = 0
print(matrix)

for i in range(m):
    for j in list(column):
        matrix[i][j] = 0
print(matrix)