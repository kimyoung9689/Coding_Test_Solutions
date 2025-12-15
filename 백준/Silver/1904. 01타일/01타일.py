import sys

def solve() -> None:
    """길이 N 2진 수열 개수 (피보나치)"""
    try:
        n: int = int(sys.stdin.readline().strip())
    except Exception:
        return

    if n == 1:
        print(1)
        return

    # D[i]: 길이가 i인 경우의 수
    dp: list[int] = [0] * (n + 1)
    dp[1] = 1  # '1'
    dp[2] = 2  # '00', '11'
    MOD: int = 15746

    # D[i] = D[i-1] + D[i-2]
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

    print(dp[n])

if __name__ == "__main__":
    solve()