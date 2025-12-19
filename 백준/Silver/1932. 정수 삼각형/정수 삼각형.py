import sys


def solve() -> None:
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n: int = int(input_data[0])
    
    # 삼각형 데이터 구성
    triangle: list[list[int]] = []
    idx: int = 1
    for i in range(1, n + 1):
        triangle.append(list(map(int, input_data[idx : idx + i])))
        idx += i

    # DP 테이블 초기화 (삼각형과 동일한 구조)
    dp: list[list[int]] = [[0] * len(row) for row in triangle]
    dp[0][0] = triangle[0][0]

    # 아래층으로 내려가며 최댓값 계산
    for i in range(n - 1):
        for j in range(len(triangle[i])):
            # 왼쪽 대각선 아래 업데이트
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + triangle[i + 1][j])
            # 오른쪽 대각선 아래 업데이트
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + triangle[i + 1][j + 1])

    # 맨 마지막 줄에서 가장 큰 값 출력
    print(max(dp[n - 1]))


if __name__ == "__main__":
    solve()