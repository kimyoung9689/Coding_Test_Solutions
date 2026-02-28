import collections
from typing import Dict, List, Deque


def solve() -> None:
    """
    뱀과 사다리 게임의 최단 횟수를 BFS로 구하는 함수
    """
    # 1. 입력 받기
    # n: 사다리 개수, m: 뱀의 개수
    try:
        line = input().split()
        if not line:
            return
        n, m = map(int, line)
    except ValueError:
        return

    # 사다리와 뱀 정보를 하나의 딕셔너리에 저장해 (어차피 이동하는 건 똑같으니까!)
    teleports: Dict[int, int] = {}
    for _ in range(n + m):
        start, end = map(int, input().split())
        teleports[start] = end

    # 2. 준비물 만들기
    # board: 각 칸에 도착하기 위한 최소 주사위 횟수 (0으로 초기화)
    # visited: 이미 가본 칸인지 확인하는 리스트
    board_size = 100
    visited: List[bool] = [False] * (board_size + 1)
    
    # 큐(Queue)를 만들어서 (현재 칸, 굴린 횟수)를 넣어줘
    queue: Deque[List[int]] = collections.deque([[1, 0]])
    visited[1] = True

    # 3. BFS 탐색 시작
    while queue:
        current_pos, count = queue.popleft()

        # 100번 칸에 도착하면 횟수 출력하고 종료!
        if current_pos == board_size:
            print(count)
            return

        # 주사위 1부터 6까지 굴리기
        for dice in range(1, 7):
            next_pos = current_pos + dice

            # 보드판 범위 안에 있고, 아직 안 가본 칸이라면?
            if next_pos <= board_size and not visited[next_pos]:
                # 만약 사다리나 뱀이 있는 칸이라면 이동해!
                if next_pos in teleports:
                    next_pos = teleports[next_pos]

                # 이동한 칸도 방문 체크하고 큐에 넣어줘
                if not visited[next_pos]:
                    visited[next_pos] = True
                    queue.append([next_pos, count + 1])


if __name__ == "__main__":
    solve()