'''
문제: 슈퍼 마리오
   
URL: https://www.acmicpc.net/problem/2851
'''

import sys
mushroom = []
for _ in range(10):
    mushroom.append(int(sys.stdin.readline()))

result = 0
for i in range(len(mushroom)):
    result+=mushroom[i]
    if result >=100:
        if result - 100 > 100 - (result-mushroom[i]):
            result-=mushroom[i]
            break
print(result)