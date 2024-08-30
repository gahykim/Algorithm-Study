'''
문제: 약수의 합
   
URL: https://www.acmicpc.net/problem/17425
'''

from copy import deepcopy
import sys
N = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))
s = deepcopy(H)
result = 0

for i in range(1, N):
    s[i] += s[i-1]

# 오른쪽으로 가는 케이스
for i in range(1, N-1):
    # 첫번째 벌: s[-1]-H[0]-H[i]
    # 두번째 벌: s[-1]-s[i]
    result = max(result, (2 * s[-1])-H[0]-H[i]-s[i])

# 왼쪽에서 부터 가는 케이스
for i in range(1, N-1):
    # 첫번째 벌: s[-1]-H[-1]-H[i]
    # 두번째 벌: s[i-1]
    result = max(result, s[-1]-H[-1]-H[i]+s[i-1])

# 오른쪽, 왼쪽 모두로 부터 가는 케이스
for i in range(1, N-1):
    # 첫번째 벌(오른쪽으로) : s[i]-H[0]
    # 두번째 벌(왼쪽에서부터): s[-1]-s[i-1]-H[-1]
    result = max(result, s[i]-H[0] + s[-1]-s[i-1]-H[-1])
print(result)