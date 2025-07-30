# 입력 값 받기
n = int(input())

# 위쪽 피라미드 형태 출력
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

# 아래쪽 피라미드 형태 출력
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))