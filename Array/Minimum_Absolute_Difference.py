"""
Question:
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
"""
from typing import List

'''
Ans: 

1. Sort array
2. Iterate through the array and find minimum difference between adjacent integers(In sorted array 
minimum occurs only between adjacent integers).
3. Iterate again ,if two adjacent integers difference is equals to 
minimum difference then add them to list(list).(Since difference occurs between adjacent integers, result list will 
also contains adjacent integers of sorted array)'''


def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    diff = float('inf')
    arr.sort()
    for i in range(1, len(arr)):
        diff = min(arr[i] - arr[i - 1], diff)

    res = []
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] == diff:
            res.append([arr[i - 1], arr[i]])
    return res


print(minimumAbsDifference([1, 2, 3]))
