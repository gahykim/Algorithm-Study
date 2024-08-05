'''
문제: 구간 합 구하기 4
   
URL: https://www.acmicpc.net/problem/11659
'''
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
numbers = [0]
numbers += list(map(int, input().split()))

# 누적합 (Prefix Sum) 을 사용해야 시간 복잡도를 줄일 수 있다
# 2개의 list를 두지 말고 하나의 numbers list에 누적합을 구현하자

for i, num in enumerate(numbers):
   if i>0:
      numbers[i] = numbers[i-1] + num

for _ in range(m):
    i,j = map(int, input().split())
    print(numbers[j] - numbers[i-1])