n = int(input())

money = [500, 100, 50, 10]  # 거스름돈 동전 리스트
ret = 0                     # 거슬러 줘야 할 동전의 최소 개수

for i in money:
    ret += (n // i)
    n %= i

print(ret)