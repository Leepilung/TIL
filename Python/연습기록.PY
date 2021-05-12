#뒤쪽부터 기록하기 시작.


def 함수명(매개변수1):
    if 매개변수1 == "웅이":
        return
    print("나의 별명은 %s 입니다."% 매개변수1)

함수명('웅이')

#기초값 설정
def 내이름말하기(이름, 나이, 남성=True):
    print("나의 이름은 %s 입니다."% 이름)
    print("나이는 %s살 입니다."% 나이)
    if 남성:
        print("남성입니다.")
    else:
        print("여성입니다.")

내이름말하기 ('이필웅',29)
내이름말하기 ('이필웅',29,True)
#gloabl
a = 1
def 테스트():
    global a
    a = a+1

테스트()
print(a)

#lambda
더하기 = lambda a, b: a+b
result = 더하기(3, 4)
print(result)
#def 함수와 lambda 비교
def 더하기(a,b):
    return a+b

result = 더하기(3,4)
print(result)
