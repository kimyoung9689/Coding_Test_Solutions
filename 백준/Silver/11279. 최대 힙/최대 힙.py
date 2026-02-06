import heapq
import sys
from typing import List


def solve() -> None:
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])
    operations: List[int] = list(map(int, input_data[1:]))

    max_heap: List[int] = []

    for x in operations:
        if x > 0:
            # 최대 힙을 위해 음수로 변환하여 push
            heapq.heappush(max_heap, -x)
        else:
            # 힙이 비어있으면 0 출력
            if not max_heap:
                print(0)
            else:
                # 가장 작은 값(원래 가장 큰 값)을 꺼내서 다시 양수로 변환
                print(-heapq.heappop(max_heap))


if __name__ == "__main__":
    solve()