# 10진수를 N진수로 변환해야됨.
# divmod로 몫, 나머지 구하기.

tmp = '0123456789ABCDEF'  
# tmp =  string.digits+string.ascii_lowercase와 동일 다만 이렇게 사용할시 import string 넣어줘야함.
def convert(num, base) :    
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
    
print(convert(10,2))