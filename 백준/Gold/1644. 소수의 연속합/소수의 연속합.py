import sys
from typing import List


def solve() -> None:
    # 입력 받기
    raw_input: str = sys.stdin.readline().strip()
    if not raw_input:
        return
    n: int = int(raw_input)

    if n == 1:
        print(0)
        return

    # 1. 에라토스테네스의 체를 이용해 n 이하의 소수 구하기
    is_prime: List[bool] = [True] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    primes: List[int] = [i for i in range(2, n + 1) if is_prime[i]]

    # 2. 투 포인터를 이용해 연속합 계산
    count: int = 0
    current_sum: int = 0
    start: int = 0
    end: int = 0

    while True:
        if current_sum >= n:
            if current_sum == n:
                count += 1
            current_sum -= primes[start]
            start += 1
        elif end == len(primes):
            break
        else:
            current_sum += primes[end]
            end += 1

    print(count)


if __name__ == "__main__":
    solve()