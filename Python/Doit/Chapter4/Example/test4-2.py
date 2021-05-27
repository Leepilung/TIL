#고정 길이 스택 Fixed Stack 사용한 실습 예제 짜보면서 해석, 공부 모자란 부분 정리하기

from enum import Enum
from fixed_stack import FixedStack

Menu = Enum('Menu',['푸시','팝','피크','검색','덤프','종료'])       # 'Menu'와 옆의 리스트 부분을 딕셔너리 모습으로 출력(Enum에 의해) Enum 공부 더할 필요성 있음.

def select_menu() -> Menu:
    '메뉴 선택'
    s = [f'({m.value}){m.name}'for m in Menu]
    while True:
        print(*s, sep = '    ', end ='')                        # sep => print문에서 사용되는 함수. sep 관련 내용 정리 및 공부
        n = int(input(': '))
        if 1 <= n <= len(Menu):              # Menu의 개수 이하로 입력할 시
            return Menu(n)

s = FixedStack(64)                  # 최대 64개의 푸시를 할 수있는 스택이라는 의미

while True:
    print(f'현재 데이터 개수 : {len(s)} / {s.capacity}')
    menu = select_menu()        # 메뉴 선택

    if menu == Menu.푸시:       # 푸시 선택시
        x = int(input('데이터를 입력하시오 . : '))
        try:                   # try 문법 정리 및 공부 
            s.push(x)  
        except FixedStack.Full:
            print('스택이 가득 차 있습니다.')
    
    elif menu == Menu.팝:       # 팝 선택
        try:
            x = s.pop()
            print(f'팝한 데이터는 {x} 입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')
    
    elif menu == Menu.피크:     # 피크 선택
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x} 입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')
        
    elif menu == Menu.검색:     # 검색 선택
        x = int(input('검색할 값을 입력하세요. : '))
        if x in s:
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
        else:
            print('검색할 수 없습니다.')
    
    elif menu == Menu.덤프:     # 덤프 선택
        s.dump()

    else: 
        break
    