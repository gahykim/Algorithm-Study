'''
문제: 수열
   
URL: https://www.acmicpc.net/problem/2559
'''
import sys

N, K = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

sum_value = sum(numbers[:K])
result = sum_value

for i in range(N-K): 
    new_sum_value = sum_value - numbers[i] + numbers[i+K]
    if new_sum_value > result:
        result = new_sum_value
    sum_value = new_sum_value
print(result)