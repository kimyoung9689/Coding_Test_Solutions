import sys
from typing import List


def solve() -> None:
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n: int = int(input_data[0])
    # 각 집의 [R, G, B] 비용 리스트 생성
    costs: List[List[int]] = []
    for i in range(n):
        idx = 1 + i * 3
        costs.append([
            int(input_data[idx]),
            int(input_data[idx + 1]),
            int(input_data[idx + 2])
        ])

    # DP 테이블 초기화 (비용 리스트를 그대로 사용)
    dp: List[List[int]] = costs

    # 2번째 집(인덱스 1)부터 마지막 집까지 계산
    for i in range(1, n):
        # 현재 집을 빨강으로 칠할 때: 이전 집의 초록/파랑 중 최솟값 더함
        dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
        # 현재 집을 초록으로 칠할 때: 이전 집의 빨강/파랑 중 최솟값 더함
        dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
        # 현재 집을 파랑으로 칠할 때: 이전 집의 빨강/초록 중 최솟값 더함
        dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])

    # 마지막 집까지 계산된 비용 중 가장 작은 값 출력
    print(min(dp[n - 1]))


if __name__ == "__main__":
    solve()