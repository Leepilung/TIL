s1 = "aabcc" 
s2 = "dbbca" 
s3 = "aadbbcbcac"


#s1[0] == s3[0] == -> 재탐색
#s1[1] == s3[1] -> 재탐색
#s1[2] != s3[2] -> s2에서 찾기.
#s2[0] == s3[2] -> s2에서 재탐색
i1 = 0
i2 = 0
i3 = 0
while i1 == len(s1) or i2 == len(s2):
    if s1[i1] == s3[i3]:
        i1 += 1
        i3 += 1
    elif s2[i2] == s3[i3]:
        i2 +=1
        i3 +=1
    else: # s3[i3] != s1[i1] and s3[i3] != s2[i2]:
        print(False)
        break
    if i3 == len(s3):
        print(True)
        break