import sys
from typing import List

def solve() -> None:
    # 입력 속도를 높이기 위해 사용
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return
        
    v: int = int(data[0])
    e: int = int(data[1])
    
    # 충분히 큰 값으로 무한대 설정 (도로 최대 길이 10,000 * 마을 400개)
    inf: int = 10_000 * 400 + 1
    
    # 그래프 초기화 (1번부터 V번까지 사용하기 위해 V+1 크기)
    graph: List[List[int]] = [[inf] * (v + 1) for _ in range(v + 1)]
    
    # 간선 정보 입력
    idx: int = 2
    for _ in range(e):
        a: int = int(data[idx])
        b: int = int(data[idx + 1])
        c: int = int(data[idx + 2])
        graph[a][b] = c
        idx += 3
        
    # 플로이드-워셜 알고리즘 수행
    # k: 거쳐가는 마을, i: 출발 마을, j: 도착 마을
    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    
    # 최소 사이클 찾기 (자기 자신으로 돌아오는 경로 중 최솟값)
    min_cycle: int = inf
    for i in range(1, v + 1):
        min_cycle = min(min_cycle, graph[i][i])
        
    # 결과 출력
    if min_cycle >= inf:
        print(-1)
    else:
        print(min_cycle)

if __name__ == "__main__":
    solve()