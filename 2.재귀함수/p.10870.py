'''
문제: 피보나치 5
   
URL: https://www.acmicpc.net/problem/10870
'''
import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
arr = [-1] * (n+2)
arr[0] = 0
arr[1] = 1

def fibo(n):
    global arr
    if arr[n] != -1:
        return arr[n]
    arr[n] = fibo(n-1) + fibo(n-2)
    return arr[n]

print(fibo(n))