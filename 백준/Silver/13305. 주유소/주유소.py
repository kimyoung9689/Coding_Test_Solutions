import sys


def solve() -> None:
    # 도시 개수 입력
    n: int = int(sys.stdin.readline())
    
    # 도로 길이 리스트 (N-1개)
    distances: list[int] = list(map(int, sys.stdin.readline().split()))
    
    # 주유소 가격 리스트 (N개)
    prices: list[int] = list(map(int, sys.stdin.readline().split()))

    # 최소 비용 합계
    total_cost: int = 0
    
    # 현재까지 발견한 가장 저렴한 기름값 (첫 번째 도시 가격으로 초기화)
    min_price: int = prices[0]

    for i in range(n - 1):
        # 현재 도시의 가격이 더 저렴하면 갱신
        if prices[i] < min_price:
            min_price = prices[i]
        
        # 가장 저렴한 가격으로 다음 도시까지 이동
        total_cost += min_price * distances[i]

    print(total_cost)


if __name__ == "__main__":
    solve()