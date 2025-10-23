import math
import sys

# 두 정수 A와 B를 입력받기
a, b = map(int, sys.stdin.readline().split())

# 최대공약수 구하기
gcd_value = math.gcd(a, b)

# 최소공배수(LCM) 계산: (A * B) // GCD(A, B)
lcm_value = (a * b) // gcd_value

# 최소공배수 출력
print(lcm_value)