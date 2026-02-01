import sys
from typing import List


def solve() -> None:
    # 입력 최적화 및 데이터 읽기
    input_data: List[int] = list(map(int, sys.stdin.read().split()))
    if not input_data:
        return

    n: int = input_data[0]
    c: int = input_data[1]
    houses: List[int] = sorted(input_data[2:])

    start: int = 1
    end: int = houses[-1] - houses[0]
    result: int = 0

    while start <= end:
        mid: int = (start + end) // 2  # 인접한 공유기 사이의 최소 거리 설정
        count: int = 1  # 첫 번째 집에는 무조건 설치
        last_installed: int = houses[0]

        # mid 거리 이상으로 몇 개 설치 가능한지 확인
        for i in range(1, n):
            if houses[i] >= last_installed + mid:
                count += 1
                last_installed = houses[i]

        # C개 이상 설치 가능하다면 거리 늘리기
        if count >= c:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    print(result)


if __name__ == "__main__":
    solve()