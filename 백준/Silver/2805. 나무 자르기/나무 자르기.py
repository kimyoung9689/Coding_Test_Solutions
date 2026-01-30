import sys
from typing import List


def solve() -> None:
    # 빠른 입력을 위해 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])  # 나무의 수
    m: int = int(input_data[1])  # 필요한 나무 길이
    trees: List[int] = list(map(int, input_data[2:]))

    # 이분 탐색 범위 설정
    low: int = 0
    high: int = max(trees)
    result: int = 0

    while low <= high:
        mid: int = (low + high) // 2
        
        # 잘린 나무 길이 합 계산 (리스트 컴프리헨션보다 반복문이 빠를 수 있음)
        total_length: int = 0
        for tree in trees:
            if tree > mid:
                total_length += tree - mid
        
        # 목표 길이 달성 여부에 따라 범위 조정
        if total_length >= m:
            result = mid  # 일단 기록하고 더 높은 높이 시도
            low = mid + 1
        else:
            high = mid - 1

    print(result)


if __name__ == "__main__":
    solve()