import sys


def solve() -> None:
    # 입력 받기
    line = sys.stdin.readline()
    if not line:
        return
    n: int = int(line.strip())

    # dp 테이블 초기화 (0부터 n까지)
    # dp[i]는 숫자 i를 1로 만드는 최소 횟수
    dp: list[int] = [0] * (n + 1)

    for i in range(2, n + 1):
        # 1. 현재 숫자에서 1을 빼는 경우 (기본값)
        dp[i] = dp[i - 1] + 1

        # 2. 현재 숫자가 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

        # 3. 현재 숫자가 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    # 결과 출력
    print(dp[n])


if __name__ == "__main__":
    solve()