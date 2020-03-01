#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
totalNumSwaps = 0
for i in range(n):
    numSwaps = 0
    for j in range(n-1):
        if(a[j] > a[j+1]):
            t = a[j]
            a[j] = a[j+1]
            a[j+1]= t
            numSwaps += 1
    totalNumSwaps += numSwaps

    if numSwaps == 0:
     break

print('Array is sorted in ' + str(totalNumSwaps) + ' swaps.')
print('First Element: ' + str(a[0]))
print('Last Element: ' + str(a[n-1]))
