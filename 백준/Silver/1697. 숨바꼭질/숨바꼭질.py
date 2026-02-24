import sys
from collections import deque


def solve() -> None:
    # 입력 받기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n: int = int(input_data[0])
    k: int = int(input_data[1])
    
    # 최대 범위 설정 (0 ~ 100,000)
    max_pos: int = 100000
    # 각 위치까지 걸리는 시간을 저장하는 리스트 (방문 여부 확인 겸용)
    time_taken: list[int] = [-1] * (max_pos + 1)
    
    # BFS를 위한 큐 생성
    queue: deque[int] = deque([n])
    time_taken[n] = 0
    
    while queue:
        current_pos: int = queue.popleft()
        
        # 동생을 찾으면 시간 출력 후 종료
        if current_pos == k:
            print(time_taken[current_pos])
            return
        
        # 이동 가능한 세 가지 경로 확인
        for next_pos in (current_pos - 1, current_pos + 1, current_pos * 2):
            # 범위 안에 있고, 아직 방문하지 않은 곳이라면
            if 0 <= next_pos <= max_pos and time_taken[next_pos] == -1:
                time_taken[next_pos] = time_taken[current_pos] + 1
                queue.append(next_pos)


if __name__ == "__main__":
    solve()