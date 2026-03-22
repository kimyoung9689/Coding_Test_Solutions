import sys
from typing import List

def solve() -> None:
    # 빠른 입력을 위해 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n: int = int(input_data[0])
    m: int = int(input_data[1])
    
    # 충분히 큰 값으로 무한대 설정 (도시 최대 100개 * 비용 최대 100,000)
    inf: int = 100_000_001
    
    # 그래프 초기화
    graph: List[List[int]] = [[inf] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        graph[i][i] = 0
        
    # 버스 정보 입력 (최소 비용만 저장)
    current_idx: int = 2
    for _ in range(m):
        u: int = int(input_data[current_idx])
        v: int = int(input_data[current_idx + 1])
        w: int = int(input_data[current_idx + 2])
        current_idx += 3
        
        if w < graph[u][v]:
            graph[u][v] = w
            
    # 플로이드-워셜 알고리즘 핵심
    for k in range(1, n + 1):  # 거쳐가는 도시
        for i in range(1, n + 1):  # 출발 도시
            for j in range(1, n + 1):  # 도착 도시
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    
    # 결과 출력
    for i in range(1, n + 1):
        row: List[int] = []
        for j in range(1, n + 1):
            if graph[i][j] == inf:
                row.append(0)
            else:
                row.append(graph[i][j])
        print(*(row))

if __name__ == "__main__":
    solve()