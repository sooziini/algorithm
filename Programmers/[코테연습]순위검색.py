# 순위검색 (2021 KAKAO BLIND RECRUITMENT)

# 정확성O / 효율성O
# bisect_left + 딕셔너리 사용
from bisect import bisect_left
from itertools import combinations

def solution(info, query):
    answer=[]
    info_dict={}        # {info의 가능한 조합:[score 값을 담을 배열]}
    for i in info:
        _i = i.split()
        _info_keys=_i[:-1]    # info의 score 제외 부분
        _info_val=_i[-1]      # info의 score 부분
        for j in range(5):
            for c in combinations(_info_keys, j):
                _c = ''.join(c)
                if _c in info_dict:     # key 값이 딕셔너리에 있다면 values 배열에 score 값 append
                    info_dict[_c].append(int(_info_val))
                else:       # key 값이 딕셔너리에 없다면 values 배열에 score 값을 담을 배열 추가
                    info_dict[_c] = [int(_info_val)]
    for d in info_dict:     
        info_dict[d].sort()     # 딕셔너리의 값에 해당하는 배열 오름차순 정렬
    for q in query:
        _q = q.replace("and",'').replace("-",'').split()
        _query, _query_score = ''.join(_q[:-1]), int(_q[-1])
        if _query in info_dict:     # query가 딕셔너리에 있을 경우
            scores = info_dict[_query]
            if scores:
                idx = bisect_left(scores, _query_score)  # lower bound 이진탐색
                answer.append(len(scores)-idx)
        else:
            answer.append(0)
    return answer

def bs_lower_bound(arr, target):
    left, right = 0, len(arr)-1
    if arr[-1]<target:
        return len(arr)
    while left<right:
        mid = (left+right)//2
        if target<=arr[mid]:
            right=mid
        elif arr[mid]<target:
            left=mid+1
    return right

# 정확성O / 효율성X
# binary search 사용
def solution2(info, query):
    answer=[]
    _info=sorted([i.split() for i in info], key=lambda x:int(x[-1]))
    _info_bs=[int(i[-1]) for i in _info]
    for q in query:
        cnt=0
        _q = q.replace("and",'').replace('-','').split()
        _query, _query_score = _q[:-1], int(_q[-1])
        bs_idx=bs_lower_bound(_info_bs, _query_score)
        if bs_idx<len(_info_bs):
            for _i in _info[bs_idx:]:
                if len([i for i in _i[:4] if i in _query])==len(_query):
                    cnt+=1            
        answer.append(cnt)
    return answer

# 정확성O / 효율성X
def solution3(info, query):
    answer=[]
    _info=sorted([i.split() for i in info], key=lambda x:int(x[-1]))
    for q in query:
        cnt=0
        _q = q.replace("and",'').replace('-','').split()
        _query, _query_score = _q[:-1], int(_q[-1])
        # query_set = set(_query)
        for _i in _info:
            # if len(set(_i[:4])&query_set)==len(query_set) and _query_score<=_i[4]:
            if len([i for i in _i[:4] if i in _query])==len(_query) and _query_score<=int(_i[4]):
                cnt+=1
        answer.append(cnt)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))