import sys
# 입력이 많으니 sys.stdin.readline 사용
input = sys.stdin.read
# 입력 데이터를 한 번에 읽음
data = input().split()

# 1,000,000까지의 소수를 미리 구하기 위한 준비
MAX_N = 1000000
# 소수 판별 리스트 초기화 (True: 소수 가능성 있음)
is_prime = [True] * (MAX_N + 1)
is_prime[0] = is_prime[1] = False # 0과 1은 소수 아님

# 에라토스테네스의 체 실행
for i in range(2, int(MAX_N**0.5) + 1):
    if is_prime[i]:
        # i의 배수들을 소수가 아니라고 표시
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False

# 소수 리스트 생성 (optional: 속도 최적화에 도움)
# primes = [i for i, is_p in enumerate(is_prime) if is_p]

# 테스트 케이스 개수 T
T = int(data[0])
# N 값들만 추출
N_values = [int(data[i]) for i in range(1, T + 1)]

results = []
# 모든 테스트 케이스 처리
for N in N_values:
    count = 0
    # N = p1 + p2 에서 p1 <= p2 조건 만족을 위해 p1을 N/2까지만 확인
    # N/2의 정수 부분까지만 확인하면 돼.
    # 예: N=10, i는 2, 3, 4까지 확인. (4+6은 3+7의 순서만 바꾼 것)
    for p1 in range(2, N // 2 + 1):
        if is_prime[p1]:
            p2 = N - p1
            # p1과 p2 둘 다 소수인지 확인
            if is_prime[p2]:
                count += 1
    
    results.append(str(count))

# 결과 한 번에 출력
sys.stdout.write('\n'.join(results) + '\n')