# 암호 만들기

import sys
import itertools

l, c = map(int, sys.stdin.readline().rstrip().split())
word = sorted(sys.stdin.readline().rstrip().split())    # 리스트 정렬

def calc():
    ret = []
    for w in itertools.combinations(word, l):
        vowelCnt, wordCnt = 0, 0
        for c in w:
            if c in 'aeiou':    # 모음일 경우
                vowelCnt += 1
                continue
            wordCnt += 1        # 자음일 경우
        if vowelCnt>0 and wordCnt>1:    # 모음 최소 1개 & 자음 최소 2개 확인
            ret.append("".join(w))
    return ret

for r in calc():
    print(r)