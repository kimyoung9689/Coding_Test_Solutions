import sys
from typing import List, Tuple


def solve() -> None:
    """
    두 용액의 합이 0에 가장 가까운 조합을 찾아 출력한다.
    """
    # 입력 받기
    n: int = int(sys.stdin.readline())
    solutions: List[int] = list(map(int, sys.stdin.readline().split()))

    # 1. 정렬 (투 포인터를 사용하기 위한 필수 단계)
    solutions.sort()

    left: int = 0
    right: int = n - 1

    # 최저 합의 절대값을 저장 (초기값은 매우 큰 수)
    min_abs_sum: int = float('inf')
    answer: Tuple[int, int] = (0, 0)

    # 2. 투 포인터 탐색
    while left < right:
        current_sum: int = solutions[left] + solutions[right]

        # 0에 더 가까운 합을 찾은 경우 갱신
        if abs(current_sum) < min_abs_sum:
            min_abs_sum = abs(current_sum)
            answer = (solutions[left], solutions[right])

        # 합의 결과에 따라 포인터 이동
        if current_sum > 0:
            right -= 1
        elif current_sum < 0:
            left += 1
        else:
            # 합이 0이면 더 이상 찾을 필요 없음
            break

    # 결과 출력 (이미 정렬된 상태라 오름차순 보장됨)
    print(answer[0], answer[1])


if __name__ == "__main__":
    solve()