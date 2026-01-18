import sys
from typing import List


def binary_search(target: int, data: List[int]) -> int:
    """이분 탐색을 통해 target이 data에 있는지 확인"""
    low: int = 0
    high: int = len(data) - 1

    while low <= high:
        mid: int = (low + high) // 2
        if data[mid] == target:
            return 1
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return 0


def main() -> None:
    # 입력 속도를 위해 sys.stdin.readline 사용
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # N과 A 배열 처리
    n: int = int(input_data[0])
    a_list: List[int] = sorted(map(int, input_data[1:n+1]))
    
    # M과 찾을 숫자들 처리
    m: int = int(input_data[n+1])
    targets: List[int] = list(map(int, input_data[n+2:]))

    # 결과 출력
    for target in targets:
        print(binary_search(target, a_list))


if __name__ == "__main__":
    main()