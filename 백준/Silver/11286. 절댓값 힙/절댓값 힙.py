import heapq
import sys

def solve() -> None:
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input = sys.stdin.read().split()
    if not input:
        return
    
    n: int = int(input[0])
    operations: list[str] = input[1:]
    
    # (절댓값, 원본값) 형태로 저장할 리스트
    abs_heap: list[tuple[int, int]] = []
    
    results: list[int] = []
    
    for i in range(n):
        x: int = int(operations[i])
        
        if x != 0:
            # (절댓값, 실제값)을 튜플로 추가
            # 1. 절댓값이 작은 순 2. 실제값이 작은 순으로 자동 정렬됨
            heapq.heappush(abs_heap, (abs(x), x))
        else:
            if not abs_heap:
                results.append(0)
            else:
                # 가장 우선순위가 높은(절댓값이 작거나, 실제값이 작은) 원소 제거 및 출력
                results.append(heapq.heappop(abs_heap)[1])
    
    # 한 번에 결과 출력
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    solve()