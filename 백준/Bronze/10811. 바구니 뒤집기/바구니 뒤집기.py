import sys

# N, M 값 입력 받기
N, M = map(int, sys.stdin.readline().split())

# 1부터 N까지 바구니 초기화
baskets = [i for i in range(1, N + 1)]

# M번 바구니 역순 작업 실시
for _ in range(M):
    # i, j 범위 입력
    i, j = map(int, sys.stdin.readline().split())
    
    # 부분 리스트 뒤집어 주기
    baskets[i-1:j] = baskets[i-1:j][::-1]

# 결과 출력
print(' '.join(map(str, baskets)))