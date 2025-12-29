import sys

def solve() -> None:
    # 입력 받기
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n: int = int(input_data[0])  # 물건 개수
    k: int = int(input_data[1])  # 배낭 무게 제한
    
    # dp[i]는 무게 i일 때 가질 수 있는 최대 가치
    dp: list[int] = [0] * (k + 1)
    
    items: list[tuple[int, int]] = []
    for i in range(n):
        w: int = int(input_data[2 + i * 2])
        v: int = int(input_data[3 + i * 2])
        items.append((w, v))

    # DP 진행
    for weight, value in items:
        # 뒤에서부터 계산해야 같은 물건을 중복해서 담지 않아
        for j in range(k, weight - 1, -1):
            if dp[j] < dp[j - weight] + value:
                dp[j] = dp[j - weight] + value

    print(dp[k])

if __name__ == "__main__":
    solve()