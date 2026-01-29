import sys
from typing import List


def solve() -> None:
    # 입력 속도를 위해 sys.stdin.read 사용
    input_data: List[str] = sys.stdin.read().split()
    if not input_data:
        return

    k: int = int(input_data[0])
    n: int = int(input_data[1])
    lan_lengths: List[int] = [int(x) for x in input_data[2:]]

    # 이분 탐색을 위한 시작점과 끝점 설정
    start: int = 1
    end: int = max(lan_lengths)
    result: int = 0

    while start <= end:
        mid: int = (start + end) // 2
        count: int = 0

        # mid 길이로 잘랐을 때 나오는 랜선 개수 합산
        for length in lan_lengths:
            count += length // mid

        # 개수가 충분하면 길이를 더 늘려봄 (오른쪽 탐색)
        if count >= n:
            result = mid
            start = mid + 1
        # 개수가 부족하면 길이를 줄임 (왼쪽 탐색)
        else:
            end = mid - 1

    print(result)


if __name__ == "__main__":
    solve()