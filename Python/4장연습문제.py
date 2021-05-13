#Q1.

#주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.

def is_odd(a):
    if a %2 == 0:
        print("%d는 짝수입니다."% a)
    else:
        print("%d는 홀수입니다."% a)
    return a
    
a = is_odd(int(input("숫자를 입력하시오")))

#풀기 성공(Suceess). input 활용하여 숫자 입력 가능하게 하고 4입력
#> python3 ./BASIC.PY
#숫자를 입력하시오 4
#4는 짝수입니다.

#Q1. - Lambda 활용

is_odd = lambda a: a %2 == 0
result = is_odd(int(input("숫자를 입력하시오")))
if result == True:
    print("짝수입니다")
else:
    print("홀수입니다")

#풀기 성공(Success). 기존 문제에서 요구하는것과 달리 숫자입력 부분으로 판단하게 하였고 짝수인지 홀수인지를 알려주도록 만들어봤음
#> python3 ./BASIC.PY
#숫자를 입력하시오4
#짝수입니다
#> python3 ./BASIC.PY
#숫자를 입력하시오3
#홀수입니다

#Q2.

#입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.


def avg_number(*입력값들):
    result = 0
    for i in 입력값들:
        result += i
    return result / len(입력값들)

a = avg_number(1, 2, 3, 4, 5)
print(a)

#★풀기 실패(Failure)★. 입력으로 들어오는 매개변수의 값이 고정되지 않았을때 *매개변수 사용하는것 잊지말기.
#결과의 계산값은 result로, 매개변수에 입력되는 튜플값을 차례대로 입력하는 인수는 i로
#result += i 로 입력값들에 지정된 숫자가 i에 의해 하나씩 더해지고
#return 으로 입력값들의 총합 / len(입력값들)의 갯수로 평균값 구함
#a = def함수명(입력값들)와 같이 def함수로 정의된 함수를 별도로 출력하기 위해선 변수 설정 해줘야함.


#Q3.

#다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
#3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)

#풀기 성공(Success). int 함수의 개념에 대해 조금더 공부하기.
#int 함수는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수이다.
#기존에 36 입력시 36으로 출력되는건 정수의 합이 아닌 문자열의 합으로 인식되어서라고 판단. total 부분에서 input 1, 2를 정수로 바꿔주면 된다도 생각하였다.

#Q4

#다음 중 출력 결과가 다른 것 한 개를 골라 보자.

print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

#.풀기성공(Success). 3번째 위치한 print("you", "need", "python") ','표시는 문자열간에 간격을 나타내는 명령어이기 때문.
#4번째 join문의 동작과정이 자세하게 기억나지 않으니 복습할 것. -> basic.md 참조
#join문 사용시 join(["you", "need", "python"])의 경우 각각의 문장을 잇는경우 전체를 []로 감싸지 않으면 join함수가 매개변수 인식을 제대로 못함.
#join문 사용시 join("youneedpthon")의 경우 문장사이별로 "-"로 구분이 잘됨.

print("-".join("youneedpython"))

#Q5

#다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.

#f1 = open("test.txt", 'w')
#f1.write("Life is too short")

#f2 = open("test.txt", 'r')
#print(f2.read())

# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

#풀기 실패(Failure)
#파일을 닫지 않은상태에서 다른파일을 열면 저장한 데이터 값을 읽는것이 불가능하다.
#그래서 f1 open->close -> f2 open의 순서를 지켜줘야한다.

#with구문을 사용한 경우는 다음과 같다.
with open("test.txt",'w') as f1:
    f1.write("Life is too short!")
with open("test.txt",'r') as f2:
    print(f2.read())

#Q6

#사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.
#(단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)

input = input("저장할 내용을 입력하세요 : ")
f1 = open("test.txt", 'a')
f1.write(input)
f1.write("\n")
f1.close()

#풀기실패(Failure). 별도의 입력창을 만들어줬어야함 input함수로
#입력끝난후에 write("\n")과 같이 줄바꿈 명령어도 필요함.

#Q7.

#다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

#Life is too short
#you need java

f = open('test.txt','r')
수정사항 = f.read()
f.close()

수정사항 = 수정사항.replace('java','python')

f = open('test.txt', 'w')
f.write(수정사항)
f.close()

#풀기 실패(Failure). replace 함수를 처음봤음. replace 함수에 대해 공부가 필요.
#변수 f를 test.txt 'r'의 형태로 선언
#수정사항 = f.read함수로 선언
#f. 문서를 닫고 수정사항 변수에서 replace함수 사용하여 변경사항 반영하여 재선언
#변수 f를 test.txt의 'w'쓰기로 선언
#write로 replace로 바뀐 수정사항 작성
