##### 순열 (Permutation)
# 서로 다른 n개의 데이터 중에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우의 수
from itertools import permutations

data = ['A', 'B', 'C']
ret = list(permutations(data, 2))
print(ret)  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
print(len(ret))     # 모든 경우의 수: 6


##### 조합 (Combination)
# 서로 다른 n개의 데이터 중에서 순서를 고려하지 않고 r개의 데이터를 뽑아 나열하는 모든 경우의 수
from itertools import combinations

data = ['A', 'B', 'C']
ret = list(combinations(data, 2))
print(ret)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(len(ret))     # 모든 경우의 수: 3


##### 중복순열 (Permutation with repetition)
# 중복 가능한 n개의 데이터 중에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우의 수
from itertools import product

data = ['A', 'B', 'C']
ret = list(product(data, repeat=2))
print(ret)  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
print(len(ret))     # 모든 경우의 수: 9


##### 중복조합 (Combination with repetition)
# 중복 가능한 n개의 데이터 중에서 순서를 생각하지 않고 r개의 데이터를 뽑아 나열하는 모든 경우의 수
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
ret = list(combinations_with_replacement(data, 2))
print(ret)  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
print(len(ret))     # 모든 경우의 수: 6