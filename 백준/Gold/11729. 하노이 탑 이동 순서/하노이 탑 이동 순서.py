import sys
# 재귀 한도를 늘려줘. N이 20일 때 재귀가 깊어질 수 있어.
sys.setrecursionlimit(2000)

def hanoi_tower(n: int, start: int, end: int, auxiliary: int) -> None:
    """
    하노이 탑 이동 과정을 출력하는 재귀 함수

    Args:
        n: 옮길 원판의 개수
        start: 출발 기둥 번호 (1, 2, 또는 3)
        end: 도착 기둥 번호 (1, 2, 또는 3)
        auxiliary: 보조 기둥 번호 (1, 2, 또는 3)
    """
    if n == 1:
        # 1. 원판이 1개일 때: 바로 도착 기둥으로 옮김
        print(f"{start} {end}")
        return

    # 2. n-1개의 원판을 출발 -> 보조 기둥으로 옮김
    hanoi_tower(n - 1, start, auxiliary, end)

    # 3. 가장 큰 1개의 원판을 출발 -> 도착 기둥으로 옮김
    print(f"{start} {end}")

    # 4. 보조에 있는 n-1개의 원판을 보조 -> 도착 기둥으로 옮김
    hanoi_tower(n - 1, auxiliary, end, start)

# 입력 받기
try:
    N: int = int(sys.stdin.readline())
except:
    N = 0

# 최소 이동 횟수 계산 (2^N - 1)
# N이 0일 때 (1<<0) - 1 = 0이 나와서 에러를 막아줌
K: int = (1 << N) - 1

# 결과 출력
print(K)
if N <= 20: # N이 너무 크면 시간 초과/메모리 초과 날 수 있어서 문제 조건 (N<=20)을 고려
    hanoi_tower(N, 1, 3, 2)