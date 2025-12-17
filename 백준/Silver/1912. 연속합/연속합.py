import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.read

def solve():
    # 모든 입력을 한 번에 읽음 (n과 수열)
    data = input().split()
    if not data:
        return
    
    # 첫 번째 데이터는 n (수열의 길이)
    n = int(data[0])
    
    # 나머지 데이터는 수열 A
    A = [int(x) for x in data[1:]]
    
    # n이 0이면 종료
    if n == 0:
        print(0)
        return

    # DP 테이블 초기화. DP[i]는 A[i]를 반드시 포함하는 최대 연속합
    # 배열 인덱스를 0부터 시작한다고 가정
    # A[0]를 반드시 포함하는 최대 연속합은 A[0] 자신
    dp = [0] * n
    dp[0] = A[0]
    
    # 전체 수열의 최대 연속합을 저장하는 변수.
    # 초기값은 첫 번째 원소를 포함하는 최대 연속합
    max_so_far = dp[0]
    
    # 1부터 n-1까지 반복
    for i in range(1, n):
        # 점화식: A[i]부터 새로 시작하는 합 vs 이전 연속합에 A[i]를 더한 합
        # DP[i] = max(A[i], dp[i-1] + A[i])
        dp[i] = max(A[i], dp[i-1] + A[i])
        
        # 전체 최대 연속합 갱신
        max_so_far = max(max_so_far, dp[i])
        
    print(max_so_far)

solve()