#보이어, 무어법으로 문자열 검색하기(문자열 길이는 0~255개이다) 실습 예제

def bm_match(txt: str, pat: str) -> int:
    '보이어 무어법으로 문자열 검색'
    skip = [None] * 256         # 문자열 0~255개이므로,그 개수만큼 건너뛰기 표 생성

    #건너뛰기 표만드는 부분
    for pt in range(256):       #pt 0~255까지
        skip[pt] = len(pat)
    for pt in range(len(pat)):  #여기서 pt값이 0~len(pat)까지로 바뀜.
        skip(ord(pat[pt])) = len(pat) - pt - 1 #ord 함수는 문자열을 정수형으로 반환해줌

    #검색 하기 부분

    while pt < len(txt):
        pp = len(pat) -1        # 패턴의 끝부터 검색하기 때문에 len(pat) -1
        while txt[pt] == pat[pp]:   # txt[pt] == pat[pp] 끝부분이 같을때까지 반복
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
            else len(pat) - pp

    return -1

if __name__ == '__main__':
    s1 = input('텍스트를 입력하시오 : ')
    s2 = input('패턴을 입력하시오. : ')

    idx = bm_match(s1,s2)

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다')
    else:
        print(f'{(idx+1)}번째 문자가 일치합니다.')