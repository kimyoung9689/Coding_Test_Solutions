import sys


def solve_lcs() -> None:
    """
    LCS 길이를 계산하여 출력한다.
    """
    # 입력 처리
    str1: str = sys.stdin.readline().strip()
    str2: str = sys.stdin.readline().strip()

    n: int = len(str1)
    m: int = len(str2)

    # DP 테이블 초기화 (0으로 채움)
    dp: list[list[int]] = [[0] * (m + 1) for _ in range(n + 1)]

    # DP 진행
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                # 문자가 같으면 대각선 위 + 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 문자가 다르면 위나 왼쪽 중 큰 값
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # 최종 결과 출력
    print(dp[n][m])


if __name__ == "__main__":
    solve_lcs()