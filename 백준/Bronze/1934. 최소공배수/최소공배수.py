import sys

input = sys.stdin.readline

# 테스트 케이스 개수 T를 입력받음
t = int(input())

# 최대공약수(GCD)를 계산하는 함수
def calculate_gcd(a: int, b: int) -> int:
    # 유클리드 호제법을 사용하여 최대공약수 계산
    while b > 0:
        # a와 b를 나누고, 나머지를 r에 저장
        r = a % b
        # a에 b를 할당
        a = b
        # b에 r을 할당
        b = r
    # 나머지가 0이 되었을 때의 a가 최대공약수
    return a

# T개의 테스트 케이스를 처리
for _ in range(t):
    # 각 줄에서 A와 B를 입력받아 정수로 변환
    a, b = map(int, input().split())

    # 최대공약수(GCD) 계산
    gcd_value = calculate_gcd(a, b)

    # 최소공배수(LCM) 계산: (A * B) / GCD
    # A와 B는 최대 45,000이라서 곱하면 최대 2,025,000,000
    lcm_value = (a * b) // gcd_value

    # 결과 출력
    # 최소공배수를 구하는 식: lcm(a, b) = (a * b) / gcd(a, b)
    print(lcm_value)