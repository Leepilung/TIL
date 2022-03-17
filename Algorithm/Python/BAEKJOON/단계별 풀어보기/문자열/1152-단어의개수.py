# BaekJoon - 문자열 - 1157.단어의 개수
# https://www.acmicpc.net/problem/1152

# 복기할 부분
# 입력의 형태가 The Curious Case of Benjamin Button 와같은 형태이고
# 문자열 앞이나 끝에 공백이 들어가는 경우가 있다.
# 웃긴게 공백기준으로 나눠서 split(" ")으로 하면 통과를 안하고 split()만 해야 통과한다.
# 이유가 뭔지 모르겠네. list형태로 정리해보면 결과값은 똑같은데 이해 불가;

import sys

Text = list(sys.stdin.readline().strip().split())

print(len(Text))