#x의 길이는 0 <= x < s s보단 작아야함.


s = "[)(]"
stack = []
answer = 0

for i in range(len(s)):
    array_s = list(s[i:]+s[:i])
    print(f'arry_s의{i}번째 배열입니다',array_s)
    while array_s:
        if array_s[0] == '(' or array_s[0] ==  '[' or array_s[0] ==  '{':
            stack.append(array_s[0])
            array_s.pop(0)
        else:
            if len(stack) == 0:
                break
            else:
                stack.append(array_s[0])
                array_s.pop(0)
                if stack[-2] + stack[-1] == '[]' or stack[-2] + stack[-1] == '()' or stack[-2] + stack[-1] == '{}':
                    stack.pop(-1)
                    stack.pop(-1)
                    continue
        print(f'array_s의 {i}번째 루프결과입니다.',array_s)
        print(F'stack의 {i}번째 루프 결과입니다.',stack)
    if len(array_s) == 0 and stack == 0:
        answer +=1
    print('answer = ',answer)
print('정답 : ',answer)