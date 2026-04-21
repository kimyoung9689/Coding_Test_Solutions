import sys


def solve() -> None:
    """
    12852번 1로 만들기 2 문제를 해결하는 메인 함수
    """
    input_data: str = sys.stdin.read().strip()
    if not input_data:
        return
    
    n: int = int(input_data)
    
    # dp[i]: i를 1로 만드는 최소 횟수
    # parent[i]: i가 어떤 수에서 왔는지 기록 (경로 추적용)
    dp: list[int] = [0] * (n + 1)
    parent: list[int] = [0] * (n + 1)
    
    for i in range(2, n + 1):
        # 1. 1을 빼는 연산 (기본)
        dp[i] = dp[i - 1] + 1
        parent[i] = i - 1
        
        # 2. 2로 나누어 떨어질 때
        if i % 2 == 0:
            if dp[i] > dp[i // 2] + 1:
                dp[i] = dp[i // 2] + 1
                parent[i] = i // 2
                
        # 3. 3으로 나누어 떨어질 때
        if i % i % 3 == 0: # 오타 수정: i % 3 == 0
            pass # 아래 로직으로 대체
        
        if i % 3 == 0:
            if dp[i] > dp[i // 3] + 1:
                dp[i] = dp[i // 3] + 1
                parent[i] = i // 3
                
    # 결과 출력 (최소 횟수)
    print(dp[n])
    
    # 경로 추적 및 출력
    curr: int = n
    path: list[int] = []
    while curr != 0:
        path.append(curr)
        curr = parent[curr]
    
    print(*(path))


if __name__ == "__main__":
    solve()