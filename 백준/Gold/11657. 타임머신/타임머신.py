import sys
from typing import List, Tuple

# PEP 8, 484 준수 및 초보자 맞춤 설명

def solve() -> None:
    # 입력 처리
    input_data: List[str] = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])  # 도시 수
    m: int = int(input_data[1])  # 노선 수
    
    # 간선 정보 (시작, 도착, 시간)
    edges: List[Tuple[int, int, int]] = []
    index: int = 2
    for _ in range(m):
        u: int = int(input_data[index])
        v: int = int(input_data[index + 1])
        w: int = int(input_data[index + 2])
        edges.append((u, v, w))
        index += 3

    # 최단 거리 테이블 (무한대로 초기화)
    inf: float = float('inf')
    dist: List[float] = [inf] * (n + 1)
    dist[1] = 0  # 시작 도시

    negative_cycle: bool = False

    # N번 반복 (마지막 N번째는 사이클 확인용)
    for i in range(n):
        for u, v, w in edges:
            # 시작점에서 갈 수 있는 경로가 있고, 더 짧은 길을 찾으면 갱신
            if dist[u] != inf and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                # N번째 반복에서도 갱신되면 음수 사이클 존재
                if i == n - 1:
                    negative_cycle = True

    # 결과 출력
    if negative_cycle:
        print("-1")
    else:
        for i in range(2, n + 1):
            if dist[i] == inf:
                print("-1")
            else:
                print(int(dist[i]))

if __name__ == "__main__":
    solve()