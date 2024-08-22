'''
문제: 나머지 합
   
URL: https://www.acmicpc.net/problem/10986
'''

import sys
N,M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

# 나머지의 수가 같은 누적합의 조합을 통해 나머지가 0이 되는 부분합의 경우의 수를 구할 수 있음

sum_value = 0
remainder = [0] * M
for i in range(N):
    sum_value +=numbers[i]
    remainder[sum_value % M] +=1

result = remainder[0]
for i in remainder:
    result += i*(i-1) // 2
print(result)
