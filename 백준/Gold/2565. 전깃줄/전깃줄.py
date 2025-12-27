import sys
from typing import List


def solve() -> None:
    """
    전깃줄 교차 문제를 LIS 알고리즘으로 해결한다.
    """
    # 입력 처리
    try:
        line_count_str = sys.stdin.readline().strip()
        if not line_count_str:
            return
        n: int = int(line_count_str)
    except ValueError:
        return

    lines: List[List[int]] = []
    for _ in range(n):
        lines.append(list(map(int, sys.stdin.readline().split())))

    # A 전봇대 기준으로 정렬
    lines.sort(key=lambda x: x[0])

    # B 전봇대 위치들만 추출
    b_targets: List[int] = [line[1] for line in lines]

    # LIS(가장 긴 증가하는 부분 수열) 계산을 위한 DP 테이블
    dp: List[int] = [1] * n

    for i in range(n):
        for j in range(i):
            if b_targets[j] < b_targets[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # 전체 개수 - 최대 설치 가능 개수 = 최소 삭제 개수
    print(n - max(dp))


if __name__ == "__main__":
    solve()