import math

def solve():
    """M개 중 N개를 고르는 조합(M C N)을 계산한다."""
    # 테스트 케이스 개수 T
    try:
        T = int(input())
    except EOFError:
        return

    for _ in range(T):
        try:
            # N: 서쪽, M: 동쪽 사이트 수
            N, M = map(int, input().split())
        except EOFError:
            break

        # M C N 계산
        result = math.comb(M, N)
        
        print(result)

solve()