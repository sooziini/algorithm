
# 이진 탐색
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return None

# 이진 탐색 - 재귀
def binary_search_recursion(arr, target, left, right):
    if left>right:
        return None
    mid=(left+right)//2
    if arr[mid]==target:
        return mid
    elif arr[mid]<target:
        left=mid+1
    else:
        right=mid-1
    return binary_search_recursion(arr, target, left, right)

# Lower Bound
def binary_search_lower(arr, target):
    left, right = 0, len(arr)-1
    if arr[-1]<target:
        return len(arr)
    while left<right:
        mid = (left+right)//2
        if arr[mid]>=target:
            right=mid
        elif arr[mid]<target:
            left=mid+1
    return right

# Upper Bound
def binary_search_upper(arr, target):
    left, right = 0, len(arr)-1
    if arr[-1]<=target:
        return len(arr)
    while left<right:
        mid = (left+right)//2
        if arr[mid]>target:
            right=mid
        elif arr[mid]<=target:
            left=mid+1
    return right


data=[50, 80, 150, 150, 150, 150, 210, 260]

from bisect import bisect_left, bisect_right

print(binary_search_lower(data, 255))   # 7
print(bisect_left(data, 255))   # 7
print(binary_search_upper(data, 260))   # 8
print(bisect_right(data, 260))  # 8
print(binary_search(data, 210)) # 6
print(binary_search_recursion(data, 200, 0, len(data)-1))   # None