import sys
# 입력받기, sys.stdin.readline 사용해서 빠르게 처리
m, n = map(int, sys.stdin.readline().split())

# 에라토스테네스의 체를 위한 리스트, n+1 크기로 만들고 True로 초기화
is_prime = [True] * (n + 1)
is_prime[1] = False # 1은 소수가 아님

# 2부터 n의 제곱근까지 반복
for i in range(2, int(n**0.5) + 1):
    if is_prime[i]: # i가 소수일 경우
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

# M부터 N까지 반복하며 소수 출력
for i in range(m, n + 1):
    if is_prime[i]:
        print(i)