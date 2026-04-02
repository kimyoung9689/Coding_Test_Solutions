import sys
from typing import List


def solve() -> None:
    """
    크누스 최적화(Knuth Optimization)를 사용하여
    파일 합치기 문제를 O(K^2)으로 해결한다.
    """
    input_data: List[str] = sys.stdin.read().split()
    if not input_data:
        return

    ptr: int = 0
    t_cases: int = int(input_data[ptr])
    ptr += 1

    for _ in range(t_cases):
        k: int = int(input_data[ptr])
        ptr += 1
        
        files: List[int] = [int(x) for x in input_data[ptr:ptr + k]]
        ptr += k

        # dp[i][j]: i에서 j까지 합치는 최소 비용
        # opt[i][j]: dp[i][j]가 최소가 되는 최적의 분할 지점 k
        dp: List[List[int]] = [[0] * (k + 1) for _ in range(k + 1)]
        opt: List[List[int]] = [[0] * (k + 1) for _ in range(k + 1)]
        
        # 누적 합 계산
        prefix_sum: List[int] = [0] * (k + 1)
        for i in range(1, k + 1):
            prefix_sum[i] = prefix_sum[i - 1] + files[i - 1]
            # 길이가 1인 구간의 최적 분할 지점 초기화
            opt[i][i] = i

        # 구간 길이 2부터 시작
        for length in range(2, k + 1):
            for i in range(1, k - length + 2):
                j: int = i + length - 1
                dp[i][j] = float('inf')
                
                # Knuth Optimization: opt[i][j-1] <= k <= opt[i+1][j]
                # 탐색 범위를 이전 단계에서 구한 최적 지점 사이로 제한함
                start: int = opt[i][j - 1]
                end: int = opt[i + 1][j]
                
                for m in range(start, end + 1):
                    if m >= j:
                        break
                    
                    cost: int = dp[i][m] + dp[m + 1][j] + (prefix_sum[j] - prefix_sum[i - 1])
                    if dp[i][j] > cost:
                        dp[i][j] = cost
                        opt[i][j] = m
        
        sys.stdout.write(str(dp[1][k]) + '\n')


if __name__ == "__main__":
    solve()