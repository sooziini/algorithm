# k진수에서 소수 개수 구하기 (2022 KAKAO BLIND RECRUITMENT)

def decimal_to_base(n, base):
    ret=''
    while n>0:
        n,mod=divmod(n, base)
        ret+=str(mod)
    return ret[::-1]

def is_prime_number(n):
    if n<2:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def solution(n, k):
    answer=0
    candidate=decimal_to_base(n, k).replace('0',' ').split()
    for c in candidate:
        if is_prime_number(int(c)):
            answer+=1
    return answer

print(solution(437674, 3))
print(solution(110011, 10))