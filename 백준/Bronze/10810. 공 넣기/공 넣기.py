import sys # 모듈 불러오기

# n과 m값 입력 받기 (n: 바구니 개수, m: 공 넣는 횟수)
n, m = map(int, sys.stdin.readline().split())

# 바구니 0으로 초기화
baskets = [0] * n

# m개의 줄에 걸쳐서 공 넣기
for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split()) # i: 시작 바구니, j: 끝 바구니, k: 넣을 공 번호

    for idx in range(i - 1, j): # i-1부터 j-1까지 바구니에 공 넣기
        baskets[idx] = k # k번 공 넣기

print(' '.join(map(str, baskets))) # 바구니 상태 출력