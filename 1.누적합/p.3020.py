'''
문제: 개똥벌레
   
URL: https://www.acmicpc.net/problem/3020
'''

import sys
N, H = map(int, sys.stdin.readline().split())

up = [0]* (H+1)
down = [0]* (H+1)

for i in range(N):
    if i % 2 == 0:
        down[int(sys.stdin.readline())] +=1
    else:
        up[int(sys.stdin.readline())] +=1


for i in range(H-1, 0, -1):
    up[i] += up[i+1]
    down[i] += down[i+1]
    
min_value = sys.maxsize
count = 0

for i in range(1, H+1):
    result = down[i] + up[H-i+1]
    if result == min_value:
        result+=1
        continue
    if min_value > result:
        min_value = result
        count = 1
print(result, count)