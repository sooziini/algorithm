# 신고 결과 받기 (2022 KAKAO BLIND RECRUITMENT)

def solution(id_list, report, k):
    answer=[0]*len(id_list)
    report_dict={id:set() for id in id_list}
    for r in set(report):
        i,j=r.split()
        report_dict[j].add(i)

    for _, value in report_dict.items():
        if len(value)>=k:
            for v in value:
                answer[id_list.index(v)]+=1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))