import sys


def solve() -> None:
    # 입력 속도 향상
    input = sys.stdin.readline
    
    # N: 행, M: 열, K: 체스판 크기
    n, m, k = map(int, input().split())
    board = [input().strip() for _ in range(n)]

    # 2차원 누적 합 배열 (1-based indexing을 위해 크기 +1)
    # diff[i][j]: (i, j)를 체스판(B시작)으로 만들 때 칠해야 하면 1
    sum_pf = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            # 체스판 패턴: (행 인덱스 + 열 인덱스)가 짝수면 시작색, 홀수면 다른색
            # 여기서는 맨 왼쪽 위(0,0)가 'B'인 경우를 기준으로 함
            expected = 'B' if (i + j) % 2 == 0 else 'W'
            val = 1 if board[i][j] != expected else 0
            
            # 누적 합 공식 적용
            sum_pf[i + 1][j + 1] = (val + sum_pf[i][j + 1] + 
                                    sum_pf[i + 1][j] - sum_pf[i][j])

    min_paint = float('inf')

    # K x K 구간 탐색
    for i in range(k, n + 1):
        for j in range(k, m + 1):
            # (i-k, j-k)부터 (i, j)까지의 구간 합 계산
            cnt = (sum_pf[i][j] - sum_pf[i - k][j] - 
                   sum_pf[i][j - k] + sum_pf[i - k][j - k])
            
            # cnt: 'B'로 시작할 때 칠할 횟수
            # k*k - cnt: 'W'로 시작할 때 칠할 횟수
            current_min = min(cnt, k * k - cnt)
            if current_min < min_paint:
                min_paint = current_min

    print(min_paint)


if __name__ == "__main__":
    solve()