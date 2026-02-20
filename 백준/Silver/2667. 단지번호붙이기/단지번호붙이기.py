import sys
from collections import deque
from typing import List, Tuple

def solve() -> None:
    # 지도 크기 입력
    n_str = sys.stdin.readline().strip()
    if not n_str:
        return
    n: int = int(n_str)
    
    # 지도 정보 입력
    grid: List[List[int]] = [
        list(map(int, sys.stdin.readline().strip())) 
        for _ in range(n)
    ]
    
    visited: List[List[bool]] = [[False] * n for _ in range(n)]
    complex_counts: List[int] = []

    # 상, 하, 좌, 우 이동을 위한 방향 설정
    directions: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(n):
        for c in range(n):
            # 집이 있고 아직 방문하지 않은 곳이라면 새로운 단지 탐색 시작
            if grid[r][c] == 1 and not visited[r][c]:
                count: int = 0
                queue: deque = deque([(r, c)])
                visited[r][c] = True
                
                while queue:
                    curr_r, curr_c = queue.popleft()
                    count += 1
                    
                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc
                        
                        # 지도 범위 안이고, 집이 있으며, 아직 안 가본 곳인가?
                        if 0 <= nr < n and 0 <= nc < n:
                            if grid[nr][nc] == 1 and not visited[nr][nc]:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                
                complex_counts.append(count)

    # 결과 출력 (오름차순 정렬)
    complex_counts.sort()
    print(len(complex_counts))
    for res in complex_counts:
        print(res)

if __name__ == "__main__":
    solve()