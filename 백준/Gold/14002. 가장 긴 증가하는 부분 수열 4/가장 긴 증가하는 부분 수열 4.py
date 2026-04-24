import sys
from typing import List


def solve_lis() -> None:
    """
    LIS(Longest Increasing Subsequence)의 길이와 수열을 구하고 출력한다.
    """
    # 입력 처리
    try:
        input_data: List[str] = sys.stdin.read().split()
        if not input_data:
            return
            
        n: int = int(input_data[0])
        a: List[int] = list(map(int, input_data[1:]))
    except (ValueError, IndexError):
        return

    # dp[i]: a[i]를 마지막 원소로 가지는 LIS의 길이
    dp: List[int] = [1] * n
    # prev[i]: a[i] 이전에 오는 원소의 인덱스
    prev: List[int] = [-1] * n

    # LIS 길이 계산 (O(N^2))
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j

    # 최대 길이와 그 마지막 인덱스 찾기
    max_length: int = 0
    last_index: int = -1
    for i in range(n):
        if dp[i] > max_length:
            max_length = dp[i]
            last_index = i

    # 수열 역추적
    lis_sequence: List[int] = []
    current: int = last_index
    while current != -1:
        lis_sequence.append(a[current])
        current = prev[current]
    
    # 역순이므로 뒤집기
    lis_sequence.reverse()

    # 결과 출력
    print(max_length)
    print(*(lis_sequence))


if __name__ == "__main__":
    solve_lis()