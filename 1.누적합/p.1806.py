'''
문제: 부분합
   
URL: https://www.acmicpc.net/problem/1806
'''

# 기본 탐색 방법으로는 시간초과가 일어난다
# 따라서 투포인터를 사용해서 풀이해야 한다.

import sys
input = sys.stdin.readline
n,S = map(int, input().split())
numbers = list(map(int, input().split()))

left, right = 0,0
sum_value = 0
min_length = sys.maxsize

while True:
    # 만약 총 합이 S가 넘는다면, left를 하나씩 옮겨보면서 어디까지 길이가 줄어드나 확인
    if sum_value >=S:
        min_length = min(min_length, right - left)
        sum_value-=numbers[left]
        left+=1
    elif right == n:
        break
    # 만약 총합이 S를 넘지 않는다면 right을 오른쪽으로 한칸씩 옮기며 총합이 S를 넘을 때 까지 더함
    else:
        sum_value +=numbers[right]
        right+=1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)