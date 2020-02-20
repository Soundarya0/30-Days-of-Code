#!/bin/python3
import sys

def _get_hourglass_sum(matrix, row, col):

    sum = 0
    sum += matrix[row-1][col-1]
    sum += matrix[row-1][col]
    sum += matrix[row-1][col+1]
    sum += matrix[row][col]
    sum += matrix[row+1][col-1]
    sum += matrix[row+1][col]
    sum += matrix[row+1][col+1]
    return sum

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

max_hourglass_sum = -63
for i in range(1,5):
    for j in range(1,5):
        current_hourglass_sum = _get_hourglass_sum(arr, i, j)
        if current_hourglass_sum > max_hourglass_sum:
            max_hourglass_sum = current_hourglass_sum
print(max_hourglass_sum)
