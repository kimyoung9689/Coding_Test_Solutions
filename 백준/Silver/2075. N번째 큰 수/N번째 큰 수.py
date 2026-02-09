import heapq
import sys

def solve() -> None:
    # 첫 번째 줄에서 N 읽기
    line = sys.stdin.readline()
    if not line:
        return
    n: int = int(line)
    
    min_heap: list[int] = []
    
    # 한 줄씩 읽어서 바로 처리 (메모리 적게 사용)
    for i in range(n):
        row_nums: list[int] = list(map(int, sys.stdin.readline().split()))
        
        for num in row_nums:
            if len(min_heap) < n:
                # 힙에 N개가 채워질 때까지는 그냥 넣기
                heapq.heappush(min_heap, num)
            else:
                # 힙의 최솟값보다 큰 수가 들어오면 교체
                if num > min_heap[0]:
                    heapq.heapreplace(min_heap, num)
                    
    # 마지막에 힙의 루트(가장 작은 값)가 N번째로 큰 수
    print(min_heap[0])

if __name__ == "__main__":
    solve()