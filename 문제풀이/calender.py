
#참고) 윤달 규칙
#1) 4년으로 나누어지는 해는 윤달(2월은 29일)이 있다. 
#2) 그러나 100년으로 나누어지는 해는 윤달이 없다. 
#3) 그러나 400년으로 나누어지는 해는 윤달이 있다. 이 규칙을 만족해야만 그 해가 윤년(2월은 29일)이고 
#아닌 경우에는 평년(2월은 28일)이다.
#날짜의 시작 기준은 1년 1월 1일 월요일이다.

dayofmonth = {0 : 31, 1 : 28, 2 : 31, 3: 30, 4 : 31, 5 : 30, 6 : 31, 7 : 31, 8 : 30, 9 : 31, 10 : 30, 11 : 31}
#Enddate에서 해당 달의 일 수를 전부 더해야하므로 해당 달에 맞는 일수를 미리 딕셔너리로 선정.


def intercalation(year):
    return year % 4 == 0 and year % 400 == 0 and year % 100 != 0
#윤달 판단 함수 True면 윤달 Flase면 비 윤달

def inputdate(date):
    #입력받은 날짜를 연 월 일로 나눠주는 함수
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])
    return (year, month, day)

def CalStartday(year, month, day):
    #마지막 날짜를 년,월,일값으로 입력받아 1년 1월 1일 기준으로 언제부터 시작해야하는지 알려주는 함수
    result = (year -1) * 365
    #날짜의 시작 기준을 1년 1월 1일로 잡았기 때문에 년도에 1-해서 시작.
    for i in range (year):
        if intercalation(i +1):
            result += 1

    for i in range (11):
        #1월부터 12월까지의 달을 기준으로 입력달로 그달까지의 일수를 구하는 함수
        if month <= i+1:
            break
        #i는 0부터 시작하나 월은 1월부터 시작하므로 +1을 해준다.
        if intercalation(year) == True and i +1 == 2:
            result = result + dayofmonth[i] + 1
            #윤달이 있는 년도이고, i가 2월이면 결과값에 +1을 해준다.
        else:
            result = result + dayofmonth[i]
            #윤달이 아니라면 그냥 정상적으로 해당 달에 해당하는 일자를 더해준다.
   
    result += day
    return result % 7
    #결과값을 7로 나누는 이유는 결과값을 7로 나눠서 0 일요일 1 월 2 화 3 수 4 목 5 금 6 토 로 결과값을 통해 시작하는 요일을 구할 수 있기 때문

def drawcalender(date):
    (year, month, day)= inputdate(date)
    #inputdate함수로 입력받은 년 월 일을 리스트로 바꿔 해당 함수의 인수로 사용시키는 함수
    Startday = CalStartday(year, month, 1)
    #해당 월에 시작할 날짜를 고르는 함수.
    print("=" * 28)
    print(' 일',' 월',' 화',' 수',' 목',' 금',' 토')
    print("=" * 28)
    lineswitch = 0
    for i in range(7):
        #시작 위치 앞에 공백을 넣는 반복문
        if i < Startday:
            #i부터 공백을입력하는데 startday보다 크면 시작숫자가 밀리므로 i < startday로 써줘야함
            print("{:^4}".format(""),end="")
            #빈칸("")의 포맷을 가운대정렬로 4칸출력하고 칸띄우기 대신 end =""로 붙이는 명령어
            lineswitch +=1
            # for문을 사용했기때문에 i가 빈 공백을 그릴때마다 +1씩 가산.

    for i in range(31):
        #1일부터 31일까지 출력하는 반복문
        day = i + 1
        # i 는 0부터 시작하기 때문에 +1을 붙여준다.
        lineswitch += 1
        # 위에서 공백부분과 이유 동일.
        print("{:^4}".format(day), end="")
        # day = i+1이기 때문에 그것에 걸맞는 숫자값을 앞에 가운데정렬4칸의 공백과 함께 출력
        if day == dayofmonth[month] and not intercalation:
            print('')
            break
        # 입력 일수 == dayofmonth[month]의 입력월에 해당하는 일수와 같고 윤달이 아니라면
        # 공백을 출력하고 함수 중단(28일이나 30일까지 있는달들 해당)
        if month == 2 and intercalation and day == dayofmonth[month] + 1:
            print('')
            break
        # 만약 월수가 2월이고 윤달이고 일수 == dayofmonth[month]에 넣은 값+1이라면
        # 공백을 출력하고 함수 중단.
        if lineswitch % 7 == 0:
            print('')
        #줄바꿈 부분.
    print('')
    print("",'='*28)



while True:
    drawcalender(input("날짜를 입력하시오(ex20040516) : "))
# While문을 쓰는 이유는 입력 -> 출력 -> 입력이 다시금 되게하기 위해서.
