# 실패율 (2019 KAKAO BLIND RECRUITMENT)

# count 함수 사용
def solution(N, stages):
    stage_len = len(stages)
    stage_dict = {i:0 for i in range(1, N+1)}
    for s in range(1, N+1):
        cnt = stages.count(s)
        stage_dict[s]=cnt/stage_len
        stage_len-=cnt
        if stage_len==0:    # stages 배열 전체를 순회했을 경우
            break
    stage_tuple = sorted(stage_dict.items(), key=lambda x:-x[1])    # 실패율 내림차순 정렬
    return [s for s, _ in stage_tuple]

def solution2(N, stages):
    stages.sort()
    stage_len = len(stages)
    stage_dict = {i:0 for i in range(1, N+1)}
    cnt = 1
    for i in range(1, len(stages)):
        if stages[i-1]!=stages[i]:
            stage_dict[stages[i-1]]=cnt/stage_len
            stage_len-=cnt
            cnt = 0
        if stages[i]==N+1:
            break
        if i==len(stages)-1:    # 마지막 stage
            stage_dict[stages[i]]=(cnt+1)/stage_len
        cnt+=1
    stage_tuple = sorted(stage_dict.items(), key=lambda x:-x[1])    # 실패율 내림차순 정렬
    return [s for s, _ in stage_tuple]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))