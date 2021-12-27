##### .sort()
# 원본 데이터를 변경해 정렬
data = ['bcd', 'abc', 'abb']
data.sort()
print(data) # ['abb', 'abc', 'bcd']


##### sorted(data)
# 원본 데이터를 변경하지 않고 정렬한 후 새로운 데이터 리턴
data = ['bcd', 'abc', 'abb']
new_data = sorted(data)
print(data) # ['bcd', 'abc', 'abb']
print(new_data) # ['abb', 'abc', 'bcd']


# 1. 데이터 문자열의 길이를 기준으로 정렬할 경우
data = ['bcd', 'abc', 'bcdefg', 'bcddfg', 'zbcd','za']
print(sorted(data, key=len))    # ['za', 'bcd', 'abc', 'zbcd', 'bcdefg', 'bcddfg']
print(sorted(data, key=lambda x: -len(x)))  # ['bcdefg', 'bcddfg', 'zbcd', 'bcd', 'abc', 'za']


# 2. 데이터 문자열의 각 원소를 기준으로 정렬할 경우
data = ['bcd', 'abc', 'bcdefg', 'bcddfg', 'zbcd','za']
print(sorted(data, key=lambda x:(x[1], x[0]), reverse=True))  # ['za', 'abc', 'zbcd', 'bcd', 'bcdefg', 'bcddfg']


# 3. 문자열 자체를 정렬할 경우 (anagram 찾을 때)
s = 'abazc'
new_s = sorted(s)   # ['a', 'a', 'b', 'c', 'z']
print(''.join(new_s))   # 'aabcz'


# 4. max & min
data = ['bcd', 'abc', 'bcdefg', 'bcddfg', 'zbcd','za']
print(max(data, key=len))   # 'bcdefg'
print(max(data, key=lambda x:x[1])) # 'bcd'