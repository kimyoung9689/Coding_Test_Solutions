# $2n$의 최대 범위인 246,912까지의 소수 판별
MAX_LIMIT = 123456 * 2 + 1 # 2n까지 포함해야 하므로 +1
is_prime = [True] * MAX_LIMIT # 일단 모두 소수로 가정

# 0과 1은 소수가 아님
if MAX_LIMIT > 0:
    is_prime[0] = False
if MAX_LIMIT > 1:
    is_prime[1] = False

# 에라토스테네스의 체 실행
for i in range(2, int(MAX_LIMIT**0.5) + 1):
    if is_prime[i]: # i가 소수인 경우
        for j in range(i * i, MAX_LIMIT, i):
            is_prime[j] = False # i의 배수들은 소수가 아님

# 테스트 케이스 반복 처리
while True:
    try:
        n_input = input()
    except EOFError:
        break # 입력이 끝나면 종료

    if not n_input:
        continue

    n: int = int(n_input)

    if n == 0:
        break # 0이 입력되면 종료

    count: int = 0
    # n보다 크고 2n보다 작거나 같은 범위의 소수 개수를 셈
    for k in range(n + 1, 2 * n + 1):
        if k < MAX_LIMIT and is_prime[k]:
            count += 1
            
    print(count)