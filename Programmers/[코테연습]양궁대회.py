# 양궁대회 (2022 KAKAO BLIND RECRUITMENT)

from copy import deepcopy

max_diff,max_lion=0,[]

def calc_score(info, lion):
    a,l=0,0
    for i in range(11):
        if info[i]==0 and lion[i]==0:
            continue
        if info[i]>=lion[i]:
            a+=10-i
        else:
            l+=10-i
    return l-a if a<l else -1

def dfs(idx, n, info, lion):
    global max_diff,max_lion
    if sum(lion)>n:
        return
    if idx>10:
        diff=calc_score(info, lion)
        if diff>=max_diff:
            lion[10]=n-sum(lion)
            max_diff,max_lion=diff,lion
        return
    lion[idx]=info[idx]+1
    dfs(idx+1, n, info, deepcopy(lion))
    lion[idx]=0
    dfs(idx+1, n, info, deepcopy(lion))

def solution(n, info):
    dfs(0, n, info, [0]*11)
    return max_lion if max_lion else [-1]

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))