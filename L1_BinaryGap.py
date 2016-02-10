#! /usr/bin/python
# Find the Largest Binary Gap
import sys,os

def solution(N):
	input = str(bin(N)).strip("0b");
	length = len(input)
	current = 0
	max = 0
	
	for index in range(length):
		if input[index]=="0":
			current = current + 1
		if input[index]=="1":
			if current > max:
				max = current
			current = 0
	return max	

N = int(sys.argv[1])
print N
bingap = solution(N)
print bingap
