import sys
from typing import List


def solve() -> None:
    # 입력 받기
    n: int = int(sys.stdin.readline())
    p_list: List[int] = list(map(int, sys.stdin.readline().split()))

    # 1. 인출 시간이 짧은 순서대로 정렬
    p_list.sort()

    total_wait_time: int = 0  # 모든 사람이 기다린 총 시간
    current_wait_time: int = 0  # 현재 사람이 인출을 마치기까지 걸린 시간

    # 2. 각 사람의 대기 시간을 누적하며 합산
    for time in p_list:
        current_wait_time += time
        total_wait_time += current_wait_time

    # 결과 출력
    print(total_wait_time)


if __name__ == "__main__":
    solve()