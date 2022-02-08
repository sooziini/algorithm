# 일곱 난쟁이 - BinarySearch

import sys

data=sorted([int(sys.stdin.readline().rstrip()) for _ in range(9)])

data_sum=sum(data)
left,right=0,8
while left<right:
    total=data_sum-(data[left]+data[right])
    if total==100:
        for i in range(9):
            if i!=left and i!=right:
                print(data[i])
        break
    elif total>100:
        left+=1
    else:
        right-=1