# Programmers 2018 KAKAO BLIND RECURITMENT - [1차] 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677
# 조건문 간소화 가능. isalpha 사용하기.
# 내장함수 사용한 풀이. 다중집합의 동일성을 이중배열로 for문 사용해서 카운트시키기.
import string
def solution(str1, str2):
    rule1 = list(string.punctuation)
    rule2 = list(string.digits)
    rule3 = (' ','')
    rule1.extend(rule2)
    rule1.extend(rule3)
    print(rule1)
    stack_str1 = []
    stack_str2 = []
    for i in range(len(str1)):
        if str1[i-1:i+1] not in rule1:
            a = str1[i-1:i+1].lower()
            if a[0] in rule1 or a[1] in rule1:
                pass
            else:
                stack_str1.append(a)
    print('stack1 =',stack_str1)

    for i in range(len(str2)):
        if str2[i-1:i+1] not in rule1:
            b = str2[i-1:i+1].lower()
            if b[0] in rule1 or b[1] in rule1:
                pass
            else:
                stack_str2.append(b)
    print('stack2 =',stack_str2)

    intersection = set(stack_str1) & set(stack_str2)
    print('intersection =',intersection)

    union = set(stack_str1) | set(stack_str2)
    print('union =',union)

    inter = [min(stack_str1.count(i), stack_str2.count(i)) for i in intersection]
    print('inter=',inter)
    uni = [max(stack_str1.count(i), stack_str2.count(i)) for i in union]
    print('uni =',uni)
    
    if len(uni):
        return int(sum(inter)/sum(uni) * 65536)
    else:
        return 65536