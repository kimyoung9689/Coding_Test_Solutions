import sys
from typing import List


def solve() -> None:
    """
    백준 11053번 LIS 문제를 해결하는 함수
    입력을 받고 DP를 이용해 가장 긴 증가하는 부분 수열의 길이를 계산
    """
    # 입력 받기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n: int = int(input_data[0])
    # 수열 A 리스트 생성 (PEP 484: 타입 힌트 사용)
    a: List[int] = list(map(int, input_data[1:]))

    # dp[i]는 a[i]를 마지막 숫자로 사용하는 LIS의 길이
    # 처음에는 모두 자기 자신만 포함하니까 1로 초기화해
    dp: List[int] = [1] * n

    # 이중 반복문을 통해 각 숫자마다 앞의 숫자들과 비교해
    for i in range(n):
        for j in range(i):
            # 내 앞(j)에 나(i)보다 작은 숫자가 있다면?
            if a[j] < a[i]:
                # 그 숫자의 줄(dp[j]) 뒤에 서는 게 나은지 확인해
                dp[i] = max(dp[i], dp[j] + 1)

    # 전체 줄 중에서 가장 긴 길이를 출력해
    print(max(dp))


if __name__ == "__main__":
    solve()