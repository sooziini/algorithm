# 뉴스 클러스터링 (2018 KAKAO BLIND RECRUITMENT)

# 다중 집합의 교집합을 리턴하는 함수
def intersection(list1, list2):
    tmp=[]
    tmp_list2=list2[:]
    for i in list1:
        if i in tmp_list2:
            tmp.append(i)
            tmp_list2.remove(i)
    return tmp

# 다중 집합의 합집합을 리턴하는 함수
def union(list1, list2, intersection_list):
    tmp=list1+list2
    for i in intersection_list:
        tmp.remove(i)
    return tmp

def solution(str1, str2):
    str1_list=[str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2_list=[str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not (str1_list or str2_list):
        return int(1*65536)
    intersection_list=intersection(str1_list, str2_list)
    union_list=union(str1_list, str2_list, intersection_list)
    return int(len(intersection_list)/len(union_list)*65536)

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))