import sys


def solve() -> None:
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n: int = int(input_data[0])
    wine: list[int] = [0] * (n + 1)
    for i in range(1, n + 1):
        wine[i] = int(input_data[i])

    # DP 테이블 초기화
    dp: list[int] = [0] * (n + 1)

    # 기본값 설정
    dp[1] = wine[1]
    if n >= 2:
        dp[2] = wine[1] + wine[2]

    # 점화식 계산 (n이 3 이상일 때부터)
    for i in range(3, n + 1):
        dp[i] = max(
            dp[i - 1],                # i번째 안 마심
            dp[i - 2] + wine[i],      # i번째가 연속 1잔째
            dp[i - 3] + wine[i - 1] + wine[i]  # i번째가 연속 2잔째
        )

    print(dp[n])


if __name__ == "__main__":
    solve()