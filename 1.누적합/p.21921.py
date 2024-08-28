'''
문제: 블로그
   
URL: https://www.acmicpc.net/problem/21921
'''
import sys
X, N = map(int, sys.stdin.readline().split())
ppl = list(map(int, sys.stdin.readline().split()))

max_visitor = 0
count = 0

for i in range(X-N+1):
    if i == 0:
        visitor = sum(ppl[:N])
    else:
        visitor = visitor - ppl[i-1] + ppl[i+N-1]
    if visitor > max_visitor:
        max_visitor = visitor
        count = 1
    elif visitor == max_visitor:
        count +=1

if max_visitor == 0:
    print("SAD")
else:
    print(max_visitor)
    print(count)