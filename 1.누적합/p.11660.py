'''
문제: 구간 합 구하기 5
   
URL: https://www.acmicpc.net/problem/11660
'''
import sys
input = sys.stdin.readlines

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

# 그대로 구현하면 시간초과 문제가 발생 --> 누적합 dp 계산 (보텀업)을 사용해야 함

# dp 테이블 계산 
# 기준 포인트에서 +서쪽 +북쪽 - 대각선  + matrix 값
dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + matrix[i-1][j-1]

# 역으로 맨마지막 값 - 서쪽 - 북쪽 + 대각선 
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)