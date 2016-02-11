#! /usr/bin/python
# Odd Occurences in Array
import sys,os

def solution(A):
    # write your code in Python 2.7
    length = len(A)
    for i in range(length):
        cnt = A.count(A[i])
        if (cnt%2 != 0):
            return A[i]

A = [9,3,9,3,9,7,9]
N = solution(A)
print A
