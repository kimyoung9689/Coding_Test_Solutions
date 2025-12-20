import sys


def solve_stairs() -> None:
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n: int = int(input_data[0])
    stairs: list[int] = [0] * 301  # 최대 계단 수 300개
    for i in range(1, n + 1):
        stairs[i] = int(input_data[i])

    # dp 테이블 초기화
    dp: list[int] = [0] * 301

    # 초기값 설정
    dp[1] = stairs[1]
    if n >= 2:
        dp[2] = stairs[1] + stairs[2]
    if n >= 3:
        # 3번째 계단까지의 최댓값 계산
        dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

    # 점화식 계산
    for i in range(4, n + 1):
        # (i-3 -> i-1 -> i) 경로와 (i-2 -> i) 경로 중 최댓값 선택
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

    print(dp[n])


if __name__ == "__main__":
    solve_stairs()