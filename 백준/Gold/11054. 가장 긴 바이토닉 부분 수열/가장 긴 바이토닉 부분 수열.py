import sys
from typing import List


def solve() -> None:
    """가장 긴 바이토닉 부분 수열 길이를 계산하고 출력한다."""
    input_data: List[str] = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])
    a: List[int] = [int(x) for x in input_data[1:]]

    # 각 위치에서 끝나는 가장 긴 증가하는 부분 수열(LIS)
    increase: List[int] = [1] * n
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                increase[i] = max(increase[i], increase[j] + 1)

    # 각 위치에서 시작하는 가장 긴 감소하는 부분 수열(LDS)
    decrease: List[int] = [1] * n
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if a[j] < a[i]:
                decrease[i] = max(decrease[i], decrease[j] + 1)

    # 두 값을 더하고 중복된 자기 자신(1)을 뺌
    result: int = 0
    for i in range(n):
        result = max(result, increase[i] + decrease[i] - 1)

    print(result)


if __name__ == "__main__":
    solve()