#보석 돌 풀이+실험용 시트

jewels = 'aA'
stone = 'aAAbbbbb'
sepjewels = list(jewels)
print(sepjewels)
# -> a와 A가 남음.
for j in stone:
#인덱스로 표시하기때문에     
#결과값 print(j)하면a, A, A, b,b,b,b,b로 나옴
#위 부분은 함수에서 바꾸면 j for j in stone 이 꼴로 변환 가능.
#그렇다면 저 반복문 sepjewels in j 꼴 쓰려면?
#이중 for문은 시간복잡도가 커져서 사용 X.
#결과값 예상대로 나옴 (for j in stone = ㅁ,)

j in sepjewels for j in stone #가능한가? -> 확인 불가능

#변수 하나를 초기값 0으로 설정.
#a A A b b b b b가 sepjewels에 있을경우 아무 변수 1씩 증가시키고

