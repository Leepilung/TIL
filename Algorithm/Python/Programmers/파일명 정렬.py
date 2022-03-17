# Programmers -  파일명 정렬
# https://programmers.co.kr/learn/courses/30/lessons/17686
# 파일명은 우선 HEAD 부분을 기준으로 사전 순으로 정렬한다. 문자열 비교 시 대소문자 구분을 하지 않는다.
# 파일명의 HEAD 부분이 대소문자 차이 외에는 같을 경우, NUMBER의 숫자 순으로 정렬한다. 
# 9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬된다. 숫자 앞의 0은 무시되며, 012와 12는 정렬 시에 같은 같은 값으로 처리된다.
# 두 파일의 HEAD 부분과, NUMBER의 숫자도 같을 경우, 원래 입력에 주어진 순서를 유지한다.
#  MUZI01.zip과 muzi1.png가 입력으로 들어오면, 정렬 후에도 입력 시 주어진 두 파일의 순서가 바뀌어서는 안 된다.
#입력: ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
#출력: ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# 대충 file명에서 head, number, tail 3부분으로 나눠야할듯.
# 우선 파일명 for문으로 돌리고 숫자부분을 제외한 head부분 처리. 대문자던 소문자던상관업으니까 소문자로 통일.
# 숫자 판별은 string 모듈 사용.(N진수 게임 -> 10진수 n진수 변환할때도 사용)
# 이중 for문써야할듯. 리스트안에서 또 한번 인덱스값 받아서 파일명에 숫자 포함되있는지 아닌지 확인. 
# 그다음 number 부분. number 변수 설정 ''. head때랑 같이 판별. 범위는 head랑 다르게 filename으로
# number = '' 변수를 전역설정으로 해두니까 for문으로 반복할수록 기존값이 가산됨. for문 안에다가 돌때마다 초기화시켜야할듯
# 파일명에서 number, head 빼면 남은건 tail로 저장.
# 정렬 조건 -> 헤드 1 number 2 같은 이름일 경우 인덱스가 3 순으로 정렬되야함.
# sort key lambda 사용. 이거찾는데 시간 다쓴듯. 정리 및 복습한번 더하기.
# 정렬된걸 이제 원본의 형태로 넣어야함. 인덱스 활용하기.
# answer 배열은 이미 사용했으므로 trueanswer = [] 만듦

import string
def solution(files):
    answer = []
    trueanswer = []
    index = 0

    for i in files:
        filename = i.lower()
        head = ''
        for j in range(len(i)):
            if filename[j] in string.digits:
                filename = filename[j:]
                break
            else:
                head += filename[j]

        number = ''
        for i in range(len(filename)):
            if filename[i] not in string.digits:
                filename = filename[i:]

                break
            else:
                number += filename[i]
        tail = filename
        answer.append([index,head,number,tail])
        index += 1

    answer.sort(key=lambda x: (x[1], int(x[2]), x[0]))

    for i in answer:
        trueanswer.append(files[i[0]])
        
    return trueanswer