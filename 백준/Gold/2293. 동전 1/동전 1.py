import sys

def solve() -> None:
    # 입력 속도를 높이기 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])  # 동전 종류 수
    k: int = int(input_data[1])  # 목표 금액
    coins: list[int] = [int(input_data[i]) for i in range(2, n + 2)]

    # dp[i]는 i원을 만드는 경우의 수
    # 목표 금액 k까지 표현해야 하므로 크기를 k + 1로 설정
    dp: list[int] = [0] * (k + 1)
    
    # 0원을 만드는 경우는 아무것도 안 쓰는 경우 1가지
    dp[0] = 1

    for coin in coins:
        # 현재 동전의 가치부터 목표 금액 k까지 순회
        for j in range(coin, k + 1):
            # j원을 만드는 경우의 수에 (j - 현재동전)원을 만드는 경우의 수를 더함
            dp[j] += dp[j - coin]

    # 최종 결과 출력
    print(dp[k])

if __name__ == "__main__":
    solve()