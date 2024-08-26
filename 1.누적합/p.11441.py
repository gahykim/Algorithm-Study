'''
문제: 합 구하기
   
URL: https://www.acmicpc.net/problem/11441
'''
import sys

N = int(sys.stdin.readline())
A = [0]
A = A + list(map(int, sys.stdin.readline().split()))
    
M = int(sys.stdin.readline())
arr = []
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    arr.append((i, j))

for i in range(1, N+1):
    A[i] = A[i-1]+A[i]

for (x,y) in arr:
    print(A[y] - A[x-1])