import sys


def solve() -> None:
    # N: 동전 종류 수, K: 목표 금액
    line = sys.stdin.readline().split()
    if not line:
        return
    n, k = map(int, line)
    
    # 동전 가치 리스트 (오름차순으로 입력됨)
    coins: list[int] = [int(sys.stdin.readline()) for _ in range(n)]
    
    count: int = 0
    
    # 가장 큰 동전부터 확인하기 위해 리스트를 역순으로 순회
    for coin in reversed(coins):
        if k == 0:
            break
        
        # 현재 동전으로 만들 수 있는 최대 개수 추가
        count += k // coin
        # 남은 금액 업데이트
        k %= coin
        
    print(count)


if __name__ == "__main__":
    solve()