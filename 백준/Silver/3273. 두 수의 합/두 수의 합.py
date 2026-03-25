import sys
from typing import List


def solve() -> None:
    """
    수열에서 두 수의 합이 x인 쌍의 개수를 구하여 출력한다.
    """
    # 입력 속도를 위해 sys.stdin.read 사용
    input_data: List[str] = sys.stdin.read().split()
    
    if not input_data:
        return

    n: int = int(input_data[0])
    # n개의 수열 추출
    numbers: List[int] = sorted(map(int, input_data[1:n + 1]))
    # 목표 합 x 추출
    target_x: int = int(input_data[n + 1])

    count: int = 0
    left: int = 0
    right: int = n - 1

    # 투 포인터 이동
    while left < right:
        current_sum: int = numbers[left] + numbers[right]
        
        if current_sum == target_x:
            count += 1
            left += 1
            right -= 1
        elif current_sum < target_x:
            left += 1
        else:
            right -= 1

    print(count)


if __name__ == "__main__":
    solve()