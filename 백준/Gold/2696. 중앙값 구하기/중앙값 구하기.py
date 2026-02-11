import heapq
import sys
from typing import List


def solve() -> None:
    # 테스트 케이스 개수
    try:
        line = sys.stdin.readline()
        if not line:
            return
        t: int = int(line.strip())
    except ValueError:
        return

    for _ in range(t):
        # 수열의 크기
        m: int = int(sys.stdin.readline().strip())
        
        # 수열 데이터 읽기 (여러 줄에 걸쳐 있을 수 있음)
        nums: List[int] = []
        while len(nums) < m:
            nums.extend(map(int, sys.stdin.readline().split()))

        # 중앙값 계산을 위한 힙
        max_heap: List[int] = []  # 중앙값보다 작은 값들 (최대 힙)
        min_heap: List[int] = []  # 중앙값보다 큰 값들 (최소 힙)
        medians: List[int] = []

        for i in range(m):
            val: int = nums[i]
            
            # 1. 최대 힙에 먼저 넣고 최소 힙과 균형 맞추기
            if not max_heap or val <= -max_heap[0]:
                heapq.heappush(max_heap, -val)
            else:
                heapq.heappush(min_heap, val)

            # 2. 두 힙의 크기 조정 (max_heap이 하나 더 많거나 같게)
            if len(max_heap) > len(min_heap) + 1:
                heapq.heappush(min_heap, -heapq.heappop(max_heap))
            elif len(min_heap) > len(max_heap):
                heapq.heappush(max_heap, -heapq.heappop(min_heap))

            # 3. 홀수 번째마다 중앙값 저장
            if (i + 1) % 2 == 1:
                medians.append(-max_heap[0])

        # 결과 출력
        print(len(medians))
        for i in range(len(medians)):
            print(medians[i], end=' ')
            if (i + 1) % 10 == 0 or i == len(medians) - 1:
                print()


if __name__ == "__main__":
    solve()