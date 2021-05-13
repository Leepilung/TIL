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

#input 사용예제
숫자 = input("숫자를 입력하시오")

print(숫자)


#Print 사용 예제
변수1 = 2021
print(변수1)

print("hello","my","yesterday")

for i in range(3):
    print(i, end=(" "))

# 파일 생성
f = open("새파일.txt", 'w')
f.close

# 파일 경로지정 생성
f = open("/home/ek3434/TIL/Python/새파일.txt","w")
f.close

#파일 쓰기모드로 작성
f = open("/home/ek3434/TIL/Python/새파일.txt","w")
for 변수 in range(1, 5):
    데이터 = "%d번째 줄입니다.\n" % 변수
    f.write(데이터)
f.close()

#파일 읽기모드(루프사용)
f = open("/home/ek3434/TIL/Python/새파일.txt","r")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

#파일 읽기모드(readlines)
f = open("/home/ek3434/TIL/Python/새파일.txt","r")
line = f.readlines()
for 줄 in line:
    print()
f.close()


#파일 읽기모드(read사용)
f = open("/home/ek3434/TIL/Python/새파일.txt","r")
데이터 = f.read()
print(데이터)
f.close

#with문
f = open("/home/ek3434/TIL/Python/새파일.txt",'w')
f.write("삶은 매우 짧다. 파이썬이 필요하다")
f.close()

