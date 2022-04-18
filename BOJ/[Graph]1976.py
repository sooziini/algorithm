# 여행 가자 - Graph (Union-Find)

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

parent = [0]*(N+1)
for i in range(1, N+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def play(parent, a, b):
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

for i in range(1, N+1):
    cities = [0] + list(map(int, input().split()))
    for j in range(1, N+1):
        if cities[j] == 1:
            play(parent, i, j)

plan = list(map(int, input().split()))
for i in range(0, len(plan)-1):
    if parent[plan[i]] != parent[plan[i+1]]:
        print("NO")
        break
else:
    print("YES")