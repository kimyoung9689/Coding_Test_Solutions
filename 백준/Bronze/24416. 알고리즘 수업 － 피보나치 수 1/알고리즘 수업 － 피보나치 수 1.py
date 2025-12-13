import sys

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    # N을 입력받아 정수형으로 변환 (5 <= N <= 40)
    n = int(input())

    # 1. 재귀 호출 (코드1) 실행 횟수 = N번째 피보나치 수 F_N 구하기
    
    # 동적 프로그래밍(DP)을 사용해서 피보나치 수 F_N을 효율적으로 계산
    # 메모이제이션을 위한 리스트 초기화 (인덱스 1부터 사용)
    # n의 최대값은 40이므로 크기는 41로 충분함
    f = [0] * (n + 1)

    # 기본값 설정
    if n >= 1:
        f[1] = 1
    if n >= 2:
        f[2] = 1

    # DP를 이용해 F_N까지 계산
    # for i=3 to n
    for i in range(3, n + 1):
        # F[i] = F[i-1] + F[i-2]
        f[i] = f[i - 1] + f[i - 2]
    
    # 코드1 실행 횟수 = F_N
    code1_count = f[n]

    # 2. 동적 프로그래밍 (코드2) 실행 횟수
    # 코드2는 for i <- 3 to n 에서 총 n - 2번 실행됨
    code2_count = n - 2

    # 결과 출력 (코드1 횟수, 코드2 횟수)
    print(f"{code1_count} {code2_count}")

# 함수 실행
solve()