import sys

# N, M을 입력받기
N, M = map(int, sys.stdin.readline().split())

# A를 입력받아 리스트에 저장
A = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    A.append(row)

# B 입력받아 리스트에 저장
B = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    B.append(row)

# A와 B를 더해서 출력
for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print() # 한 줄 출력 후 다음 줄로 넘어감