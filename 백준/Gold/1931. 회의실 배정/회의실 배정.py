import sys


def solve() -> None:
    # 빠른 입력을 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])
    meetings: list[tuple[int, int]] = []

    # 데이터 읽기 (시작 시간, 종료 시간)
    for i in range(n):
        start: int = int(input_data[2 * i + 1])
        end: int = int(input_data[2 * i + 2])
        meetings.append((start, end))

    # 1. 종료 시간 기준 오름차순, 2. 시작 시간 기준 오름차순 정렬
    meetings.sort(key=lambda x: (x[1], x[0]))

    count: int = 0
    last_end_time: int = 0

    for start, end in meetings:
        # 현재 회의 시작 시간이 이전 회의 종료 시간 이후라면 선택
        if start >= last_end_time:
            count += 1
            last_end_time = end

    print(count)


if __name__ == "__main__":
    solve()