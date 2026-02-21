import sys
from typing import List

# 재귀 한도를 늘려줘야 안전해
sys.setrecursionlimit(10**6)

def solve() -> None:
    """
    백준 1012번: 유기농 배추 문제 해결 함수
    """
    try:
        line = sys.stdin.readline()
        if not line:
            return
        t_cases: int = int(line.strip())
    except ValueError:
        return

    for _ in range(t_cases):
        # M: 가로, N: 세로, K: 배추 개수
        m, n, k = map(int, sys.stdin.readline().split())
        
        # 밭 만들기 (0으로 초기화)
        field: List[List[int]] = [[0] * m for _ in range(n)]
        
        # 배추 위치 입력받기
        for _ in range(k):
            x, y = map(int, sys.stdin.readline().split())
            field[y][x] = 1
            
        worm_count: int = 0
        
        # 밭 전체를 돌아보자
        for row in range(n):
            for col in range(m):
                # 배추가 있는 곳을 발견하면!
                if field[row][col] == 1:
                    # 지렁이 한 마리 추가하고 연결된 배추 다 지우기
                    dfs(field, row, col, n, m)
                    worm_count += 1
                    
        print(worm_count)

def dfs(field: List[List[int]], y: int, x: int, n: int, m: int) -> None:
    """
    상하좌우로 연결된 배추를 방문 처리(0으로 변경)하는 함수
    """
    # 밭 밖으로 나가거나 배추가 없는 곳이면 종료
    if x < 0 or x >= m or y < 0 or y >= n or field[y][x] == 0:
        return
    
    # 방문한 배추는 0으로 만들어서 다시 안 오게 해
    field[y][x] = 0
    
    # 상, 하, 좌, 우 확인하기
    dfs(field, y + 1, x, n, m)
    dfs(field, y - 1, x, n, m)
    dfs(field, y, x + 1, n, m)
    dfs(field, y, x - 1, n, m)

if __name__ == "__main__":
    solve()