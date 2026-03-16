import collections
import typing


def solve_hide_and_seek() -> None:
    """
    수빈이가 동생을 찾는 가장 빠른 시간을 계산하여 출력한다.
    0-1 BFS 알고리즘을 사용하여 가중치가 0인 순간이동을 우선 처리한다.
    """
    # 입력 받기
    try:
        line: str = input()
        if not line:
            return
        n, k = map(int, line.split())
    except ValueError:
        return

    # 최대 범위 설정 (0 ~ 100,000)
    max_pos: int = 100_000
    # 방문 여부와 시간을 저장하는 리스트 (-1은 미방문)
    dist: typing.List[int] = [-1] * (max_pos + 1)
    
    # 덱(Deque) 생성 및 시작점 설정
    queue: typing.Deque[int] = collections.deque([n])
    dist[n] = 0

    while queue:
        curr: int = queue.popleft()

        # 동생을 찾으면 시간 출력 후 종료
        if curr == k:
            print(dist[curr])
            return

        # 1. 순간이동 (비용 0): 가장 높은 우선순위
        if curr * 2 <= max_pos and dist[curr * 2] == -1:
            dist[curr * 2] = dist[curr]
            queue.appendleft(curr * 2)  # 덱의 앞쪽에 추가

        # 2. 걷기 (비용 1): -1 이동
        if curr - 1 >= 0 and dist[curr - 1] == -1:
            dist[curr - 1] = dist[curr] + 1
            queue.append(curr - 1)      # 덱의 뒤쪽에 추가

        # 3. 걷기 (비용 1): +1 이동
        if curr + 1 <= max_pos and dist[curr + 1] == -1:
            dist[curr + 1] = dist[curr] + 1
            queue.append(curr + 1)      # 덱의 뒤쪽에 추가


if __name__ == "__main__":
    solve_hide_and_seek()