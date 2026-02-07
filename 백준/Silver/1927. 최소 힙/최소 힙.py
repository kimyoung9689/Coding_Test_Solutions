import heapq
import sys

def solve() -> None:
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])
    operations: list[str] = input_data[1:]
    
    heap: list[int] = []

    for i in range(n):
        x: int = int(operations[i])
        
        if x > 0:
            # 힙에 자연수 추가
            heapq.heappush(heap, x)
        else:
            # 힙이 비어있으면 0 출력, 아니면 최솟값 삭제 후 출력
            if not heap:
                print(0)
            else:
                print(heapq.heappop(heap))

if __name__ == "__main__":
    solve()