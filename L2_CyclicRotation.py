#! /usr/bin/python
# Cyclic Rotation of Array
import sys,os

def solution(A, K):
    length = len(A)
    if length == 0:
        return A
    new = [None] * length
    K = K%length
    for i in range(length):
        index = length - K
        new[i] = A[(index+i)%length]
        #print index+i
    return new

A = [3,8,9,7,6]
N = 3
A = solution(A,N)
print A
