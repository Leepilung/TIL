# 뉴스 클러스터링 풀이용 파일
# https://programmers.co.kr/learn/courses/30/lessons/17677

from typing import Dict

def createFragmentMap(s):
    fragmentMap = {}
    for i in range(len(s)-1):
        fragment = (s[i] + s[i + 1]).lower()
        if fragment.isalpha():
            if fragmentMap.get(fragment):
                fragmentMap[fragment] += 1
            else:
                fragmentMap[fragment] = 1
    return fragmentMap
def calIntersection(str1: Dict, str2: Dict):
    count = 0
    for (key, value) in str1.items():
        if str2.get(key):
            count += min(value, str2.get(key))
    return count
def calUnion(str1: Dict, str2: Dict):
    count = 0
    for key, value in str1.items():
        if str2.get(key):
            count += max(value, str2.get(key))
        else:
            count += value
    for key, value in str2.items():
        if not str1.get(key):
            count += value
    return count
def solution(str1, str2):
    str1Map = createFragmentMap(str1)
    str2Map = createFragmentMap(str2)
    intersection = calIntersection(str1Map, str2Map)
    union = calUnion(str1Map, str2Map)
    ratio = 1 if union == 0 else intersection / union
    return int(ratio * 65536)