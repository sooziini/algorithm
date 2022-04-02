# 최소 스패닝 트리 - MST

import sys
input=sys.stdin.readline

V,E=map(int, input().split())
edges=[]
for _ in range(E):
    a,b,cost=map(int, input().split())
    edges.append((cost, a, b))

parent=[0]*(V+1)
for i in range(1, V+1):
    parent[i]=i

def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a=find_parent(parent, a)
    b=find_parent(parent, b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

ans=0
for cost, a, b in sorted(edges):
    if find_parent(parent, a)!=find_parent(parent, b):
        union_parent(parent, a, b)
        ans+=cost
print(ans)