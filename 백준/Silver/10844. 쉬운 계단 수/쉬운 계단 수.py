import sys


def solve() -> None:
    # 입력 받기
    input_data: str = sys.stdin.readline().strip()
    if not input_data:
        return
    n: int = int(input_data)
    
    mod: int = 1_000_000_000
    
    # dp[길이][마지막숫자] 
    # dp[i][j] : 길이가 i이고 마지막 숫자가 j인 계단 수의 개수
    dp: list[list[int]] = [[0] * 10 for _ in range(n + 1)]
    
    # 길이가 1인 경우 초기화 (0으로 시작 불가)
    for j in range(1, 10):
        dp[1][j] = 1
        
    # DP 진행
    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                # 마지막이 0이면 이전은 1이어야 함
                dp[i][j] = dp[i - 1][1] % mod
            elif j == 9:
                # 마지막이 9이면 이전은 8이어야 함
                dp[i][j] = dp[i - 1][8] % mod
            else:
                # 그 외는 위아래 차이 1인 두 숫자 가능
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % mod
                
    # 최종 결과 출력 (나머지 연산 필수)
    print(sum(dp[n]) % mod)


if __name__ == "__main__":
    solve()