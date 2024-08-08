'''
문제: 수들의 합 2
   
URL: https://www.acmicpc.net/problem/2003
'''
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 0, 0
result = 0
sum_value = 0

while True:
    if sum_value >= M:
        if sum_value == M:
            result +=1
        sum_value -=numbers[left]
        left+=1
    elif right == N:
        break
    else:
        sum_value +=numbers[right]
        right+=1

print(result)