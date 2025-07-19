import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int,sys.stdin.readline().split())
    print(a + b)


# t 입력받을 땐 readline을 썼는데 정작 for문에서 input으로 받는 바람에
#  시간초과로 틀리게 됐다.