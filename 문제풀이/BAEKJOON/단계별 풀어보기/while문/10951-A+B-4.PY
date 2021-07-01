# 백준 알고리즘 - while문 10951 A+B - 4 알고리즘
# https://www.acmicpc.net/problem/10951
# 두 정수 A,B를 입력받아 A+B를 출력하는 프로그램을 작성해야함

# 10952 문제와는 다르게 종료조건으로 삼을만한 입력이 없음(0 0 과같은) 
# 그래서 기존 10952와 같이 실행시 EOFError가 뜨는데 (End of file)의 약자로 파일의 끝이 올것을 예상하지 못하여 발생하는 에러이다.
# 이를 처리하기 위해선 try ~ except문을 사용해줘야 한다.
# try문은 뭐가됐던 실행되는 구문이고 try실행중에 오류가 발생시 except 구문이 실행되는 구조이다.


while True:
    try:
        A,B = map(int,input().split())
    except:
        break
    if 0 < A and B < 10:
        print(A+B)