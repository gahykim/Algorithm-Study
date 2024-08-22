'''
문제: 두 배열의 합
   
URL: https://www.acmicpc.net/problem/2143
'''
import bisect
import sys
T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

an, bn = [], []
for i in range(n):
    for j in range(i+1, n+1):
        an.append(sum(A[i:j]))
for i in range(m):
    for j in range(i+1, m+1):
        bn.append(sum(B[i:j]))

an.sort()
bn.sort()

result = 0
for i in range(len(an)):
    bmp = T - an[i]
    left = bisect.bisect_left(bn, bmp) # bn 리스트 내에 bmp 값이 존재하는지 확인
    right = bisect.bisect_right(bn, bmp)
    result+=(right - left)
print(result)