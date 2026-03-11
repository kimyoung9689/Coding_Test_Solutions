import sys
from collections import deque
from typing import List, Union


def solve() -> None:
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    t_cases = int(input_data[idx])
    idx += 1
    
    for _ in range(t_cases):
        n = int(input_data[idx])
        idx += 1
        
        # 작년 순위 (1등부터 차례대로 팀 번호)
        last_year = list(map(int, input_data[idx:idx + n]))
        idx += n
        
        # 진입 차수와 인접 행렬 초기화
        indegree = [0] * (n + 1)
        # n이 최대 500이므로 인접 행렬 사용 가능
        adj = [[False] * (n + 1) for _ in range(n + 1)]
        
        # 작년 순위를 바탕으로 그래프 생성 (자신보다 순위 낮은 팀들을 가리킴)
        for i in range(n):
            for j in range(i + 1, n):
                adj[last_year[i]][last_year[j]] = True
                indegree[last_year[j]] += 1
        
        # 상대적 순위 변경 적용
        m = int(input_data[idx])
        idx += 1
        for _ in range(m):
            u = int(input_data[idx])
            v = int(input_data[idx + 1])
            idx += 2
            
            # 간선 방향 뒤집기
            if adj[u][v]:
                adj[u][v] = False
                adj[v][u] = True
                indegree[v] -= 1
                indegree[u] += 1
            else:
                adj[v][u] = False
                adj[u][v] = True
                indegree[u] -= 1
                indegree[v] += 1
        
        # 위상 정렬 시작
        result = []
        queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])
        
        is_uncertain = False
        is_impossible = False
        
        for _ in range(n):
            if not queue:
                is_impossible = True
                break
            if len(queue) > 1:
                is_uncertain = True
                break
            
            curr = queue.popleft()
            result.append(curr)
            
            for next_node in range(1, n + 1):
                if adj[curr][next_node]:
                    indegree[next_node] -= 1
                    if indegree[next_node] == 0:
                        queue.append(next_node)
        
        # 결과 출력
        if is_impossible:
            print("IMPOSSIBLE")
        elif is_uncertain:
            print("?")
        else:
            print(*(result))


if __name__ == "__main__":
    solve()