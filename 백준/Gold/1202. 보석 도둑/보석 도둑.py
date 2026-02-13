import heapq
import sys
from typing import List, Tuple

def solve() -> None:
    # 입력 속도 향상
    input = sys.stdin.readline
    
    # N: 보석 개수, K: 가방 개수
    n, k = map(int, input().split())
    
    # 보석 정보 (무게, 가격)
    jewels: List[Tuple[int, int]] = []
    for _ in range(n):
        jewels.append(tuple(map(int, input().split())))
        
    # 가방 무게 제한
    bags: List[int] = []
    for _ in range(k):
        bags.append(int(input()))
        
    # 무게 기준 오름차순 정렬
    jewels.sort()
    bags.sort()
    
    result: int = 0
    temp_jewels: List[int] = []
    jewel_idx: int = 0
    
    for bag_limit in bags:
        # 현재 가방에 담을 수 있는 모든 보석을 후보군(힙)에 추가
        while jewel_idx < n and jewels[jewel_idx][0] <= bag_limit:
            # 최대 힙을 위해 가격에 마이너스 사용
            heapq.heappush(temp_jewels, -jewels[jewel_idx][1])
            jewel_idx += 1
            
        # 후보군 중 가장 비싼 보석 선택
        if temp_jewels:
            result -= heapq.heappop(temp_jewels)
            
    print(result)

if __name__ == "__main__":
    solve()