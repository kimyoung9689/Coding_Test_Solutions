from typing import List

# N과 M을 입력받음
N, M = map(int, input().split())

# 현재 수열을 저장할 리스트
sequence: List[int] = []

def solve_n_m(count: int, start_num: int) -> None:
    """백트래킹으로 비내림차순 수열을 찾음."""
    # M개의 숫자를 모두 고르면 출력
    if count == M:
        print(' '.join(map(str, sequence)))
        return

    # start_num부터 N까지 반복 (비내림차순 조건)
    for i in range(start_num, N + 1):
        # 숫자 추가
        sequence.append(i)
        
        # 다음 숫자 선택 (중복 허용이므로 i부터 다시 시작)
        solve_n_m(count + 1, i)
        
        # 백트래킹 (방금 넣은 숫자 제거)
        sequence.pop()

# DFS 시작 (0개 선택, 1부터 시작)
solve_n_m(0, 1)