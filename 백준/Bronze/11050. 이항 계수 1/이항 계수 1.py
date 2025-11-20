import math # 수학 계산을 위한 math 모듈을 불러온다

# N과 K를 한 줄에서 입력받아 정수로 변환한다
# 예를 들어, '5 2'가 입력되면 N=5, K=2가 된다
N, K = map(int, input().split())

# 1. 분자: N! (N 팩토리얼)
# math.factorial(N)은 N부터 1까지 모두 곱한 값이다
N_factorial = math.factorial(N) 

# 2. 분모: K! * (N-K)!
# K_factorial = math.factorial(K)
# NK_factorial = math.factorial(N - K)
Denominator = math.factorial(K) * math.factorial(N - K)

# 3. 계산 결과 (정수형)
# 결과를 계산하고, 정수형으로 출력해야 하므로 // (정수 나눗셈)을 사용한다
result = N_factorial // Denominator

# 결과 출력
print(result)