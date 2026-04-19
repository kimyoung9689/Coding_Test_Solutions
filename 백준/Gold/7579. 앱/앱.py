import sys
from typing import List


def solve() -> None:
    # 입력 처리
    input_data: List[str] = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])
    m: int = int(input_data[1])
    memories: List[int] = list(map(int, input_data[2:n + 2]))
    costs: List[int] = list(map(int, input_data[n + 2:]))

    max_cost: int = sum(costs)
    # dp[i]는 비용 i로 얻을 수 있는 최대 메모리
    dp: List[int] = [0] * (max_cost + 1)

    for i in range(n):
        curr_mem: int = memories[i]
        curr_cost: int = costs[i]
        
        # 중복 선택을 방지하기 위해 뒤에서부터 계산 (0-1 Knapsack)
        for j in range(max_cost, curr_cost - 1, -1):
            if dp[j - curr_cost] + curr_mem > dp[j]:
                dp[j] = dp[j - curr_cost] + curr_mem

    # M 바이트 이상을 확보하는 최소 비용 탐색
    answer: int = max_cost
    for cost, mem in enumerate(dp):
        if mem >= m:
            answer = cost
            break

    print(answer)


if __name__ == "__main__":
    solve()