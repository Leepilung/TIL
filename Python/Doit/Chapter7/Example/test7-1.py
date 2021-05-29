#브루트 포스법으로 문자열 검색하기 실습 예제
#검색되는 쪽의 문자열이 텍스트(text), 찾아내는 문자열을 패턴(pat)이라고 정의한다.

def bf_match(txt: str, pat: str) -> int:
    '브루트 포스법으로 문자열 검색'
    pt = 0                  # 텍스트(txt)를 따라가는 커서            
    pp = 0                  # 패턴(pat)을 따라가는 커서

    while pt != len(txt) and pp != len(pat):        #각각의 커서를 의미하는 pt와 pp가 각 문자열의 길이와 같지 않을동안 반복
        if txt[pt] == pat[pp]:                      #txt[pt]가 pat[pp]와 같을 때
            pt += 1
            pp += 1
        else:                                       # txt[pt] != pat[pp] 일 경우
            pt = pt - pp + 1                        # PT - PP +1 한값 출력
            pp = 0                                  # PP는 0으로 만듦

    return pt - pp if pp == len(pat) else -1        # 개인적으로 판단하기에 
    #if pp == len(pat):
    #   return pt - pp
    #else:  -1                                      과 같다고 판단됨.

if __name__ == '__main__':
    s1 = input('텍스트를 입력하시오. : ')              # 텍스트용 문자열
    s2 = input('패턴을 입력하시오. : ')                # 패턴용 문자열

    idx =bf_match(s1,s2)                             #문자열 s1, s2를 브루트 포스법으로 검색

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx+1)}번째 문자가 일치합니다.')
