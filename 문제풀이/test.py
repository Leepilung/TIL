
txt = ('ABCDEFGHIJKLMP')
skip = [None] * 256
pat = ('ABC')

for pt in range(256):
    skip[pt] = len(pat)
    print(pt)
for pt in range(len(pat)):
    print(pt)
    
    
print(pt)