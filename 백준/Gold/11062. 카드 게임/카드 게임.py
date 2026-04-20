import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(2000)


def solve() -> None:
    """
    카드 게임 문제를 해결하는 함수.
    근우가 얻을 수 있는 최대 점수를 계산하여 출력한다.
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    t_cases = int(input_data[idx])
    idx += 1

    results = []
    for _ in range(t_cases):
        n = int(input_data[idx])
        idx += 1
        cards = [int(x) for x in input_data[idx : idx + n]]
        idx += n

        # dp[i][j]: i번째부터 j번째 카드까지 있을 때 현재 차례인 사람이 얻는 최대 점수
        dp = [[0] * n for _ in range(n)]

        # 카드가 1개만 남았을 때 (기본 사례)
        for i in range(n):
            dp[i][i] = cards[i]

        # 카드의 개수를 늘려가며 DP 테이블 채우기
        for length in range(2, n + 1):  # 구간의 길이
            for i in range(n - length + 1):
                j = i + length - 1
                
                # 왼쪽 카드를 선택하는 경우와 오른쪽 카드를 선택하는 경우 중 최댓값 선택
                # 내가 카드를 가져가면 다음 턴은 상대방이 최선을 다해 점수를 가져감
                # 따라서 (현재 구간의 전체 합 - 상대방이 다음 구간에서 얻을 최대 점수)가 내 점수가 됨
                
                # 구간 합을 미리 구하지 않고 효율적으로 계산하기 위해 
                # 이번 턴에 얻는 이득 = max(왼쪽 카드 - 상대방 최선, 오른쪽 카드 - 상대방 최선) 방식 사용 가능
                # 여기서는 이해하기 쉽게 '전체 합 - 상대방의 최선' 개념을 적용
                
                # 이 문제의 특성을 이용한 점화식:
                # dp[i][j] = max(왼쪽 선택 시 내 점수, 오른쪽 선택 시 내 점수)
                # 내 점수 = (남은 카드들의 총합) - (상대방이 얻을 최선의 점수)
                
                # 구간 합 계산 (매번 계산하지 않도록 누적합을 쓸 수도 있지만 n이 1000이라 아래 방식도 가능)
                # 하지만 성능을 위해 '상대와의 점수 차이'를 저장하는 방식이 깔끔함
                pass

        # 더 효율적인 구현을 위해 Bottom-up 방식 적용
        # dp[i][j]는 i부터 j까지의 카드에서 (내 점수 - 상대 점수)의 최댓값
        diff_dp = [[0] * n for _ in range(n)]
        for i in range(n):
            diff_dp[i][i] = cards[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                diff_dp[i][j] = max(cards[i] - diff_dp[i+1][j], 
                                    cards[j] - diff_dp[i][j-1])

        # (내 점수 + 상대 점수 = 전체 합)
        # (내 점수 - 상대 점수 = diff_dp[0][n-1])
        # 위 두 식을 더하면: 2 * 내 점수 = 전체 합 + diff_dp
        total_sum = sum(cards)
        results.append(str((total_sum + diff_dp[0][n-1]) // 2))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()