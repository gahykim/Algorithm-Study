'''
문제: 부분합
   
URL: https://www.acmicpc.net/problem/1806
'''

# import sys
# input = sys.stdin.readline
# n,S = map(int, input().split())
# numbers = [0]
# numbers += list(map(int, input().split()))
n, S = 10, 15
numbers = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]

result = 1000
for i in range(n): 
    tmp = [numbers[i]]
    for j in range(i, n):
        tmp.append(tmp[j-1] + numbers[j])
        if tmp[j] >= S:
            if len(tmp) - 1 < result:
                result = len(tmp) - 1
                break
                
print(result)